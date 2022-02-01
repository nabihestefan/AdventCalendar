## Parsing
files = ['input.txt', 'testInput.txt']
with open(files[0], 'r') as f:
    lines =  [a.strip() for a in f.readlines()]

row = 6 #3
col = 50 #7
screen = [[False for i in range(col)] for j in range(row)]

for line in lines:
    line = line.split()
    if len(line) == 2:
        x,y = int(line[1][:line[1].index('x')]), int(line[1][line[1].index('x')+1:])
        for i in range(y):
            for j in range(x):
                screen[i][j] = True
    elif line[1] == 'row':
        x,y = int(line[2][2:]), int(line[-1])
        screen[x] = screen[x][-y:] + screen[x][:-y]
    else:
        x,y = int(line[2][2:]), int(line[-1])
        g = [screen[i][x] for i in range(row)]
        g = g[-y:] + g[:-y]
        for i in range(row):
            screen[i][x] = g[i]

count = 0
for row in screen:
    count += row.count(True)
print("PART1")
print(count)

print("PART2")
for row in screen:
    print (''.join('#' if g else ' ' for g in row))
