files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f: lines =  [int(a.strip()) for a in f.readlines()]

def valid(num, preamble):
    for i in preamble:
        for j in preamble:
            if i!=j and i+j == num:
                return True
    return False

preambleLen = 25

for i in range(preambleLen, len(lines)):
    if not valid(lines[i], lines[i-preambleLen:i]):
        part1 = lines[i]
        break

print("Part 1: ", part1)

for start in range(len(lines)):
    sum = 0
    for end in range(start, len(lines)):
        sum += lines[end]
        if sum > part1:
            break
        if sum == part1:
            print("Part 2: ", max(lines[start:end+1]) + min(lines[start:end+1]))
            exit()
