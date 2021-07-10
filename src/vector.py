from math import atan, cos, radians, sin


class vector:
    """Basic 2D vectors for making more readable code"""

    def __init__(self, x=0, y=0) -> None:  # noqa: ANN001
        self.x = x
        self.y = y

    def __add__(self, other):  # noqa: ANN001
        self.x += other.x
        self.y += other.y

    def __sub__(self, other):  # noqa: ANN001
        self.x -= other.x
        self.y -= other.y

    def size(self) -> float:
        """Calculates the hypotemuse of a vector"""
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def rotate(self, angle: float) -> None:
        """Rotates the vector clockwise around the origin (angle should be in degrees)"""
        angle = radians(angle)
        s = sin(angle)
        c = cos(angle)
        newVector = vector()
        newVector.x = (self.x * c) - (self.y * s)
        newVector.y = (self.x * s) + (self.y * c)
        self = newVector


def vectorDistance(vectorA: vector, vectorB: vector) -> float:
    """Calculates the distance between two vectors"""
    finalVector = vector(abs(vectorA.x - vectorB.x), abs(vectorA.y - vectorB.y))
    return finalVector.size()


def vectorBearing(vectorA: vector, vectorB: vector) -> float:
    """Calculates the bearing of vectorB from vectorA"""
    newVector = vectorB-vectorA
    return atan(newVector.x / newVector.y)
