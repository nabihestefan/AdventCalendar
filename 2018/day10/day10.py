files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f:
    lines =  [a.strip() for a in f.readlines()]

points = []
velocities = []
for line in lines:
    py = int(line[line.index("<")+1:line.index(",")])
    px = int(line[line.index(",")+1:line.index(">")])
    line = line[line.index("velocity"):]
    vy = int(line[line.index("<")+1:line.index(",")])
    vx = int(line[line.index(",")+1:line.index(">")])
    points.append((px,py))
    velocities.append((vx,vy))

def update(points, vels):
    npoints = []
    for ind, i in enumerate(points):
        npoints.append((i[0]+vels[ind][0], i[1] + vels[ind][1]))
    return npoints

def display(points):
    x = [i[0] for i in points]
    y = [i[1] for i in points]
    minX, maxX, minY, maxY = min(x), max(x), min(y), max(y)
    for x in range(minX, maxX+1):
        line = []
        for y in range(minY, maxY+1):
            if (x,y) in points: line.append("#")
            else: line.append(".")
        print("".join(line))

def finished(points, velocities):
    for indi, i in enumerate(velocities):
        for indj, j in enumerate(velocities):
            if i == (-1*j[0], -1*j[1]): break

    def dist(p1, p2): return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

    ps = [points[indi], points[indj]]
    vs =[i,j]
    t = 0
    d = dist(ps[0], ps[1])
    while True:
        ps = update(ps[:], vs)
        nd = dist(ps[0], ps[1])
        if nd > d: return t
        else:
            d = nd
            t += 1

totalT = finished(points, velocities)
for _ in range(totalT):
    points = update(points[:], velocities)

print("Part 1: ")
display(points)
print("Part 2: ", totalT)
