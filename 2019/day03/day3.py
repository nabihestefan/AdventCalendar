files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f:
    wires = [a.strip().split(",") for a in f.readlines()]

def getWire(wireDirs):
    wire = set()
    wireS = {}
    pos = [0,0]
    steps = 0
    for i in wireDirs:
        if i[0] == "U":
            for j in range(int(i[1:])):
                pos[0]+=1
                steps += 1
                wire.add((pos[0], pos[1]))
                wireS[(pos[0], pos[1])] = steps
        if i[0] == "R":
            for j in range(int(i[1:])):
                pos[1]+=1
                steps += 1
                wire.add((pos[0], pos[1]))
                wireS[(pos[0], pos[1])] = steps
        if i[0] == "D":
            for j in range(int(i[1:])):
                pos[0]-=1
                steps += 1
                wire.add((pos[0], pos[1]))
                wireS[(pos[0], pos[1])] = steps
        if i[0] == "L":
            for j in range(int(i[1:])):
                pos[1]-=1
                steps += 1
                wire.add((pos[0], pos[1]))
                wireS[(pos[0], pos[1])] = steps
    return wire, wireS


wire1, wire1S = getWire(wires[0])
wire2, wire2S = getWire(wires[1])
intrs = wire1&wire2

dists = [abs(i[0])+abs(i[1]) for i in intrs]
distsP2 = [wire1S[i] + wire2S[i] for i in intrs]

print("Part 1: ", min(dists))
print("Part 2   : ", min(distsP2))
