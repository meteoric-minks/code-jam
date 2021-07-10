class vector:
    """Basic 2D vectors for making more readable code"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        self.x += other.x
        self.y += other.y

    def size(self):
        """calculates the hypotemuse of a vector"""
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def distance(vectorA, vectorB):
        """calculates the distance between two vectors"""
       finalVector=vector(abs(vectorA.x - vectorB.x), abs(vectorA.y - vectorB.y))
       return finalVector.size()
