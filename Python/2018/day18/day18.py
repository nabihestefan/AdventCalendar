files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f: lines =  [a.strip() for a in f.readlines()]

open = set()
trees = set()
lumber = set()
s = len(lines)
for y,row in enumerate(lines):
    for x, c in enumerate(row):
        if c == ".": open.add((x,y))
        if c == "|": trees.add((x,y))
        if c == "#": lumber.add((x,y))

def countNbs(x,y, open, trees, lumber):
    nbs = []
    o=t=l=0
    for dx,dy in [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]:
        nx, ny = x+dx, y+dy
        if 0<=nx<s and 0<=ny<s:
            if (nx,ny) in open: o+=1
            elif (nx,ny) in trees: t+=1
            elif (nx,ny) in lumber: l+=1
    return o,t,l


def update(open, trees, lumber):
    nOpen = set()
    nTrees = set()
    nLumber = set()
    for x in range(s):
        for y in range(s):
            o,t,l = countNbs(x,y, open, trees, lumber)
            if (x,y) in open:
                if t >= 3: nTrees.add((x,y))
                else: nOpen.add((x,y))
            if (x,y) in trees:
                if l >= 3: nLumber.add((x,y))
                else: nTrees.add((x,y))
            if (x,y) in lumber:
                if l >= 1 and t >= 1:
                    nLumber.add((x,y))
                else: nOpen.add((x,y))

    return nOpen, nTrees, nLumber

hist = {}
for step in range(1000000000):
    open, trees, lumber = update(open, trees, lumber)

    if step == 9:
        print("Part 1: ", len(trees)*len(lumber))

    state = (tuple(open),tuple(trees),tuple(lumber))

    if state in hist:
        left = 1000000000 - hist[state] - 1
        for step in range(left%(step-hist[state])):
            open, trees, lumber = update(open, trees, lumber)
        break

    hist[state] = step

print("Part 2: ", len(trees)*len(lumber))
