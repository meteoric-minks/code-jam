class vector:
    """Basic 2D vectors for making more readable code"""

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __add__(self, other) -> None:
        self.x += other.x
        self.y += other.y

    def size(self) -> float:
        """Calculates the hypotemuse of a vector"""
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5


def distance(vectorA: vector(), vectorB: vector()) -> float:
    """Calculates the distance between two vectors"""
    finalVector = vector(abs(vectorA.x - vectorB.x), abs(vectorA.y - vectorB.y))
    return finalVector.size()
