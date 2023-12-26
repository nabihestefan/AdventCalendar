from copy import deepcopy
## Parsing
files = ['input.txt', 'testInput.txt']
with open(files[0], 'r') as f:
    line =  f.readlines()[0].strip()

def isSafe(x,y, grid):
    left = grid.get((x-1,y-1), True)
    center = grid[(x,y-1)]
    right = grid.get((x+1,y-1), True)
    if (left and center and not right) or (not left and center and right) or \
        (left and not center and not right) or (not left and not center and right):
        return False
    return True

grid = dict()
y = 0
for x,c in enumerate(line): grid[(x,y)] = (c == ".")
cols = len(line)
rows = 40

def display():
    for y in range(rows):
        line = ""
        for x in range(cols):
            if grid[(x,y)]:
                line+="."
            else:
                line+="^"
        print(line)
def run(rows, grid):
    for y in range(1,rows):
        for x in range(cols):
            grid[(x,y)] = isSafe(x,y, grid)
    return sum(grid.values())


print("Part 1: ", run(40,deepcopy(grid)))
print("Part 2: ", run(400000,deepcopy(grid)))
