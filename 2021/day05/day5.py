## Parsing
with open('day5.txt') as f:
    lines = f.readlines()

arrows = []
for i in lines:
    ind = i.index("->")
    one = i[0:ind-1]
    two = i[ind+3:]
    arrows.append(((int(one[0:one.index(",")]), int(one[one.index(",")+1:])), (int(two[0:two.index(",")]), int(two[two.index(",")+1:-1]))))


##Part 1
def run(arrows, part2):
    arr = []
    for x in range(0,1000):
        row = []
        for x in range(0,1000):
            row.append(0)
        arr.append(row)

    for i in arrows:
        if i[0][0] == i[1][0]:
            col = i[0][0]
            if i[0][1] < i[1][1]:
                for j in list(range(i[0][1], i[1][1]+1)):
                    arr[j][col] += 1
            else:
                for j in list(range(i[1][1], i[0][1]+1)):
                    arr[j][col] += 1
        elif i[0][1] == i[1][1]:
            row = i[0][1]
            if i[0][0] < i[1][0]:
                for j in list(range(i[0][0], i[1][0]+1)):
                    arr[row][j] += 1
            else:
                for j in list(range(i[1][0], i[0][0]+1)):
                    arr[row][j] += 1
        elif part2:
            if i[0][0] < i[1][0]:
                cols = list(range(i[0][0], i[1][0]+1))
                if i[0][1] < i[1][1]:
                    rows = list(range(i[0][1], i[1][1]+1))
                else:
                    rows = list(range(i[1][1], i[0][1]+1))
                    rows.reverse()
            else:
                cols = list(range(i[1][0], i[0][0]+1))
                cols.reverse()
                if i[0][1] < i[1][1]:
                    rows = list(range(i[0][1], i[1][1]+1))
                else:
                    rows = list(range(i[1][1], i[0][1]+1))
                    rows.reverse()

            for i in list(range(0,len(cols))):
                arr[rows[i]][cols[i]] += 1

    overlap = 0
    for i in arr:
        for j in i:
            if j > 1: overlap += 1

    return overlap

print("Part 1: ", run(arrows, False))
print("Part 1: ", run(arrows, True))
