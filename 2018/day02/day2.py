files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f:
    lines =  [a.strip() for a in f.readlines()]

def createDict(line):
    d = {}
    for c in line: d[c] = d.get(c,0) + 1
    return d

twos = 0
threes = 0
for line in lines:
    d = createDict(line)
    if 2 in d.values(): twos += 1
    if 3 in d.values(): threes += 1

print("Part 1: ", twos*threes)

for a in lines:
    for b in lines:
        d = 0
        for ind,c in enumerate(a):
            if c != b[ind]: d += 1
        if d == 1:
            ans = "".join([c for ind,c in enumerate(a) if b[ind]==c])
            print("Part 2: ", ans)
            exit()
