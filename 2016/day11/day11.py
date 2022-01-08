## Parsing
files = ['input.txt', 'testInput.txt']
with open(files[0], 'r') as f:
    lines =  [a.strip() for a in f.readlines()]

floors = [[], [], [], []]
for floor, line in enumerate(lines):
    if "nothing" in line:
        continue
    else:
        line = line[line.index("contains a")+11:]
        while line:
            if "," in line:
                part = line[0:line.index(",")]
                if "a " in part: part = part[2:]
                line = line[line.index(",")+2:]
                floors[floor].append(part.strip().split())
            elif "and" in line:
                part = line[0:line.index("and")]
                line = line[line.index("and a")+5:]
                floors[floor].append(part.strip().split())
            else:
                part = line[:-1]
                line = ""
                floors[floor].append(part.strip().split())
        if [] in floors[floor]: floors[floor].remove([])

for floor in floors:
    for part in floor:
        if "compatible" in part[0]:
            part[0] = part[0][0:part[0].index("-")]

for i in floors:
    print(i)
