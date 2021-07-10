from vector import vector

class side:
    def __init__(self,cornerA,cornerB):
        self.cornerA=cornerA
        self.cornerB=cornerB
        self.extremesCalc()

    def extremesCalc(self):
        #gets the min and max point of the side > this is just for convenience later on
        self.mins = vector(min(self.cornerA.x,self.cornerB.x),min(self.cornerA.y,self.cornerB.y))
        self.maxs = vector(max(self.cornerA.x,self.cornerB.x),max(self.cornerA.y,self.cornerB.y))

    #use to translate a side
    def move(self,translationVector):
        self.cornerA+=translationVector
        self.cornerB+=translationVector
        self.extremesCalc()
