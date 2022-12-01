files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f: adapters =  [int(a.strip()) for a in f.readlines()]

adapters.append(0)
adapters.sort()
adapters.append(adapters[-1]+3)

j1Dif = 0
j3Dif = 0
joltage = 0

for i in adapters:
    if i-joltage == 1:
        j1Dif += 1
    if i-joltage == 3:
        j3Dif += 1
    joltage = i

print("Part 1: ", j1Dif*j3Dif)

paths = {}
paths[0] = 1
for adapter in adapters:
    for d in range(1,4):
        if (adapter+d) in adapters:
            if adapter+d in paths.keys():
                paths[adapter+d] += paths[adapter]
            else:
                paths[adapter+d] = paths[adapter]

print("Part 2: ", paths[adapters[-1]])
