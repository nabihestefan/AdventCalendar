from collections import Counter
files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f:
    lines =  [a.strip() for a in f.readlines()]
    points = [[int(a[0:a.index(",")]), int(a[a.index(",")+1:])] for a in lines[0:lines.index("")]]
    folds = [(a[a.index("=")-1: a.index("=")], int(a[a.index("=")+1:])) for a in lines[lines.index("")+1:]]

for i in folds:
    remove, add = [], []
    if i[0] == "x":
        for j in points:
            if j[0] > i[1]: j[0] = j[0]-2*(j[0]-i[1])

    elif i[0] == "y":
        for j in points:
            if j[1] > i[1]: j[1] = j[1]-2*(j[1]-i[1])


print("PART1")
print(len(Counter([(point[0], point[1]) for point in points])))
board = []
for i in range(6):
    line = []
    for j in range(39):
        line.append(".")
    board.append(line)

for i in points:
    board[i[1]][i[0]] = "#"

print("PART2")
for i in board:
    str = ""
    print(str.join(i))
