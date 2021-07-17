import functools

from blessed import Terminal

from application.ascii_box import Double, Heavy
from application.ascii_drawing import DrawingChar
from application.dungeon import Character, Dungeon, Item, Room
from application.menu import Button, DungeonEngine, Menu, TextUI


def setup_dungeon() -> Dungeon:
    """Setup the dungeon and rooms"""
    item0 = Item(1, 1, DrawingChar.Vase)
    item1 = Item(4, 2, DrawingChar.Box)
    item2 = Item(8, 1, DrawingChar.Vase)

    Hroom0 = Room(0, 0, width=16, c=Heavy)
    Hroom0.add_item(item0)
    Hroom0.add_item(item1)

    Hroom1 = Room(15, 0, width=12, height=4, c=Heavy)

    Hroom2 = Room(24, 3, c=Heavy)

    Droom0 = Room(15, 3, c=Double)
    Droom0.add_item(item2)

    Droom1 = Room(24, 6, width=30, height=3, c=Double)

    dung = Dungeon()
    dung.add_room(Hroom0)
    dung.add_room(Hroom1)
    dung.add_room(Hroom2)
    dung.add_room(Droom0)
    dung.add_room(Droom1)

    char = Character(dung, 2, 2, c=DrawingChar.AltCharacter)
    dung.set_character(char)

    return dung


def show_menu() -> None:
    """Shows a menu with start and end buttons. Start button shows a message box"""
    term = Terminal()
    tui = TextUI(term)

    dung = setup_dungeon()

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
