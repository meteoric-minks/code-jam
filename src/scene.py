class bar:
    """The bars that appear on screen"""

    def __init__(self):
        self.color = None
        self.texture = None
        self.distance = None

    def addWall(self, color: tuple, texture: str, distance: float) -> None:
        """Updates the bar's properties the wall if it's closer than previous walls"""
        if self.distance is None or self.distance > distance:
            self.distance = distance


# class room:
#    """Room object"""
#
#    def __init__(self):
#        self.walls = []
#
#    def render(self, playerLocation: vector, playerRotation: float, fov: int, resolution: list) -> None:
#        """Renders the scene in the terminal"""
#        frame = [bar() for i in range(resolution[0])]
#        for eachWall in self.walls:
#            wallLocation = eachWall.getScreenLocation(playerLocation, playerRotation, fov)
#            gradient = (wallLocation[0][1] - wallLocation[1][1]) / (wallLocation[0][0] - wallLocation[1][0])
