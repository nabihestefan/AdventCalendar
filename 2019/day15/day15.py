import sys
sys.path.append("../")
from intCode import IntCode
import networkx as nx
files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f:
    ints = [int(a) for a in f.readlines()[0].split(",")]

N,S,W,E = range(1,5)
ERR,OK,GOAL = range(3)
UNK,WLL,EMP,OX = range(4)
dirs = [(0,0),(0,-1),(0,1),(-1,0),(1,0)]
rev = {1:2, 2:1, 3:4, 4:3}
grid = {}

def addDir(p,d):
    return p[0]+dirs[d][0], p[1]+dirs[d][1]

pos = target = (0,0)
grid[pos] = EMP
comp = IntCode(ints)

def adventure(prevDir=0):
    global pos, target
    newpos = [addDir(pos,d) for d in range(1,5)]
    visited = [grid.get((x,y),0) != UNK for x,y in newpos]
    for d in range(1,5):
        if not visited[d-1]:
            comp.addInput(d)
            out = comp.run()
            grid[newpos[d-1]] = out+1
            if out != ERR:
                if out == GOAL:
                    target = newpos[d-1]
                pos = addDir(pos,d)
                adventure(d)
    if pos != (0,0):
        comp.addInput(rev[prevDir])
        comp.run()
        pos = addDir(pos, rev[prevDir])

def display():
    xs, ys = zip(*[(x,y) for x,y in grid.keys()])
    minx, maxx, miny, maxy = min(xs), max(xs), min(ys), max(ys)
    for y in range(miny, maxy-1):
        line = ""
        for x in range(minx, maxx-1):
            char = grid.get((x,y),0)
            if (x,y) == (0,0): line += "X"
            if (x,y) == pos: line += "D"
            if char == UNK: line += " "
            if char == EMP: line += "."
            if char == WLL: line += "#"
            if char == OX: line += "O"
        print(line)

def spread(start,t=0,maxT=0):
    nbs = [addDir(start,d) for d in range(1,5)]
    for nb in nbs:
        if grid.get(nb,0) == EMP:
            grid[nb] = OX
            maxT = spread(nb,t+1,maxT)
    return max(t,maxT)

adventure()
g = nx.Graph()
for key in grid:
    c = grid[key]
    if c in [EMP, OX]:
        g.add_node(key)
        nbs = [addDir(key,d) for d in range(1,5)]
        for nb in nbs:
            if grid.get(nb,0) in [EMP,OX]:
                g.add_edge(key,nb)


print("Part 1: ", nx.shortest_path_length(g,source=(0,0),target=target))
print("Part 2: ", spread(target))
