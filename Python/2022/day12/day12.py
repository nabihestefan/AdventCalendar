files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    data = [list(x.strip()) for x in f.readlines()]
g = []

def getVal(char):
    if char == "S": return 0
    elif char == "E": return 25
    else: return ord(char) - ord("a")

for y,row in enumerate(data):
    r = []
    for x,i in enumerate(row):
        if i == "S": start = (x,y)
        elif i == "E":  end = (x,y)
        r.append(getVal(i))
    g.append(r)

def run(partTwo, g, start, end):
    if not partTwo: queue = [(start, 0)]
    else: queue = [(end, 0)]

    visited = set([start])
    minSteps = int(1e20)

    while queue:
        (x,y),steps = queue.pop(0)
        difs = [(1,0), (0,1), (-1,0), (0,-1)]
        val = g[y][x]

        if not partTwo:
            if (x,y) == end: minSteps = min(minSteps,steps)
        else:
            if val == 0: minSteps = min(minSteps,steps)

        for dx,dy in difs:
            newX = x+dx
            newY = y+dy
            if (newX,newY) in visited: continue
            if 0 <= newX and newX < len(data[0]) and 0 <= newY and newY < len(data):
                if g[newY][newX] - val <= 1 and not partTwo:
                    visited.add((newX,newY))
                    queue.append(((newX,newY), steps+1))
                elif val - g[newY][newX] <= 1 and  partTwo:
                    visited.add((newX,newY))
                    queue.append(((newX,newY), steps+1))
                    
    return minSteps

print("Part 1: ", run(False, g, start, end))
print("Part 2: ", run(True, g, start, end))
