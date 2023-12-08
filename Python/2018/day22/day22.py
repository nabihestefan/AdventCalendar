files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f: lines =  [a.strip() for a in f.readlines()]

depth = int(lines[0][lines[0].index(":")+1:])
target = int(lines[1][lines[1].index(":")+1:lines[1].index(",")]), int(lines[1][lines[1].index(",")+1:])


rocky, wet, narrow = 0,1,2
torch, gear, neither = 0,1,2
validItems = {rocky: (torch, gear), wet: (gear, neither), narrow: (torch, neither)}


class Point:
    def __init__(self,geo,erosion,risk):
        self.erosion = erosion
        self.geo = geo
        self.risk = risk

def makeGrid(depth, corner):
    grid = {}
    for y in range(corner[1]+1):
        for x in range(corner[0]+1):
            if (x,y) in [(0,0), target]: geo = 0
            elif x == 0: geo = y*48271
            elif y == 0: geo = x*16807
            else: geo = grid[(x-1,y)].erosion*grid[(x,y-1)].erosion

            erosion = (geo+depth)%20183
            risk = erosion%3
            grid[(x,y)] = Point(geo,erosion, risk)

    return grid

def shortestPath(grid, corner, target):
    import networkx
    g = networkx.Graph()
    for y in range(corner[1]+1):
        for x in range(corner[0]+1):
            items = validItems[grid[(x,y)].risk]
            g.add_edge((x,y,items[0]), (x,y,items[1]), weight = 7)
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx,ny = x+dx,y+dy
                if 0<=nx<=corner[0] and 0<=ny<=corner[1]:
                    newItems = validItems[grid[(nx,ny)].risk]
                    for item in set(items)&set(newItems):
                        g.add_edge((x,y,item), (nx,ny,item), weight=1)
    return networkx.dijkstra_path_length(g, (0,0,torch), (target[0], target[1], torch))


grid = makeGrid(depth, target)
print("Part 1: ", sum(p.risk for p in grid.values()))
corner = (target[0]+50, target[1]+50)
print("Part 2: ", shortestPath(makeGrid(depth,corner), corner, target))
