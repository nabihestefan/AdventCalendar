import ast
files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f:
    lines = [list(a.strip()) for a in f.readlines()]

for indi, i in enumerate(lines):
    for indj, j in enumerate(i):
        try:
            lines[indi][indj] = int(lines[indi][indj])
        except ValueError:
            continue
lines = [[a for a in line if a != ","] for line in lines]


def simplifySnailNum(snailNum):
    explosions = True
    while True:
        stack = 0
        for ie, char in enumerate(snailNum):
            if char == "[":
                stack += 1
                continue
            elif char == "]":
                stack -= 1
                continue
            else:
                if stack > 4 and isinstance(snailNum[ie+1], int):
                    snailNum = explode(snailNum, ie)
                    break
        if ie == len(snailNum)-1: explosions = False
        if not explosions:
            for isp, char in enumerate(snailNum):
                if char == "[":
                    stack += 1
                    continue
                elif char == "]":
                    stack -= 1
                    continue
                else:
                    if char > 9:
                        snailNum = splits(snailNum, isp)
                        break
            if isp == len(snailNum)-1: return snailNum

def explode(snailNum, i):
    pair = (snailNum[i], snailNum[i+1])
    pointerLeft  = i-1
    left = 0,0
    while True:
        if pointerLeft < 0:
            break
        if isinstance(snailNum[pointerLeft], int):
            snailNum[pointerLeft] += pair[0]
            left = pointerLeft, snailNum[pointerLeft]
            break
        pointerLeft -= 1

    pointerRight = i+3
    right = 0,0
    while True:
        if pointerRight >= len(snailNum):
            break
        if isinstance(snailNum[pointerRight], int):
            snailNum[pointerRight] += pair[1]
            right = pointerRight, snailNum[pointerRight]
            break
        pointerRight += 1
    # if right[1] > 9:
    #     return splits(snailNum[:i-1] + [0] + snailNum[i+3:], pointerRight-3)
    # if left[1] > 9:
    #     return splits(snailNum[:i-1] + [0] + snailNum[i+3:], pointerLeft)

    return snailNum[:i-1] + [0] + snailNum[i+3:]


def splits(snailNum, i):
    pair = ["[", snailNum[i]//2, snailNum[i] - snailNum[i]//2, "]"]
    return snailNum[:i] + pair + snailNum[i+1:]

def snailMagnitude(snailNum):
    s = lambda x, y: 3*x + 2*y
    while True:
        if len(snailNum) == 1:
            return snailNum
        for i, char in enumerate(snailNum):
            if isinstance(char, int) and isinstance(snailNum[i+1], int):
                newNum = s(char, snailNum[i+1])
                snailNum = snailNum[:i-1] + [newNum] + snailNum[i+3:]
                break

snailSum = lines[0]
for snailNum in lines[1:]:
    newSum = ["["] + snailSum + snailNum + ["]"]
    snailSum = simplifySnailNum(newSum)


print("Part 1: ", snailMagnitude(snailSum)[0])

magnitudes = []
for i in lines:
    for j in lines:
        if i != j:
            magnitudes.append(snailMagnitude(simplifySnailNum(["["]+i+j+["]"])))
            magnitudes.append(snailMagnitude(simplifySnailNum(["["]+j+  i+["]"])))

print("Part 2: ", max(magnitudes)[0])
