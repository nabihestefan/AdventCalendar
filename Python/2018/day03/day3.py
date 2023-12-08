files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f:
    lines =  [a.strip() for a in f.readlines()]

squares = []
for line in lines:
    left = int(line[line.index("@")+1:line.index(",")])
    top = int(line[line.index(",")+1:line.index(":")])
    width = int(line[line.index(":")+1:line.index("x")])
    height = int(line[line.index("x")+1:])
    square = set()
    for x in range(left,left+width):
        for y in range(top, top+height):
            square.add((x,y))
    squares.append(square)

overlapped = set()
for ind, s1 in enumerate(squares):
    singleO = 0
    for s2 in squares:
        if s1==s2: continue
        for point in s1&s2:
            overlapped.add(point)
            singleO += 1
    if singleO == 0:
        id = ind+1

print("Part 1: ", len(overlapped))
print("Part 2: ", id)
