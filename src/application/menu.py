class Button:
    def __init__(self, term, title: str):
        self.term = term
        self.title = title
        self.width = 20
        self.selected = False

    def show(self):
        header = "-" * self.width
        body = f"|{self.title.center(self.width - 2)}|"
        button = '\n'.join([header, body, header])
        return button

    def action(self):
        print(self.term.clear + self.term.home)
        print(self.term.center(f"You selected {self.title}"))


class MainMenu:
    def __init__(self, term):
        self.title = "Main menu"
        self.width = 50
        self.term = term
        self.buttons = [Button(term, "Start"), Button(term, "Exit")]
        self.selected_id = 0
        self.selected = self.buttons[self.selected_id]
        self.selected.selected = True

    def show(self):
        term = self.term
        print(term.clear + term.home)
        header = "=" * self.width
        print(header)
        print(f"|{term.bold(self.title.center(self.width - 2))}|")
        for button in self.buttons:
            button_str = button.show()
            for line in button_str.split('\n'):
                # removes newlines
                line = line.strip()
                line = line.center(self.width - 2)
                if button.selected:
                    line = term.green(line)
                line = f"|{line}|"
                print(line)
        print(header)

    def selection_up(self):
        self.selected.selected = False
        self.selected_id += 1
        if self.selected_id >= len(self.buttons):
            self.selected_id = 0
        self.selected = self.buttons[self.selected_id]
        self.selected.selected = True

    def selection_down(self):
        self.selected.selected = False
        self.selected_id -= 1
        if self.selected_id < 0:
            self.selected_id = len(self.buttons) - 1
        self.selected = self.buttons[self.selected_id]
        self.selected.selected = True