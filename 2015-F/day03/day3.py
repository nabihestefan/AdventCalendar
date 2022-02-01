## Parsing
with open('day3.txt', 'r') as f:
    directions =  f.readlines()[0]

houses = []
l = 300
for i in range(l):
    line = []
    for j in range(l):
        line.append(0)
    houses.append(line)

x = [int(l/2), int(l/2)]
y = [int(l/2), int(l/2)]
turn = 0

for i in directions:
    houses[x[turn]][y[turn]] += 1
    if i == ">":
        y[turn] += 1
    elif i == "<":
        y[turn] -= 1
    elif i == "^":
        x[turn] -= 1
    elif i == "v":
        x[turn] += 1
    turn += 1
    turn %= 2

houses[x[turn]][y[turn]] += 1

total = 0

for i in houses:
    for j in i:
        if j > 0:
            total += 1
print(total)
