files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f:
    r = f.readlines()[0].strip().split("-")
print r

def adj(num, part2):
    num = str(num)
    pair = []
    for i in range(len(num)-1):
        if num[i] == num[i+1]:
            pair.append(i)
    if not part2: return pair != []

    for i in pair:
        if i == 0:
            if num[i+2] != num[i]: return True
        elif i == 4:
            if num[i] != num[i-1]: return True
        else:
            if num[i+2] != num[i] and num[i] != num[i-1]: return True
    return False

def inc(num):
    num = str(num)
    for i in range(len(num)-1):
        if int(num[i]) > int(num[i+1]): return False
    return True

num = int(r[0])
valid = 0
while num <= int(r[1]):
    if adj(num, False) and inc(num): valid += 1
    num += 1

print("Part 1: ", valid)

num = int(r[0])
valid = 0
while num <= int(r[1]):
    if adj(num, True) and inc(num): valid += 1
    num += 1

print("Part 2: ", valid)
