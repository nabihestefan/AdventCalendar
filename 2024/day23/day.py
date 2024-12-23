files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    connections = [x.strip().split("-") for x in f.readlines()]

computers = {}
for connection in connections:
    a, b = connection
    computers[a] = computers.get(a, set).union({b}) 
    computers[b] = computers.get(b, set()).union({a})

def run(computers):
    groups = set()
    threes = set()
    for computer in computers:
        for connection in computers[computer]:
            inter = computers[connection].intersection(computers[computer])
            for i in inter:
                groups.add(tuple(sorted([computer, connection, i])))
                if computer[0] == "t": threes.add(tuple(sorted([computer, connection, i])))

    while True:
        moved = False
        newGroups = set()
        for group in groups:
            inter = set(computers[group[0]])
            for computer in group[1:]:
                inter = inter.intersection(computers[computer])
            for i in inter:
                newGroups.add(tuple(sorted([i] + list(group))))
                moved = True
        if not moved: break
        groups = newGroups

    return len(threes), ",".join(groups.pop())

    
print("Part 1&2: ", run(computers))