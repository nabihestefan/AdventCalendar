with open('input.txt', 'r') as f: lines =  [a.strip() for a in f.readlines()]

#Create ports dictionary
ports = dict()
for i in lines:
    p1,p2 = map(int, i.split("/"))
    ports[p1] = ports.get(p1, []) + [p2]
    ports[p2] = ports.get(p2, []) + [p1]

# Recursive Function to build all paths
def buildpath(path, ports):
    path = path or [(0,0)]
    end = path[-1][1]
    for next in ports[end]:
        if not((end,next) in path or (next,end) in path):
            newPath = path + [(end,next)]
            yield newPath
            yield from buildpath(newPath, ports)

# List of all paths
paths = buildpath(None, ports)

#values for every path
values = []
for path in paths:
    values.append((len(path), sum([i+j for i,j in path])))

# Sorting for answers
print("Part 1: ", sorted(values, key = lambda x: x[1])[-1][1])
print("Part 2: ", sorted(values, key = lambda x: x[0])[-1][1])
