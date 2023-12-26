files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    data = [x.strip().split(",") for x in f.readlines()]

def run(partTwo, data):
    total = 0
    for i,j in data:
        minA,maxA = map(int, i.split("-"))
        minB,maxB = map(int, j.split("-"))
        a = set(range(minA, maxA+1))
        b = set(range(minB, maxB+1))
        if partTwo:
            if len(a & b) > 0: total += 1
        else:
            if (a.issubset(b) or b.issubset(a)): total += 1

    return total


print("Part 1: ", run(False, data))
print("Part 2: ", run(True, data))
