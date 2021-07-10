from vector import vector


class side:
    """Side objects to make up the geometry of the world"""

    def __init__(self, cornerA: vector(), cornerB: vector()) -> None:
        self.cornerA = cornerA
        self.cornerB = cornerB
        self.extremesCalc()

    def extremesCalc(self) -> None:
        """Gets the min and max point of the side"""
        self.mins = vector(min(self.cornerA.x, self.cornerB.x), min(self.cornerA.y, self.cornerB.y))
        self.maxs = vector(max(self.cornerA.x, self.cornerB.x), max(self.cornerA.y, self.cornerB.y))

    def move(self, translationVector: vector()) -> None:
        """Translates a side along a given vector"""
        self.cornerA += translationVector
        self.cornerB += translationVector
        self.extremesCalc()
