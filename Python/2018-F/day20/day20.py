import networkx as nx
files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f: regex =  f.read()[1:-1]

g = nx.Graph()

pos = {(0,0)}
stack = []
starts, ends = {(0,0)}, set()


for char in regex:
    if char == '|':
        ends.update(pos)
        pos = starts
    elif char in "NESW":
        dir ={"N":(1,0), "E":(0,1), "S":(-1,0), "W":(0,-1)}[char]
        g.add_edges_from((p, (p[0]+dir[0], p[1]+dir[1])) for p in pos)
        pos = {(p[0]+dir[0], p[1]+dir[1]) for p in pos}
    elif char == '(':
        stack.append((starts, ends))
        starts, ends = pos, set()
    elif char == ')':
        pos.update(ends)
        starts, ends = stack.pop()

roomLengths = nx.algorithms.shortest_path_length(g,(0,0))
print("Part 1: ", max(roomLengths.values()))
print("Part 2: ", len([l for l in roomLengths.values() if l >= 1000]))
