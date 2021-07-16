from .ascii_box import Light, LineChar


class Room:
    """Represents a single room in a dungeon."""

    def __init__(self,
                 x: int,  # Coords of Top Left
                 y: int,
                 width: int = 10,  # Width and Height
                 height: int = 6,
                 c: LineChar = Light,  # Which drawing chars to use
                 ):

        self.x, self.y = x, y
        self.width, self.height = width, height

        self.char = c

    def intersects(self, x0: int, y0: int, x1: int, y1: int) -> bool:
        """Calculate if the room intersects some box.

        Will be used to check if the room should be rendered at a given time.

        x0,y0 will represent the top left, x1,y1 represents the bottom right.
        Note: this is inclusive, i.e. if the rectantangles only touch it is still counted as intersecting.
        """
        if (
            (x0 > (self.x + self.width))  # Box is to the right of room
            or (self.x > x1)  # Room is to the right of box
        ):
            return False

        elif (
            (y0 > (self.y + self.height))  # Box is below room
            or (self.y > y1)  # Room is below box
        ):
            return False

        else:  # If none of these conditions are true, they must overlap
            return True

    def render(self) -> list[str]:
        """Will return a rendered box of the room and should include anything within the room.

        Returns a list of one-line strings.
        Returning a list will make it much easier to add spaces on the left so it can be rendered in the correct
        place on the screen.
        """
        # Start with a blank 2D list
        # Lists are much easier to work with since individual items can be set, unlike strings
        image = [[" " for x in range(self.width)] for y in range(self.height)]

        # Top and bottom row
        image[0][0] = self.char.DownRight.value
        image[0][-1] = self.char.DownLeft.value

        image[-1][0] = self.char.UpRight.value
        image[-1][-1] = self.char.UpLeft.value

        for n in range(1, self.width - 1):
            image[0][n] = self.char.Horizontal.value
            image[-1][n] = self.char.Horizontal.value

        # Sides
        for n in range(1, self.height - 1):
            image[n][0] = self.char.Vertical.value
            image[n][-1] = self.char.Vertical.value

        # Join rows
        image = list(map(lambda x: "".join(x), image))

        return image


class Dungeon:
    """Represents an entire dungeon.

    A single instance will likely represent either the world or a single level.
    """

    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room) -> None:
        """Adds a room to the dungeon."""
        self.rooms.append(room)