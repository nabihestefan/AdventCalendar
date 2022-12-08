files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    data = [list(map(int, list(x.strip()))) for x in f.readlines()]

def getScore(i,j):
    left = [data[i][x] for x in range(j+1)][::-1][1:]
    right = [data[i][x] for x in range(j, len(data[0]))][1:]
    above = [data[x][j] for x in range(i+1)][::-1][1:]
    below = [data[x][j] for x in range(i, len(data))][1:]

    views = [left, right, above, below]
    score = 1

    for view in views:
        curLen = 1
        for ind,t in enumerate(view[:-1]):
            if t >= data[i][j]:
                score *= ind+1
                break
            if ind+2 == len(view):
                score *= ind+2

    return score

def isVisible(i,j):
    left = [data[i][x] for x in range(j+1)]
    right = [data[i][x] for x in range(j, len(data[0]))]
    above = [data[x][j] for x in range(i+1)]
    below = [data[x][j] for x in range(i, len(data))]

    views = [left, right, above, below]
    for view in views:
        if data[i][j] == max(view) and view.count(data[i][j]) == 1:
            return 1
    return 0

def run(partTwo, data):
    answer = (len(data[0])*2 + len(data)*2 - 4) if not partTwo else 1
    for i, row in enumerate(data[1:-1]):
        i+=1
        for j, val in enumerate(row[1:-1]):
            j+=1
            if not partTwo: answer += isVisible(i, j)
            else: answer = max(answer, getScore(i,j))
    
    return answer

print("Part 1: ", run(False, data))
print("Part 1: ", run(True, data))
