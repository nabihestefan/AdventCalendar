files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f:
    polymer = f.readlines()[0].strip()

units = {}
for i in polymer:
    if i.lower() not in units.keys(): units[i.lower()] = -1

def calcLen(polymer):
    while True:
        for i in range(len(polymer)-1):
            if ord(polymer[i]) - 32 == ord(polymer[i+1]) or ord(polymer[i]) + 32 == ord(polymer[i+1]):
                polymer = polymer[:i] + polymer[i+2:]
                break
        if i == len(polymer)-2: break
    return len(polymer)

def clean(polymer, i):
    polymer = polymer.replace(i ,"")
    polymer = polymer.replace(i.upper() ,"")
    return polymer


for i in units: units[i] = calcLen(clean(polymer[:], i))

print("Part 1: ", calcLen(polymer))
print("Part 2: ", min(units.values()))
