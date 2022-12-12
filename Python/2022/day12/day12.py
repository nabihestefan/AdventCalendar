import networkx as nx
files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    data = [list(x.strip()) for x in f.readlines()]

map = []
g = nx.DiGraph()
p2Start = []

def getVal(char):
    if char == "S": return 0
    elif char == "E": return 25
    else: return ord(char) - ord("a")

for x,row in enumerate(data):
    for y, i in enumerate(row):
        if i == "S": start = (x,y)
        elif i == "E":  end = (x,y)
        if i == "S" or i == "a": p2Start.append((x,y))

        val = getVal(i)
        g.add_node((x,y))

        difs = [(1,0), (0,1), (-1,0), (0,-1)]
        for dx, dy in difs:
            newX = x-dx
            newY = y-dy
            if 0 <= newX and newX < len(data) and 0 <= newY and newY < len(data[0]):
                if getVal(data[newX][newY]) - val <= 1:
                    g.add_edge((x,y), (newX, newY))

def run(partTwo, g, start, end, p2Start):
    if not partTwo:
        paths = [len(nx.shortest_path(g, start, end))]
    else:
        paths = []
        for s in p2Start:
            try:
                path = nx.shortest_path(g, s, end)
                paths.append(len(path))
            except:
                continue
            
    return min(paths)-1
    
print("Part 1: ", run(False, g, start, end, p2Start))
print("Part 2: ", run(True, g, start, end, p2Start))
