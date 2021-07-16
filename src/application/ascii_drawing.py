from enum import Enum


class DrawingChar(Enum):
    """Characters for drawing things, other than lines."""

    def __str__(self):
        """Printing line character prints its value"""
        return self.value

    Box = '▣'
    Vase = '⚱'
