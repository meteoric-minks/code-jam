import functools

from blessed import Terminal

from application.ascii_box import Double, Heavy
from application.ascii_drawing import DrawingChar
from application.dungeon import Character, Dungeon, Item, Room
from application.menu import Button, DungeonEngine, Menu, TextUI


def show_menu() -> None:
    """Shows a menu with start and end buttons. Start button shows a message box"""
    term = Terminal()
    tui = TextUI(term)

    item0 = Item(1, 1, DrawingChar.Vase)
    item1 = Item(4, 2, DrawingChar.Box)
    item2 = Item(8, 1, DrawingChar.Vase)

    room0 = Room(0, 0, c=Heavy)
    room0.add_item(item0)
    room0.add_item(item1)

    room1 = Room(10, 3, c=Double)
    room1.add_item(item2)

    dung = Dungeon()
    dung.add_room(room0)
    dung.add_room(room1)

    char = Character(dung, 2, 2, c=DrawingChar.AltCharacter)
    dung.set_character(char)

    dung_wrapper = DungeonEngine(tui, dung)

    # messagebox = MessageBox(tui, title="Start", message="Press esc to exit")
    # makes a window-changing callback
    show_messagebox = functools.partial(setattr, tui, 'window', dung_wrapper)

    start_button = Button(tui, title="Start", action=show_messagebox)
    exit_button = Button(tui, title="Exit", action=tui.exit)
    buttons = [start_button, exit_button]

    main_menu = Menu(tui, title="Main Menu", width=50, buttons=buttons)
    tui.window = main_menu
    tui.run()


if __name__ == '__main__':
    show_menu()
