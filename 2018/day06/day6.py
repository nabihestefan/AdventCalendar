files = ['input.txt', 'inputTest.txt']
## Parsing
def parseCoord(line):
    x = int(line[:line.index(",")])
    y = int(line[line.index(",")+1:])
    return x,y

with open(files[0], 'r') as f:
    coords = [parseCoord(a) for a in f.readlines()]

minX = minY = float('inf')
maxX = maxY = -1

areas = {}
for x,y in coords:
    areas[(x,y)] = 0
    minX = min(x, minX)
    maxX = max(x, maxX)
    minY = min(y, minY)
    maxY = max(y, maxY)

def findClosest(x,y,coords):
    dists = {}
    for cx, cy in coords:
        dist = abs(cx-x) + abs(cy-y)
        l = dists.get(dist, [])
        l.append((cx,cy))
        dists[dist] = l
    m = dists[min(dists.keys())]
    if len(m) == 1:
        return m[0]
    else:
        return None


for x in range(minX, maxX+1):
    for y in range(minY, maxY+1):
        closest = findClosest(x,y,coords)
        if closest != None: areas[closest]+=1

infinite = set()
for x in range(minX, maxX+1):
    for y in range(minY, maxY+1):
        if x in [minX, maxX] or y in [minY, maxY]:
            areas[findClosest(x,y,coords)] = -1

region = 0
dist = 10000
for x in range(minX, maxX+1):
    for y in range(minY, maxY+1):
        totalD = 0
        for px,py in coords: totalD += abs(px-x) + abs(py-y)
        if totalD < dist: region += 1


print("Part 1: ", max(areas.values()))
print("Part 2: ", region)
