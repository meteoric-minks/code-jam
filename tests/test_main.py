from blessed import Terminal

from application.ascii_box import Heavy
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


def test_room_intersection() -> None:
    """Test Room.intersects"""
    room = Room(5, 5, 10, 5)

    assert room.intersects(0, 0, 3, 10) is False  # Box is left of Room
    assert room.intersects(3, 2, 8, 4) is False  # Box is above of Room

    assert room.intersects(1, 0, 8, 6) is True
    assert room.intersects(2, 4, 20, 20) is True  # Room is fully enclosed
    assert room.intersects(6, 6, 12, 8) is True  # Box is fully enclosed
    assert room.intersects(15, 6, 20, 8) is True  # Only touches


def test_room_render() -> None:
    """Test room.render"""
    room = Room(5, 3, 12, 4, c=Heavy)

    render = room.render()
    render = "\n".join(render)

    target_render = """┏━━━━━━━━━━┓
┃          ┃
┃          ┃
┗━━━━━━━━━━┛"""

    assert render == target_render
