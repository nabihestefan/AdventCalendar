files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f:
    points =  [map(int, a.split(",")) for a in f.readlines()]

overlaps = [set() for _ in range(len(points))]
for i,(w1,x1,y1,z1) in enumerate(points):
    for j,(w2,x2,y2,z2) in enumerate(points):
        d = abs(w1-w2)+abs(x1-x2)+abs(y1-y2)+abs(z1-z2)
        if d <= 3:
            overlaps[i].add(j)

overlapCounts = set()
consts = 0
for i in range(len(points)):
    if i in overlapCounts:
        continue
    consts += 1
    Q = []
    Q.append(i)
    while Q:
        x = Q.pop(0)
        if x in overlapCounts:
            continue
        overlapCounts.add(x)
        for y in overlaps[x]:
            Q.append(y)
print("Part 1:", consts)
