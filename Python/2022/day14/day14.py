files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    data = [x.split("->") for x in f.read().split("\n")]

rocks = set()
for structure in data:
    structure = [list(map(int, pair.split(","))) for pair in structure]
    start = structure[0]
    rocks.add(tuple(start))
    for next in structure[1:]:
        if start[0] == next[0]:
            for i in range(min(start[1], next[1]), max(start[1], next[1])+1):
                rocks.add((start[0], i))
        elif start[1] == next[1]:
            for i in range(min(start[0], next[0]), max(start[0], next[0])+1):
                rocks.add((i, start[1]))
        start = next

floor = max(rocks, key = lambda x: x[1])[1]+2
for i in range(500-floor-1000, 500+floor+1000):
    rocks.add((i, floor))
p1Done = False
for s in range(1000000000):
    sand = (500,0)
    while True:
        if sand[1]+1 >= floor and (not p1Done):
            p1Done = True
            print("Part 1: ", s)
        
        if (sand[0], sand[1]+1) not in rocks:
            sand = (sand[0], sand[1]+1)
        elif (sand[0]-1, sand[1]+1) not in rocks:
            sand = (sand[0]-1, sand[1]+1)
        elif (sand[0]+1, sand[1]+1) not in rocks:
            sand = (sand[0]+1, sand[1]+1)
        else:
            break
    if sand == (500,0):
        print("Part 2: ", s+1)
        break
    rocks.add(sand)
