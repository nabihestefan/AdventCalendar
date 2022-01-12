from copy import deepcopy
## Parsing
files = ['input.txt', 'testInput.txt']
with open(files[0], 'r') as f:
    desNum = int(f.readlines()[0].strip())


def isOpen(x,y):
    return bin((x*x + 3*x + 2*x*y + y + y*y) + desNum)[2:].count("1") % 2 == 0

def getNbs(pos):
    inRange = lambda x,y: 0<=x and 0<=y
    next = []
    for x,y in pos:
        for dx,dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx, ny = x+dx, y+dy
            if inRange(nx,ny) and isOpen(nx,ny) and (nx,ny) not in seen:
                seen.add((nx,ny))
                next.append((nx,ny))
    return next

cur = [(1,1)]
goal =  (31,39)
seen = {(1,1)}
steps = 0
while goal not in cur:
    steps += 1
    cur = getNbs(cur)
    if steps == 50:
        p2 = deepcopy(seen)

print("Part 1: ", steps)
print("Part 2: ", len(p2))
