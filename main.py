import Holds
import Moves
import random

holdtypes = ["crimp", "sloper", "jug", "pocket"]
connectivetypes = ["make a", "do a", "then make a", "then do a"]

levelofdetail = random.randint(0, 3)
lengthofclimb = random.randint(1, 5)

def getRandomHold(lod: int):
    holdt = random.choice(holdtypes)
    if holdt == "crimp":
        return Holds.Crimp(lod)
    if holdt == "sloper":
        return Holds.Sloper(lod)
    if holdt == "pocket":
        return Holds.Pocket(lod)
    if holdt == "jug":
        return Holds.Jug(lod)

# Start holds
numstarthold = random.randint(1,2)
print("Start on a ", end="")
if numstarthold == 2:
    hold1 = getRandomHold(levelofdetail)
    hold2 = getRandomHold(levelofdetail)
    print(hold1.text + " and a " + hold2.text)
else:
    hold1 = getRandomHold(levelofdetail)
    print(hold1.text)

for m in range(lengthofclimb):
    move = Moves.Move(levelofdetail)
    hold = getRandomHold(levelofdetail)

    print(random.choice(connectivetypes) + " " + move.text + " to a " + hold.text)

# print("Start on two crimps/a crimp sidepull and a jug, make a jump/reach/stretch/micro-move to a [hold], ")