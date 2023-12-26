files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    data = [list(map(int, list(x.strip()))) for x in f.readlines()]

def run(partTwo, data):
    answer = (len(data[0])*2 + len(data)*2 - 4) if not partTwo else 1
    for i, row in enumerate(data[1:-1]):
        i+=1
        for j, val in enumerate(row[1:-1]):
            j+=1
            curTree = data[i][j]
            score = 1

            left = [data[i][x] for x in range(j+1)]
            right = [data[i][x] for x in range(j, len(data[0]))]
            above = [data[x][j] for x in range(i+1)]
            below = [data[x][j] for x in range(i, len(data))]
            views = [left, right, above, below]

            for ind, view in enumerate(views):
                if not partTwo: 
                    if curTree == max(view) and view.count(curTree) == 1:
                        answer += 1 
                        break
                else:
                    if ind % 2 == 0: view = view[::-1]
                    view = view[1:]

                    for indT, tree in enumerate(view[:-1]):
                        if tree >= curTree:
                            score *= indT+1
                            break
                        if indT+2 == len(view):
                            score *= indT+2

            answer = max(answer, score)
    
    return answer

print("Part 1: ", run(False, data))
print("Part 1: ", run(True, data))
