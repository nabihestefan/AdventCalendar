import networkx as nx
import sys
sys.setrecursionlimit(10000)
## Parsing
files = ['input.txt', 'testInput.txt']

with open(files[0], 'r') as f:
    lines =  [a.strip() for a in f.readlines()]

w,h = len(lines[0]), len(lines)

def getNbs(x,y):
    for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
        newX,newY  = x+dx, y+dy
        if 0<=newX<=w and 0<=newY<=h:
            yield (newX,newY)

def makeGraph(lines):
    wires = []
    g = nx.Graph()
    for y in range(h):
        for x in range(w):
            if lines[y][x] == "." or lines[y][x].isdigit():
                for newX,newY in getNbs(x,y):
                    if lines[newY][newX] == "." or lines[newY][newX].isdigit():
                        g.add_edge((x,y),(newX,newY))
                if lines[y][x].isdigit():
                    if lines[y][x] == "0": start = (x,y)
                    else: wires.append((x,y))

    return g, wires, start

def permutations(wires):
    if len(wires) == 0: return[]
    if len(wires) == 1: return [wires]
    l = []
    for i,m in enumerate(wires):
        rem = wires[:i]+wires[i+1:]
        for p in permutations(rem):
            l.append([m]+p)
    return l

def run(g,wirePerms,start,partTwo):
    minLength = float('inf')
    for wirePerm in wirePerms:
        wirePerm = [start] + wirePerm
        wirePerm += [start] if partTwo else []
        length = 0
        for i in range(len(wirePerm)-1):
            length += nx.shortest_path_length(g,wirePerm[i], wirePerm[i+1])
        minLength = min(minLength, length)
    return minLength


g, wires, start = makeGraph(lines)
wirePerms = permutations(wires)

print("Part 1: ", run(g,wirePerms,start,False))
print("Part 2: ", run(g,wirePerms,start,True))
