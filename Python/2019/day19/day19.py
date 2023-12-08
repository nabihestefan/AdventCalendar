import sys
sys.path.append("../")
from intCode import IntCode
files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f:
    ints = [int(a) for a in f.readlines()[0].split(",")]

comp = IntCode(ints[:])

def checkPoint(y,x):
    comp.reset()
    comp.addInput(x)
    comp.addInput(y)
    return comp.run()

x = y = 0
while not checkPoint(x+99,y):
    y += 1
    while not checkPoint(x,y+99):
        x += 1

print("Part 1: ", sum(checkPoint(x,y) for x in range(50) for y in range(50)))
print("Part 2: ", x*10000 + y)
