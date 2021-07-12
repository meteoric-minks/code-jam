from __future__ import annotations

import functools
import sys
from abc import ABC, abstractmethod
from enum import Enum
from typing import Callable, Optional

from blessed import Terminal
from blessed.keyboard import Keystroke

echo = functools.partial(print, sep='', flush=True)

KeyCode = int


class BoxDraw(Enum):
    """Elements for construction the borders of UI elements"""

    VERTICAL = '║'
    HORISONTAL = '═'
    TOP_LEFT = '╔'
    TOP_RIGHT = '╗'
    BOT_RIGHT = '╝'
    BOT_LEFT = '╚'


class UIElement(ABC):
    """Basic class for UI elements"""

    def __init__(self, tui: TextUI, width: int = 50, title: str = '',
                 key_actions: Optional[dict[KeyCode, Callable]] = None):
        self.tui = tui
        self.term = tui.term
        self.width = width
        self.title = title
        self.key_actions = key_actions if key_actions else {}

    def handle_input(self, key: Keystroke) -> None:
        """Handles a key press"""
        code = key.code
        if code in self.key_actions:
            self.key_actions[code]()

    def make_box(self, lines: list[str]) -> list[str]:
        """Surrounds UI element with lines"""
        top = BoxDraw.TOP_LEFT.value + BoxDraw.HORISONTAL.value * (self.width - 2) + BoxDraw.TOP_RIGHT.value
        lines = [f"{BoxDraw.VERTICAL.value}{line}{BoxDraw.VERTICAL.value}" for line in lines]
        bottom = BoxDraw.BOT_LEFT.value + BoxDraw.HORISONTAL.value * (self.width - 2) + BoxDraw.BOT_RIGHT.value
        return [top, *lines, bottom]

    @abstractmethod
    def show(self) -> list[str]:
        """Returns string representation of UI object"""
        pass


class Button(UIElement):
    """Element that can be selected and pressed, activating the callback"""

    def __init__(self, tui: TextUI, title: str = '', width: int = 20, action: Optional[Callable] = None):
        super().__init__(tui, width=width, title=title)
        self.title = title
        self.highlighted = False
        self.action = action

    def show(self) -> list[str]:
        """Returns string representation of a button"""
        button = [self.term.center(self.title, self.width - 2)]
        button = self.make_box(button)
        if self.highlighted:
            button = [self.term.green(line) for line in button]
        return button

    def press(self) -> None:
        """Activates the callback"""
        if self.action:
            self.action()


class Menu(UIElement):
    """UI element with several selectable buttons"""

    def __init__(self, tui: TextUI, title: str = '', buttons: list[Button] = None, width: int = 50):
        super().__init__(tui, title=title, width=width)
        self.buttons = buttons if buttons is not None else []

        self._selected = None
        self.selected = buttons[0] if buttons else None

        self.key_actions = {
            self.term.KEY_ENTER: self.press_selected,
            self.term.KEY_UP: self.selection_up,
            self.term.KEY_DOWN: self.selection_down,
            self.term.KEY_ESCAPE: self.tui.exit,
        }

    def show(self) -> list[str]:
        """Returns string representation of UI element"""
        header = self.term.center(self.title, self.width - 2)
        header = self.term.bold(header)
        menu = [header]
        for button in self.buttons:
            button_lines = button.show()
            # embeds the button inside the body
            button_lines = [self.term.center(line, self.width - 2) for line in button_lines]
            menu.extend(button_lines)
        menu = self.make_box(menu)
        return menu

    def selection_down(self) -> None:
        """Selects next button, wraps"""
        if not self.buttons:
            return
        assert self.selected is not None
        selected_id = self.buttons.index(self.selected)
        selected_id += 1
        if selected_id >= len(self.buttons):
            selected_id = 0
        self.selected = self.buttons[selected_id]

    def selection_up(self) -> None:
        """Selects previous button, wraps"""
        if not self.buttons:
            return
        assert self.selected is not None
        selected_id = self.buttons.index(self.selected)
        selected_id -= 1
        if selected_id < 0:
            # last
            selected_id = -1
        self.selected = self.buttons[selected_id]

    def press_selected(self) -> None:
        """Presses currently selected button"""
        if self.selected:
            self.selected.press()

    @property
    def selected(self) -> Optional[Button]:
        """Return currently selected button"""
        return self._selected

    @selected.setter
    def selected(self, button: Optional[Button]) -> None:
        """Selects another button"""
        if (old_button := self._selected) is not None:
            old_button.highlighted = False
        if button is not None:
            button.highlighted = True
        self._selected = button
        self.tui.redraw()


class MessageBox(UIElement):
    """Show a message, can be closed"""

    def __init__(self, tui: TextUI, title: str = '', message: str = '', width: int = 50):
        super().__init__(tui, title=title, width=width)

        # doesn't handle multiline messages yet
        if len(message) > self.width - 2:
            raise ValueError("Message too long")

        self.title = title
        self.message = message

        self.key_actions = {
            self.term.KEY_ESCAPE: self.tui.exit,
        }

    def show(self) -> list[str]:
        """Returns string representation of UI element"""
        title = self.title.center(self.width - 2)
        message = self.message.center(self.width - 2)
        boxed = self.make_box([title, message])
        return boxed


class TextUI:
    """Manager class for UI elements"""

    def __init__(self, term: Terminal, window: Optional[UIElement] = None):
        self.term = term
        self._window = window
        self.redraw()

    def run(self) -> None:
        """Starts the program's event handling hoop"""
        with self.term.fullscreen(), self.term.hidden_cursor():
            with self.term.cbreak():
                self.redraw()
                while True:
                    pressed = self.term.inkey()
                    if win := self.window:
                        win.handle_input(pressed)
                    else:
                        sys.exit()

    @property
    def window(self) -> Optional[UIElement]:
        """Shows the current active window"""
        return self._window

    @window.setter
    def window(self, new_window: Optional[UIElement]) -> None:
        """Changes the window and redraws the screen"""
        self._window = new_window
        self.redraw()

    def redraw(self) -> None:
        """Clears the screen and redraws the current window"""
        echo(self.term.home + self.term.clear)
        if self.window:
            for line in self.window.show():
                echo(line)

    def exit(self) -> None:
        """Exits the program"""
        self.window = None
        sys.exit()
