files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    lines = [x.strip().split() for x in f.readlines()]
left = []
right = []

for i, j in lines:
    left.append(int(i))
    right.append(int(j))
    
def run(left, right, partTwo=False):
    left.sort()
    right.sort()
    total = 0
    for i in range(len(left)):
        if partTwo: total += right.count(left[i]) * left[i]
        else: total += abs(left[i] - right[i])
    return total

    
print("Part 1: ", run(left, right))
print("Part 2: ", run(left, right, True))