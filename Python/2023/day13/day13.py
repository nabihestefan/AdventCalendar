files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    data = [x.splitlines() for x in f.read().split('\n\n')]

def findReflection(mirrorMap, partTwo):
    for i in range(1,len(mirrorMap)):
        diff = 0
        for di in range(i):
            if 0 <= i-di-1 and i+di < len(mirrorMap):
                diff += sum(r != l for r, l in zip(mirrorMap[i-di-1], mirrorMap[i+di]))
                if diff > 0 if not partTwo else diff > 1: break
        if diff == 0 if not partTwo else diff == 1: 
            return i
    return 0

def run(data, partTwo):
    total = 0
    for mirrorMap in data:
        total += findReflection(list(zip(*mirrorMap[::-1])), partTwo)
        total += findReflection(mirrorMap, partTwo)*100
    return total
            
print("Part 1: ", run(data, False))
print("Part 2: ", run(data, True))