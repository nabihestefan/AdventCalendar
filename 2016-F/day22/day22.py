## Parsing
files = ['input.txt', 'testInput.txt']
nodes = dict()

def available(node):
    return node["size"] - node["used"]

def viablePair(node1, node2):
    return node1["used"] != 0 and node1!=node2 and node1["used"]<=available(node2)

with open(files[0], 'r') as f:
    for line in f.readlines()[2:]:
        words = line.strip().split()
        size = int(words[1][:-1])
        used = int(words[2][:-1])
        file = words[0]
        x = int(file[file.index("x")+1:file.index("-y")])
        y = int(file[file.index("y")+1:])
        nodes[(x,y)] = {"size":size, "used":used}

print("Part 1: ", sum(1 for n1 in nodes.values() for n2 in nodes.values() if viablePair(n1,n2)))

maxX = max([k[0] for k in nodes.keys()])
maxY = max([k[1] for k in nodes.keys()])

def findPath(start, data, obstacle=None):
    for node in nodes.values():
        node['dist'] = float('inf')
        node['prev'] = None
    q = [start]
    nodes[start]['dist'] = 0
    while q:
        x,y = q.pop(0)
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx,ny = x+dx, y+dy
            if (nx,ny) in nodes.keys() and nodes[(nx,ny)]["used"]<100 and (nx,ny)!= obstacle:
                if nodes[(nx, ny)]['dist'] > nodes[(x,y)]['dist'] + 1:
                    nodes[(nx, ny)]['dist'] = nodes[(x,y)]['dist'] + 1
                    nodes[(nx, ny)]['prev'] = (x,y)
                    q.append((nx, ny))
                if (nx, ny) == data:
                    path = [(nx, ny)]
                    while nodes[path[-1]]['prev'] != None:
                        path.append(nodes[path[-1]]['prev'])
                    return path[-2::-1]

start, data = (0,0), (maxX,0)
empty = (None,None)
for key in nodes.keys():
    if nodes[key]["used"] == 0:
        empty = key
        break

pathBasic = findPath(data, start)
c = 0
while data != start:
    newPath = findPath(empty, pathBasic.pop(0), data)
    c += len(newPath) + 1
    empty = data
    data = newPath[-1]
print("Part 2:", c)
