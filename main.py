import Holds
import Moves
import random

holdtypes = ["crimp", "sloper", "jug", "pocket"]
connectivetypes = ["make a", "do a", "then make a", "then do a"]

lengthofclimb = 0
lengthofclimb = int(input("Enter a length (number of moves) of climb:"))
while lengthofclimb <= 0:
    print("Length input invalid")
    lengthofclimb = int(input("Try again:"))

levelofdetail = int(input("Enter the level of description desired (0-3):"))
while levelofdetail < 0 or levelofdetail > 3:
    print("Description level input invalid")
    levelofdetail = int(input("Try again:"))

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