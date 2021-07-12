import functools

from blessed import Terminal

from application.menu import Button, Menu, MessageBox, TextUI


def show_menu() -> None:
    """Shows a menu with start and end buttons. Start button shows a message box"""
    term = Terminal()
    tui = TextUI(term)

    messagebox = MessageBox(tui, title="Start", message="Press esc to exit")
    # makes a window-changing callback
    show_messagebox = functools.partial(setattr, tui, 'window', messagebox)

    start_button = Button(tui, title="Start", action=show_messagebox)
    exit_button = Button(tui, title="Exit", action=tui.exit)
    buttons = [start_button, exit_button]

    main_menu = Menu(tui, title="Main Menu", width=50, buttons=buttons)
    tui.window = main_menu
    tui.run()


if __name__ == '__main__':
    show_menu()
