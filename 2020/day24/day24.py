files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f:
    lines =  [a.strip() for a in f.readlines()]

dirs  = [(1,0),(-1,0),(1,-1),(0,-1),(0,1),(-1,1)]
moves = ['e',  'w',   'ne',  'nw',  'se', 'sw'  ]

def getN(pos):
    result = []
    for d in dirs:
        nPos = (pos[0] + d[0], pos[1] + d[1])
        result.append(nPos)
    return result

def countN(tile, flipped):
    total = 0
    for nPos in getN(pos):
        if nPos in flipped:
            total += 1
    return total

flipped = set()
for line in lines:
    x,y = 0,0
    while line:
        if line[0] in moves:
            x += dirs[moves.index(line[0])][0]
            y += dirs[moves.index(line[0])][1]
            line = line[1:]
        if line[0:2] in moves:
            x += dirs[moves.index(line[0:2])][0]
            y += dirs[moves.index(line[0:2])][1]
            line = line[2:]
    pos = (x, y)
    if pos not in flipped:
        flipped.add(pos)
    else:
        flipped.remove(pos)

print("Part 1: ", len(flipped))

for _ in range(100):
    stack = set()
    visited = set()
    newFlipped = flipped.copy()

    for tile in flipped:
        stack.add(tile)
        stack.update(getN(tile))

    while len(stack) > 0:
        pos = stack.pop()
        if pos in visited:
            continue
        visited.add(pos)
        nCount = countN(pos, flipped)
        if pos in flipped and nCount not in [1,2]:
            newFlipped.remove(pos)
        elif pos not in flipped and nCount == 2:
            newFlipped.add(pos)
    flipped = newFlipped.copy()


print("Part 2: ", len(flipped))
