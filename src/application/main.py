import time

from application.menu import MainMenu
from blessed import Terminal


def main() -> str:
    """This is a start of application's structure"""
    term = Terminal()
    # to avoid "never used" from flake
    print(term)
    return "Hello World!"


def show_menu():
    term = Terminal()
    menu = MainMenu(term)
    with term.fullscreen(), term.hidden_cursor():
        menu.show()
        with term.cbreak():
            while True:
                pressed = term.inkey().code
                if pressed in (term.KEY_Q, term.KEY_ESCAPE):
                    break
                if pressed in (term.KEY_UP,):
                    menu.selection_up()
                    menu.show()
                if pressed in (term.KEY_DOWN,):
                    menu.selection_down()
                    menu.show()
                if pressed in (term.KEY_ENTER, term.KEY_SPACE):
                    menu.selected.action()
                    time.sleep(1)
                    break


if __name__ == '__main__':
    show_menu()
