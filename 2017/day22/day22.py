with open('input.txt', 'r') as f: lines =  [a.strip() for a in f.readlines()]

infected = set()
clean = set()
mid = len(lines)//2

for y, i in enumerate(lines):
    for x, j in enumerate(i):
        if j == "#": infected.add((x-mid,y-mid))
        else: clean.add((x-mid,y-mid))
#  0
# 3 1
#  2
dirs = {0: lambda (x,y): (x, y-1), 2: lambda (x,y): (x, y+1),
        1: lambda (x,y): (x+1, y), 3: lambda (x,y): (x-1, y)}

nodes = {"clean":clean, "weakened":set(), "infected":infected, "flagged":set()}

def part1(infected):
    pos = (0,0)
    dir = 0
    bursts = 0
    for _ in range(10000):
        if pos in infected:
            dir = (dir+1)%4
            infected.remove(pos)
        else:
            bursts += 1
            dir = (dir-1)%4
            infected.add(pos)
        pos = dirs[dir](pos)
    return bursts

def updateNodes(nodes, pos):
    if pos in nodes["clean"]:
        nodes["clean"].remove(pos)
        nodes["weakened"].add(pos)
    elif pos in nodes["weakened"]:
        nodes["weakened"].remove(pos)
        nodes["infected"].add(pos)
    elif pos in nodes["infected"]:
        nodes["infected"].remove(pos)
        nodes["flagged"].add(pos)
    elif pos in nodes["flagged"]:
        nodes["flagged"].remove(pos)
        nodes["clean"].add(pos)
    else:
        nodes["weakened"].add(pos)

    return nodes

def part2(nodes):
    pos = (0,0)
    dir = 0
    bursts = 0
    for _ in range(10000000):
        if pos in nodes["weakened"]: bursts += 1
        elif pos in nodes["infected"]: dir = (dir+1)%4
        elif pos in nodes["flagged"]: dir = (dir+2)%4
        else: dir = (dir-1)%4

        nodes = updateNodes(nodes, pos)
        pos = dirs[dir](pos)
    return bursts

print("Part 1: ", part1(infected.copy()))
print("Part 2: ", part2(nodes))
