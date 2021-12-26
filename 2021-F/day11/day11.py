from copy import deepcopy
files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f:
    lines =  [a.strip() for a in f.readlines()]
    octopuses = [[int(j) for j in i] for i in lines]
    flashed_blank = [[False for j in i] for i in lines]

def flash(x, y):
    flashes = 0
    octopuses[x][y] = 0
    flashed[x][y] = True

    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i != 0 or j != 0:
                if (-1 < x+i and x+i < len(octopuses)) and (-1 < y+j and y+j < len(octopuses)):
                    if not flashed[x+i][y+j]:
                        octopuses[x+i][y+j] += 1
                        if octopuses[x+i][y+j] > 9:
                            flashes += 1
                            flashes += flash(x+i, y+j)

    return flashes


flashes = 0
steps = 10000
for step in range(steps):
    flashed = deepcopy(flashed_blank)
    for i, oct_line in enumerate(octopuses):
        for j, oct in enumerate(oct_line): octopuses[i][j] += 1

    for i, oct_line in enumerate(octopuses):
        for j, oct in enumerate(oct_line):
            if octopuses[i][j] > 9:
                flashes += 1
                flashes += flash(i, j)
    #Part 1
    if step == 100:
        print("Part1")
        print(flashes)

    #Part 2
    all = True
    for i in flashed:
        for j in i: all = (all and j)

    if all:
        print("PART 2")
        print(step)
        exit(0)
