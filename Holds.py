import random

class Hold:
    size = ["small","tiny","large","thin","mega", "ratty", ""]
    angle = ["slopey", "incut", "flat", "rounded", ""]
    direction = ["gaston", "sidepull", "undercling", ""]
    def __init__(self):
        self.text = ""
    
    def generateAdjectives(self, levelOfDetail: int):
        if levelOfDetail > 3: 
            # Only have three types of adjectives, 
            #doesn't make sense to use more than one of each (but it would be funny)
            levelOfDetail = 3
        # Pick some adjectives based on the level of detail
        sizeAdj = ""
        angleAdj = ""
        dirAdj = ""
        while levelOfDetail > 0:
            type = random.randint(0,2)
            if type == 0 and sizeAdj == "":
                sizeAdj = random.choice(self.size)
            if type == 1 and angleAdj == "":
                angleAdj = random.choice(self.angle)
            if type == 2 and dirAdj == "":
                dirAdj = random.choice(self.direction)
            levelOfDetail -= 1
        adjList = []
        if sizeAdj:
            adjList.append(sizeAdj)
        if angleAdj:
            adjList.append(angleAdj)
        if dirAdj:
            adjList.append(dirAdj)
        retStr = " ".join(adjList)
        if len(adjList) > 0 and len(retStr) > 0:
            return retStr + " "
        else:
            return ""
    
class Crimp(Hold):
    def __init__(self, levelOfDetail: int):
        try:
            self.angle.remove("incut")
        except ValueError:
            pass
        self.text = self.generateAdjectives(levelOfDetail) + "crimp"

class Sloper(Hold):
    def __init__(self, levelOfDetail: int):
        try:
            self.angle.remove("slopey")
        except ValueError:
            pass
        self.text = self.generateAdjectives(levelOfDetail) + "sloper"

class Jug(Hold):
    def __init__(self, levelOfDetail: int):
        try:
            self.angle.remove("flat")
        except ValueError:
            pass  # do nothing!
        self.text = self.generateAdjectives(levelOfDetail) + "jug"

class Pocket(Hold):
    def __init__(self, levelOfDetail: int):
        self.text = self.generateAdjectives(levelOfDetail) + "pocket"