files = ['day9.txt', 'day9Test.txt']
## Parsing
with open(files[0], 'r') as f:
    lines =  f.readlines()
    positions = [x.split('')for x in f.readlines()]

positions = []
extra = []

for i in range(len(lines[0])+1):
    extra.append(9)
positions.append(extra)

for i in lines:
    line = [9]
    for j in range(len(i)-1):
        line.append(int(i[j]))
    line.append(9)
    positions.append(line)

positions.append(extra)

## Parts 1&2
lowpoints = []

for i in range(1,len(positions)-1):
    for j in range(1,len(positions[i])-1):
        if (positions[i][j] < positions[i+1][j]) and (positions[i][j] < positions[i][j+1]) and (positions[i][j] < positions[i-1][j]) and (positions[i][j] < positions[i][j-1]):
            lowpoints.append((i,j))
##Part 1
# sum = 0
# for i in lowpoints:
#     sum += (positions[i[0]][i[1]] + 1)
# print(sum)

basins = []

def basins_size(i, j, positions, checked):
    checked[i][j] = True

    if (positions[i-1][j] != 9) and not(checked[i-1][j]):
        basins_size(i-1, j, positions, checked)
    if (positions[i][j-1] != 9) and not(checked[i][j-1]):
        basins_size(i, j-1, positions, checked)
    if (positions[i+1][j] != 9) and not(checked[i+1][j]):
        basins_size(i+1, j, positions, checked)
    if (positions[i][j+1] != 9) and not(checked[i][j+1]):
        basins_size(i, j+1, positions, checked)


for i in lowpoints:
    ## Clear checked
    checked = []
    for j in positions:
        line = []
        for k in j:
            line.append(False)
        checked.append(line)

    basins_size(i[0], i[1], positions, checked)
    size = 0
    for line in checked:
        for item in line:
            if item:
                size += 1
    basins.append(size)

## Extract max 3
max1 = max(basins)
basins.remove(max1)
max2 = max(basins)
basins.remove(max2)
max3 = max(basins)
basins.remove(max3)

print(max1*max2*max3)
