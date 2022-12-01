files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f:
    lines =  [a.strip().split(")") for a in f.readlines()]

orbits = {}
for i in lines: orbits[i[1]] = i[0]

totalOrbits = 0
for key in orbits:
    while orbits[key] != "COM":
        totalOrbits+=1
        key = orbits[key]
    totalOrbits += 1

print("Part 1: ", totalOrbits)

santaCOM = set()
key = "SAN"
while orbits[key] != "COM":
    key = orbits[key]
    santaCOM.add(key)

youCOM = set()
key = "YOU"
while orbits[key] != "COM":
    key = orbits[key]
    youCOM.add(key)

overlap = youCOM&santaCOM
dist = len(santaCOM-overlap) + len(youCOM-overlap)
print("Part 2: ", dist)
