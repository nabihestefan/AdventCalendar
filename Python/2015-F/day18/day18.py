## Parsing
files = ['input.txt', 'testInput.txt']
with open(files[0], 'r') as f:
    lines =  [a.strip() for a in f.readlines()]

grid = [["." for x in range(len(lines)+2)]]
empty_grid = [["z" for x in range(len(lines)+2)] for y in range(len(lines)+2)]

for i in lines:
    line = ["."]
    for c in i:
        if c == "#":
            line.append("#")
        else:
            line.append(".")
    line.append(".")
    grid.append(line)

grid.append(["." for x in range(len(lines)+2)])

# Part 2
grid[1][1] = "#"
grid[1][len(grid)-2] = "#"
grid[len(grid)-2][1] = "#"
grid[len(grid)-2][len(grid)-2] = "#"

def state(x,y, set_grid):
    around = 0
    for i in [x-1,x,x+1]:
        for j in [y-1,y,y+1]:
            if set_grid[i][j] == "#":
                around += 1

    if set_grid[x][y] == "#":
        if around == 3 or around == 4:
            return "#"
        else:
            return "."
    else:
        if around == 3:
            return "#"
        else:
            return "."


steps = 100

for i in range(steps):
    next_grid = [["z" for x in range(len(lines)+2)] for y in range(len(lines)+2)]
    for x in range(1, len(grid)-1):
        for y in range(1, len(grid[x])-1):
            next_grid[x][y] = state(x,y, grid)

    # Part 2
    next_grid[1][1] = "#"
    next_grid[1][len(grid)-2] = "#"
    next_grid[len(grid)-2][1] = "#"
    next_grid[len(grid)-2][len(grid)-2] = "#"

    grid = next_grid

on = 0
for i in grid:
    for j in i:
        if j == "#":
            on += 1
print(on)
