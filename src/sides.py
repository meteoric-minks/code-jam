from vector import vector, vectorBearing, vectorDistance


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

    def getScreenLocation(self, cameraLocation: vector(), cameraRotation: float, fov: int) -> list:
        """Returns the location on screen and the distance to the corners of the side"""
        output = [[0, 0], [0, 0]]
        cornerA = self.cornerA
        cornerB = self.cornerB
        cornerA -= cameraLocation
        cornerB -= cameraLocation
        cornerA.rotate(-cameraRotation)
        cornerB.rotate(-cameraRotation)
        cornerA += cameraLocation
        cornerB += cameraLocation
        output[0][0] = vectorBearing(cameraLocation, cornerA) / (fov / 2)
        output[1][0] = vectorBearing(cameraLocation, cornerB) / (fov / 2)
        output[0][1] = vectorDistance(cornerA, cameraLocation)
        output[0][1] = vectorDistance(cornerB, cameraLocation)
