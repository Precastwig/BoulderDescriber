import random

class Move:
    size = ["small", "big", "powerful", "tiny", ""]
    direction = ["left hand", "right hand", ""]
    mtype = ["stretch", "bump", "throw", "snatch", "lock-off", "udge", "dyno", "deadpoint", "slap", "move"]
    
    def __init__(self, levelofdetail: int):
        self.text = self.generateAdjectives(levelofdetail) + random.choice(self.mtype)
    
    def generateAdjectives(self, levelOfDetail: int):
        if levelOfDetail > 3: 
            # Only have three types of adjectives, 
            #doesn't make sense to use more than one of each (but it would be funny)
            levelOfDetail = 3
        # Pick some adjectives based on the level of detail
        sizeAdj = ""
        dirAdj = ""
        while levelOfDetail > 0:
            type = random.randint(0,2)
            if type == 0 and sizeAdj == "":
                sizeAdj = random.choice(self.size)
            if type == 2 and dirAdj == "":
                dirAdj = random.choice(self.direction)
            levelOfDetail -= 1
        adjList = []
        if sizeAdj:
            adjList.append(sizeAdj)
        if dirAdj:
            adjList.append(dirAdj)
        retStr = " ".join(adjList)
        if len(adjList) > 0 and len(retStr) > 0:
            return retStr + " "
        else:
            return ""