files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f: lines =  [a.strip() for a in f.readlines()]

def part1(on):
    global adj
    for cycle in range(6):
        new = set()
        xR = [a[0] for a in on]
        yR = [a[1] for a in on]
        zR = [a[2] for a in on]

        for x in range(min(xR)-1, max(xR)+2):
            for y in range(min(yR)-1, max(yR)+2):
                for z in range(min(zR)-1, max(zR)+2):
                    nbrs = 0
                    for i,j,k in adj:
                        if (x+i, y+j, z+k) in on:
                            nbrs += 1
                    if (x,y,z) in on and nbrs in [2,3]:
                        new.add((x,y,z))
                    if (x,y,z) not in on and nbrs == 3:
                        new.add((x,y,z))
        on = new

    return len(on)

def part2(on):
    global adj
    for cycle in range(6):
        new = set()
        xR = [a[0] for a in on]
        yR = [a[1] for a in on]
        zR = [a[2] for a in on]
        wR = [a[3] for a in on]

        for x in range(min(xR)-1, max(xR)+2):
            for y in range(min(yR)-1, max(yR)+2):
                for z in range(min(zR)-1, max(zR)+2):
                    for w in range(min(wR)-1, max(wR)+2):
                        nbrs = 0
                        for i,j,k,l in adj:
                            if (x+i, y+j, z+k, w+l) in on:
                                nbrs += 1
                        if (x,y,z,w) in on and nbrs in [2,3]:
                            new.add((x,y,z,w))
                        if (x,y,z,w) not in on and nbrs == 3:
                            new.add((x,y,z,w))
        on = new

    return len(on)


adj = set()
for i in [-1,0,1]:
    for j in [-1,0,1]:
        for k in [-1,0,1]:
            if (i,j,k) != (0,0,0): adj.add((i,j,k))

on = set()
for indi, i in enumerate(lines):
    for indj, j in enumerate(i):
        if j == "#": on.add((indi,indj,0))


print("Part 1: ", part1(on))

adj = set()
for i in [-1,0,1]:
    for j in [-1,0,1]:
        for k in [-1,0,1]:
            for l in [-1,0,1]:
                if (i,j,k,l) != (0,0,0,0): adj.add((i,j,k,l))
on = set()
for indi, i in enumerate(lines):
    for indj, j in enumerate(i):
        if j == "#": on.add((indi,indj,0,0))

print("Part 2: ", part2(on))
