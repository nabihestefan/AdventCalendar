with open('day3.txt') as f:
    lines = f.readlines()

oo = 0
to = 0
fo = 0
so = 0
ot = 0

i = 0
while i < len(lines):
    if lines[i][i*1%(len(lines[0])-1)] == "#":
        oo += 1
    if lines[i][i*3%(len(lines[0])-1)] == "#":
        to += 1
    if lines[i][i*5%(len(lines[0])-1)] == "#":
        fo += 1
    if lines[i][i*7%(len(lines[0])-1)] == "#":
        so += 1

    i += 1
i = 0
j = 0
while i < len(lines):
    if lines[i][j%(len(lines[0])-1)] == "#":
        ot += 1
    i += 2
    j += 1

print(oo*to*fo*so*ot)
