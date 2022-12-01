from copy import deepcopy
files = ['input.txt', 'inputTest.txt']
## Parsing
cucumbers = []
for line in open(files[0]):
    cucumbers.append(list(line.strip()))

steps = 0

def moveEast(cucumbers):
    old_cucumbers = deepcopy(cucumbers)
    moves = 0
    for indi, i in enumerate(cucumbers):
        for indj, j in enumerate(i):
            if old_cucumbers[indi][indj] == ">" and old_cucumbers[indi][(indj+1)%len(i)] == ".":
                cucumbers[indi][indj] = "."
                cucumbers[indi][(indj+1)%len(i)] = ">"
                moves += 1

    return cucumbers, moves

def moveSouth(cucumbers):
    old_cucumbers = deepcopy(cucumbers)
    moves = 0
    for i in reversed(range(len(cucumbers))):
        for j in range(len(cucumbers[i])):
            if old_cucumbers[i][j] == "v" and old_cucumbers[(i+1)%len(cucumbers)][j] == ".":
                cucumbers[i][j] = "."
                cucumbers[(i+1)%len(cucumbers)][j] = "v"
                moves += 1
    return cucumbers, moves

steps = 0
while True:
    steps += 1
    movesE, movesS = 0,0
    cucumbers, movesE = moveEast(cucumbers)
    cucumbers, movesS = moveSouth(cucumbers)
    if movesS + movesE == 0:
        print("Part 1: ", steps)
        break
