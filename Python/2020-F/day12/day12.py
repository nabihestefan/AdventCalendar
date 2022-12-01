from math import cos, sin, radians, ceil
files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f:
    instructions =  [(a[0], int(a[1:-1])) for a in f.readlines()]

pos = [0,0]
wpnt = [1,10]
heading = 0
for i in instructions:
    if i[0] == "N":
        pos[0] += i[1]
    if i[0] == "S":
        pos[0] -= i[1]
    if i[0] == "E":
        pos[1] += i[1]
    if i[0] == "W":
        pos[1] -= i[1]
    if i[0] == "L":
        heading += i[1]
    if i[0] == "R":
        heading -= i[1]
    if i[0] == "F":
        pos[1] += cos(radians(heading))*i[1]
        pos[0] += sin(radians(heading))*i[1]

print("Part 1: ", int(ceil(abs(pos[0])+abs(pos[1]))))

pos = [0,0]
wpnt = [1,10]
for i in instructions:
    if i[0] == "N":
        wpnt[0] += i[1]
    if i[0] == "S":
        wpnt[0] -= i[1]
    if i[0] == "E":
        wpnt[1] += i[1]
    if i[0] == "W":
        wpnt[1] -= i[1]
    if i[0] == "L":
        if i[1] == 90:
            wpnt[0], wpnt[1] = wpnt[1], -1*wpnt[0]
        elif i[1] == 180:
            wpnt[0] *= -1
            wpnt[1] *= -1
        elif i[1] == 270:
            wpnt[0], wpnt[1] = -1*wpnt[1], wpnt[0]
    if i[0] == "R":
        if i[1] == 90:
            wpnt[0], wpnt[1] = -1*wpnt[1], wpnt[0]
        elif i[1] == 180:
            wpnt[0] *= -1
            wpnt[1] *= -1
        elif i[1] == 270:
            wpnt[0], wpnt[1] = wpnt[1], -1*wpnt[0]

    if i[0] == "F":
        pos[1] += (wpnt[1])*i[1]
        pos[0] += (wpnt[0])*i[1]

print("Part 2: ", int(ceil(abs(pos[0])+abs(pos[1]))))
