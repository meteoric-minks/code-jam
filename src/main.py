#!/usr/bin/env python

import sys
from collections import namedtuple
from typing import Dict

from blessed import Terminal
from blessed.keyboard import Keystroke


def echo(text: str) -> None:
    """Doc string"""
    sys.stdout.write(u'{0}'.format(text))
    sys.stdout.flush()


# a box is a list of (y, x) segments Locations
Location = namedtuple('Point', ('y', 'x',))


# A direction is a bearing, fe.
# y=0, x=-1 = move right
# y=1, x=0 = move down
Direction = namedtuple('Direction', ('y', 'x',))


# these functions return a new Location instance, given
# the direction indicated by their name.
LEFT = (0, -1)
RIGHT = (0, 1)
UP = (-1, 0)
DOWN = (1, 0)


def left_of(segment: list, term: Terminal) -> Location:
    """Doc string"""
    return Location(y=segment.y,
                    x=max(0, segment.x - 1))


def right_of(segment: list, term: Terminal) -> Location:
    """Doc string"""
    return Location(y=segment.y,
                    x=min(term.width - 1, segment.x + 1))


def above(segment: list, term: Terminal) -> Location:
    """Doc string"""
    return Location(
        y=max(0, segment.y - 1),
        x=segment.x)


def below(segment: list, term: Terminal) -> Location:
    """Doc string"""
    return Location(
        y=min(term.height - 1, segment.y + 1),
        x=segment.x)


def next_bearing(term: Terminal, inp_code: Keystroke, bearing: Direction) -> Dict:
    """Doc string"""
    return {
        term.KEY_LEFT: left_of,
        term.KEY_RIGHT: right_of,
        term.KEY_UP: above,
        term.KEY_DOWN: below,
    }.get(inp_code,
          # direction function given the current bearing
          {LEFT: left_of,
           RIGHT: right_of,
           UP: above,
           DOWN: below}[(bearing.y, bearing.x)])


def change_bearing(f_mov: Dict, segment: list, term: Terminal) -> Direction:
    """Doc string"""
    return Direction(
        f_mov(segment, term).y - segment.y,
        f_mov(segment, term).x - segment.x)


def main() -> None:
    """Doc string"""
    term = Terminal()
    box = [Location(x=term.width // 2, y=term.height // 2)]
    bearing = Direction(*LEFT)
    direction = left_of
    color_head = term.red_reverse
    color_bg = term.on_blue
    echo(term.move_yx(1, 1))
    echo(color_bg(term.clear))

    inp = None
    echo(term.move_yx(term.height, 0))
    with term.hidden_cursor(), term.cbreak(), term.location():
        while inp not in (u'q', u'Q'):
            head = box.pop()
            echo(term.move_yx(*head) + color_head(u'+'))
            if box:
                echo(term.move_yx(*(box[-1])))
                echo(color_bg(u' '))
            echo(term.move_yx(*head))
            inp = term.inkey()
            nxt_direction = next_bearing(term, inp.code, bearing)
            nxt_bearing = change_bearing(nxt_direction, head, term)

            direction = nxt_direction
            bearing = nxt_bearing

            box.extend([head, direction(head, term)])
    echo(term.normal)


if __name__ == '__main__':
    main()
