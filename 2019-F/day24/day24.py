files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f:
    lines =  [a.strip() for a in f.readlines()]

def visualize(bugs):
    for y in range(5):
        line = []
        for x in range(5):
            if (y,x) in bugs: line.append("#")
            else: line.append(".")
        print("".join(line))


def part1(lines):
    bugs = set()
    for y, row in enumerate(lines):
        for x, c in enumerate(row):
            if c == "#": bugs.add((y,x))
    layouts = [bugs]

    def updateBugs(bugs):
        newBugs = set()
        for y in range(5):
            for x in range(5):
                nbs = 0
                for dx, dy in [(-1,0), (0,1), (1,0), (0,-1)]:
                    if (y+dy, x+dx) in bugs: nbs += 1
                if (y, x) in bugs and nbs == 1: newBugs.add((y,x))
                elif (y, x) not in bugs and (nbs == 1 or nbs == 2):
                    newBugs.add((y,x))
        return newBugs

    while True:
        bugs = updateBugs(bugs)
        if bugs in layouts: break
        else: layouts.append(bugs)

    rating = 0
    for y,x in bugs:
        p = (y*5 + x)
        rating += 2**p
    return rating

def countRow(bugs, n):
    c = 0
    for y,_ in bugs:
        if y == n: c+=1
    return c

def countCol(bugs, n):
    c = 0
    for _,x in bugs:
        if x == n: c+=1
    return c

def countBugsDeeper(levels, level, x, y):
    grid = levels.get(level-1, set())
    if x == 1: return countCol(grid, 0)
    elif x == 3:return countCol(grid, 4)
    elif y == 1: return countRow(grid, 0)
    elif y == 3: return countRow(grid, 4)

def countBugsOuter(levels, level, x, y, nx, ny):
    grid = levels.get(level+1, set())
    if nx == -1:
        if (2,1) in grid: return 1
    if nx == 5:
        if (2,3) in grid: return 1
    if ny == -1:
        if (1,2) in grid: return 1
    if ny == 5:
        if (3,2) in grid: return 1
    return 0


def hasLife(levels, level, x, y):
    nbs = 0
    grid = levels[level]
    for dx, dy in [(-1,0), (0,1), (1,0), (0,-1)]:
        nx, ny = x+dx, y+dy
        if (nx,ny) == (2,2):
            nbs += countBugsDeeper(levels, level, x,y)
        elif nx in [-1,5] or ny in [-1,5]:
            nbs += countBugsOuter(levels, level, x,y, nx,ny)
        else:
            nbs += (y+dy, x+dx) in grid
    if (y,x) in grid: return nbs == 1
    else: return nbs == 1 or nbs == 2


def simulate(levels):
    newLvls = {}
    for level, grid in levels.items():
        newGrid = set()
        for y in range(5):
            for x in range(5):
                if (x,y) == (2,2):
                    continue
                if hasLife(levels, level, x, y):
                    newGrid.add((y,x))
        newLvls[level] = newGrid
    return newLvls

def countBugs(levels):
    total = 0
    for level in levels.values(): total += len(level)
    return total

def part2(lines):
    bugs = set()
    for y, row in enumerate(lines):
        for x, c in enumerate(row):
            if c == "#": bugs.add((y,x))

    levels = {0:bugs}
    mins = 200
    for m in range(1, (mins//2)+2):
        levels[m] = set()
        levels[-m] = set()

    for _ in range(mins):
        levels = simulate(levels)
    return countBugs(levels)


print("Part 1: ", part1(lines))
print("Part 2: ", part2(lines))
