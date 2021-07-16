from enum import Enum


class LineChar(Enum):
    """A parent class that represents lines in ASCII art"""

    def __str__(self):
        """Printing line character prints its value"""
        return self.value


class Light(LineChar):
    """Thin lines"""

    Horizontal = '─'
    Vertical = '│'
    DownRight = '┌'
    DownLeft = '┐'
    UpRight = '└'
    UpLeft = '┘'
    VerticalRight = '├'
    VerticalLeft = '┤'
    DownHorizontal = '┬'
    UpHorizontal = '┴'
    VerticalHorizontal = '┼'


class Heavy(LineChar):
    """Thick lines"""

    Horizontal = '━'
    Vertical = '┃'
    DownRight = '┏'
    DownLeft = '┓'
    UpRight = '┗'
    UpLeft = '┛'
    VerticalRight = '┣'
    VerticalLeft = '┫'
    DownHorizontal = '┳'
    UpHorizontal = '┻'
    VerticalHorizontal = '╋'


class Double(LineChar):
    """Double line"""

    Horizontal = '═'
    Vertical = '║'
    DownRight = '╔'
    DownLeft = '╗'
    UpRight = '╚'
    UpLeft = '╝'
    VerticalRight = '╠'
    VerticalLeft = '╣'
    DownHorizontal = '╦'
    UpHorizontal = '╩'
    VerticalHorizontal = '╬'


class DrawingChar(Enum):
    """Characters for drawing things, other than lines."""

    def __str__(self):
        """Printing line character prints its value"""
        return self.value

    Box = '▣'
    Vase = '⚱'
