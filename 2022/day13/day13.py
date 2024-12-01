files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    data = [pair.strip() for pair in f.read().split("\n\n")]


def compare(left, right):
    if type(left) == int and type(right) == int:
        if left > right: return -1
        if left < right: return 1
        return 0
    elif type(left) == list and type(right) == list:
        lenL = len(left)
        lenR = len(right)
        for i in range(min(lenL, lenR)):
            val = compare(left[i], right[i])
            if val != 0: return val
        if lenL < lenR: return 1
        if lenL > lenR: return -1
    elif type(left) == int:
        return compare([left], right)
    elif type(right) == int:
        return compare(left, [right])
    return 0
        

def part1(data):
    pairs = []
    for i in data:
        i = i.split("\n")
        pairs.append((eval(i[0]), eval(i[1])))
    valid = 0
    for ind, (left, right) in enumerate(pairs):
        if compare(left, right) == 1:
            valid += ind+1
    return valid

def part2(pairs):
    bigList = []
    for i in data:
        left, right = i.split("\n")
        bigList.append(eval(left)) 
        bigList.append(eval(right))
    val2 = 0
    val6 = 0
    for i in bigList:
        if compare(i, [[2]]) == 1: val2 += 1
        if compare(i, [[6]]) == 1: val6 += 1
    
    return((val2+1) * (val6+2))

print("Part 1: ", part1(data))
print("Part 2: ", part2(data))
