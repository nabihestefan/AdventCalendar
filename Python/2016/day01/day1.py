from copy import deepcopy
## Parsing
files = ['input.txt', 'testInput.txt']
with open(files[0], 'r') as f:
    moves =  [(a[0], int(a[1:])) for a in f.readlines()[0].split(", ")]

def func(part2):
    dirs = [(1,0), (0,1), (-1,0), (0,-1)]
    dir = 0
    pos = [0,0]
    seen = [deepcopy(pos)]
    for i in moves:
        dir = (dir + 2*(i[0] == 'R') - 1) % 4
        for i in range(i[1]):
            pos[0] += dirs[dir][0]
            pos[1] += dirs[dir][1]
            if pos in seen and part2:
                return(abs(pos[0]) + abs(pos[1]))
            seen.append(deepcopy(pos))
    return(abs(pos[0]) + abs(pos[1]))

print("PART1", func(False))
print("PART2", func(True))
