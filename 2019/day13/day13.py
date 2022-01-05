import sys
sys.path.append("../")
from intCode import IntCode
files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f:
    ints =  [int(a) for a in f.readlines()[0].split(",")]

def p1(ints):
    blocks = 0
    comp = IntCode(ints)
    while not comp.end:
        x = comp.run()
        y = comp.run()
        id = comp.run()
        blocks += id==2
    return blocks

def p2(ints):
    bx,px=0,0
    comp = IntCode(ints, [], lambda:(bx>px)-(bx<px))
    comp.set(0,2)
    points = 0
    while not comp.end:
        x = comp.run()
        y = comp.run()
        id = comp.run()
        if not comp.end:
            px = x if id==3 else px
            bx = x if id==4 else bx
            points = id if (x,y) == (-1,0) else points
    return points

print("Part 1: ", p1(ints[:]))
print("Part 2: ", p2(ints[:]))
