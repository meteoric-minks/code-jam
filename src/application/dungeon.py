from ascii_box import Light, LineChar


class Room:
    """Represents a single room in a dungeon."""

    def __init__(self,
                 x: int,  # Coords of Top Left
                 y: int,
                 width: int = 10,  # Width and Height
                 height: int = 6,
                 c: LineChar = Light,  # Which drawing chars to use
                 ):

        self.coord = (x, y)
        self.size = (width, height)

        self.char = c

    def intersects(self, x0: int, y0: int, x1: int, y1: int) -> bool:
        """Calculate if the room intersects some box.

        Will be used to check if the room should be rendered at a given time.
        """
        pass

    def render(self) -> list[str]:
        """Will return a rendered box of the room and should include anything within the room.

        Returns a list of one-line strings.
        """
        pass


class Dungeon:
    """Represents an entire dungeon.

    A single instance will likely represent either the world or a single level.
    """

    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room) -> None:
        """Adds a room to the dungeon."""
        self.rooms.append(room)
