from copy import deepcopy
from collections import defaultdict
files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f:
    line = f.readlines()[0].strip()

xLiteral = line[line.index("x=")+2:line.index(",")]
yLiteral = line[line.index("y=")+2:]

xRangeLits = (int(xLiteral[0:xLiteral.index("..")]), int(xLiteral[xLiteral.index("..")+2:]))
yRangeLits = (int(yLiteral[0:yLiteral.index("..")]), int(yLiteral[yLiteral.index("..")+2:]))

xRange = lambda x: x >= xRangeLits[0] and x <= xRangeLits[1]
yRange = lambda y: y >= yRangeLits[0] and y <= yRangeLits[1]
xOver = lambda x: x > xRangeLits[1]
yOver = lambda y: y < yRangeLits[0]
triangNum = lambda x: (x*(x+1))//2

def findXRanges():
    global xRange, xOver
    valid = defaultdict(list)
    stoppers = findXTriangs()
    for xv in range(xRangeLits[1]+1):
        x = 0
        step = 0
        xvCop = deepcopy(xv)
        while xvCop != 0 and not xOver(x):
            step += 1
            x += xvCop
            xvCop -= 1
            if xRange(x) and not (xv == step):
                valid[step].append(xv)
    return valid

def findXTriangs():
    global triangNum, xRange
    stoppers = []
    x = 0
    while not xOver(triangNum(x)):
        if xRange(triangNum(x)): stoppers.append(x)
        x += 1
    return stoppers

def findYRanges():
    global yRange, yOver
    valid = defaultdict(list)
    for yv in range(yRangeLits[0], abs(yRangeLits[0])):
        y = 0
        step = 0
        yvCop = deepcopy(yv)
        while not yOver(y):
            step += 1
            y += yvCop
            yvCop -= 1
            if yRange(y):
                valid[step].append(yv)
    return valid

valid = []
yRanges = findYRanges()
xRanges = findXRanges()
stoppers = findXTriangs()
for key in yRanges.keys():
    if key in xRanges.keys():
        for xv in xRanges[key]:
            for yv in yRanges[key]:
                valid.append((xv, yv))
    for i in stoppers:
        if key >= i:
            for yv in yRanges[key]:
                valid.append((i, yv))

print("Part 1: ", triangNum(abs(yRangeLits[0])-1))
print("Part 2: ", len(set(valid)))
