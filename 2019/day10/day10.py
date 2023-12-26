from math import atan2, pi
files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f:
    lines =  [a.strip() for a in f.readlines()]

asteroids = []
for indi, i in enumerate(lines):
    for indj, j in enumerate(i):
        if j == "#": asteroids.append((indj, indi))

def angle(start, end):
        result = atan2(end[0] - start[0], start[1] - end[1]) * 180 / pi
        if result < 0:
            return 360 + result
        return result

mX = 0
for i in asteroids:
    line = set()
    all = []
    for j in asteroids:
        if i != j:
            line.add(angle(i,j))
    if len(line)>mX:
        mX = len(line)
        best = i

gone = [best]
while len(gone) < 201:
    closest = {}
    for x,y in asteroids:
        if (x,y) not in gone:
            astAngle = angle(best, (x,y))
            closex,closey = closest.get(astAngle, (float('inf'), float('inf')))
            if abs(x - best[0]) + abs(y - best[1]) < abs(closex - best[0]) + abs(closey - best[1]):
                closest[astAngle] = (x,y)
    gone += sorted(closest.values(), key=lambda x: angle(best,x))


print("Part 1: ", mX)
print("Part 2: ", gone[200][0]*100 + gone[200][1])
