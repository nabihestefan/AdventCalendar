import sys
sys.path.append("../")
from intCode import *
files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f:
    ints = [int(a) for a in f.readlines()[0].split(",")]

def run(ints, start):
    x=y=curDir = 0
    dirs = [(0,-1), (1,0), (0,1), (-1,0)]
    comp = IntCode(ints)
    panels = {(x, y):start}
    while not comp.end:
        comp.addInput(panels.get((x,y), 0))
        out1 = comp.run()
        out2 = comp.run()
        if not comp.end:
            panels[(x,y)] = out1
            curDir = (curDir+1 if out2==1 else (curDir-1))%len(dirs)
            x,y = x+dirs[curDir][0], y+dirs[curDir][1]
    return panels

print("Part 1: ", len(run(ints[:], 0)))

img = [[" "]*40 for _ in range(6)]
for key in run(ints[:], 1):
    if panels[key] == 1: img[key[1]][key[0]] = "#"

print("Part 2: ")
print('\n'.join("".join(i) for i in img))
