import networkx as nx
files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f:
    grid =  [a for a in f.readlines()]

w, h = len(grid[0]), len(grid)
portals = {}
for y in range(0, h-1):
    for x in range(0, w-1):

        if not grid[y][x].isupper():
            continue
        dirs = []
        if grid[y+1][x].isupper():
            c = grid[y][x] + grid[y+1][x]
            if y > 0 and grid[y-1][x] == '.':     dirs.append((x, y-1))
            elif y < h-2 and grid[y+2][x] == '.': dirs.append((x, y+2))
            try:
                portals[c] += dirs
            except KeyError:
                portals[c] = dirs
        if grid[y][x+1].isupper():
            c = grid[y][x] + grid[y][x+1]
            if x > 0 and grid[y][x-1] == '.':     dirs.append((x-1, y))
            elif x < w-2 and grid[y][x+2] == '.': dirs.append((x+2, y))
            try:
                portals[c] += dirs
            except KeyError:
                portals[c] = dirs

def graphP1():
    g = nx.Graph()
    for key in portals.keys():
        if key not in ["AA","ZZ"]:
            p1,p2 = portals[key]
            g.add_edge(p1,p2)

    for y in range(1, h-1):
        for x in range(1, w-1):
            c = grid[y][x]
            if c == ".":
                for dx,dy in [(-1,0), (0,1), (1,0), (0,-1)]:
                    if grid[y+dy][x+dx]==".":
                        g.add_edge((x,y),(x+dx,y+dy))
    return g

def graphP2():
    maxLevels = 30 #max recursion depth
    g = nx.Graph()
    for y in range(1, h-1):
        for x in range(1, w-1):
            c = grid[y][x]
            if c == ".":
                for i in range(maxLevels):
                    for dx,dy in [(-1,0), (0,1), (1,0), (0,-1)]:
                        if grid[y+dy][x+dx]==".":
                            g.add_edge((x,y, i),(x+dx,y+dy, i))

    for key in portals.keys():
        if key not in ["AA","ZZ"]:
            p1,p2 = portals[key]
            if p1[0] in [2, w-4] or p1[1] in [2, h-3]:
                outer, inner = p1, p2
            else:
                inner, outer = p1,p2
            for i in range(maxLevels-1):
                g.add_edge((*inner, i), (*outer, i+1))
    return g


start = portals["AA"][0]
end = portals["ZZ"][0]

print("Part 1: ", nx.shortest_path_length(graphP1(),start,end))
print("Part 2: ", nx.shortest_path_length(graphP2(),(*start,0),(*end,0)))
