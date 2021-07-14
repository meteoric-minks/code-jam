from blessed import Terminal

from application.dungeon import Dungeon, Room
from application.menu import Button, Menu, TextUI


def test_text_ui() -> None:
    """This is the example test that shows that package initialises without errors"""
    term = Terminal()
    tui = TextUI(term)
    menu = Menu(tui)
    ui = TextUI(term, window=menu)
    assert ui.term is term


def test_selected_buttons() -> None:
    """Checks that the first button is selected"""
    term = Terminal()
    tui = TextUI(term)
    buttons = [Button(tui) for _ in range(3)]
    menu = Menu(tui, buttons=buttons)
    assert menu.selected is buttons[0]


def test_button_switch_down() -> None:
    """Checks that you can scroll selected buttons down"""
    term = Terminal()
    tui = TextUI(term)
    buttons = [Button(tui) for _ in range(3)]
    menu = Menu(tui, buttons=buttons)
    assert menu.selected is buttons[0]
    menu.selection_down()
    assert menu.selected is buttons[1]
    menu.selection_down()
    assert menu.selected is buttons[2]
    menu.selection_down()
    assert menu.selected is buttons[0]


def test_button_switch_up() -> None:
    """Checks that you can scroll selected buttons up"""
    term = Terminal()
    tui = TextUI(term)
    buttons = [Button(tui) for _ in range(3)]
    menu = Menu(tui, buttons=buttons)
    assert menu.selected is buttons[0]
    menu.selection_up()
    assert menu.selected is buttons[2]
    menu.selection_up()
    assert menu.selected is buttons[1]
    menu.selection_up()
    assert menu.selected is buttons[0]


def test_dungeon_add_room() -> None:
    """Checks that dungeons store their rooms correctly"""
    room1 = Room(0, 0)
    room2 = Room(10, 6)
    dungeon = Dungeon()

    dungeon.add_room(room1)
    dungeon.add_room(room2)

    assert dungeon.rooms[0] is room1
    assert dungeon.rooms[1] is room2
