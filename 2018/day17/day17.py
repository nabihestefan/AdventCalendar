import sys
sys.setrecursionlimit(5000)
files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f: lines =  [a.strip() for a in f.readlines()]

clay = set()
for i in lines:
    a,b = i.split(",")
    f = int(a.split('=')[1])
    s1, s2 = map(int, b.split('=')[1].split('..'))
    for s in range(s1,s2+1):
        if a[0] == "x": clay.add((f,s))
        else: clay.add((s,f))

ys = [i[1] for i in clay]
minY, maxY = min(ys), max(ys)

inRange = lambda x: 0<=x[1] and x[1]<=maxY



settled = set()
flowing = set()

def run(p, dir=(0,1)):
    flowing.add(p)
    below = (p[0], p[1]+1)

    if below not in clay and below not in flowing and inRange(below):
        run(below)

    if below not in clay and below not in settled:
        return False

    l = (p[0]-1, p[1])
    r = (p[0]+1, p[1])

    leftF = l in clay or l not in flowing and run(l, (-1,0))
    rightF = r in clay or r not in flowing and run(r, (1,0))

    if dir == (0,1) and leftF and rightF:
        settled.add(p)

        while l in flowing:
            settled.add(l)
            l = (l[0]-1, l[1])

        while r in flowing:
            settled.add(r)
            r = (r[0]+1, r[1])

    return (dir == (-1,0) and (leftF or l in clay)) or (dir == (1,0) and (rightF or r in clay))

run((500,0))
print("Part 1: ", len([p for p in flowing|settled if minY<=p[1]<=maxY]))
print("Part 2: ", len([p for p in settled if minY<=p[1]<=maxY]))
