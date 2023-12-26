files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    data = [x.strip() for x in f.readlines()]
    graph1 = dict()
    graph2 = dict()
    adj = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for x, line in enumerate(data):
        for y, char in enumerate(line):
            p1skip = False
            if char == "#": continue
            if char == "v":
                graph1[x+y*1j] = [(x+1+y*1j, 1)]
                p1skip = True
            if char == ">":
                graph1[x+y*1j] = [(x+(y+1)*1j, 1)]
                p1skip = True
            for dx, dy in adj:
                nx, ny = x+dx, y+dy
                if not (0 <= nx < len(data) and 0 <= nx < len(data[0])): continue
                if data[nx][ny] == "#": continue
                graph2[x+y*1j] = graph2.get(x+y*1j, []) + [(nx+(ny)*1j, 1)]
                if not p1skip:
                    if (dx,dy) == (-1,0) and data[nx][ny] == "v": continue
                    if (dx,dy) == (0,-1) and data[nx][ny] == ">": continue
                    graph1[x+y*1j] = graph1.get(x+y*1j, []) + [(nx+ (ny)*1j, 1)]
            

def simplify(graph):
    while True:
        for k, v in graph.items():
            if len(v) == 2:
                a, b = v
                if not ((k, a[1]) in graph[a[0]] and (k, b[1]) in graph[b[0]]): continue
                graph[a[0]].remove((k, a[1]))
                graph[b[0]].remove((k, b[1]))
                graph[a[0]].append((b[0], a[1]+b[1]))
                graph[b[0]].append((a[0], a[1]+b[1]))
                del graph[k]
                break
        else: 
            break
    return graph

graph1 = simplify(graph1)
graph2 = simplify(graph2)
goal = len(data)-1 + (len(data[0])-2)*1j

def move(graph, pos, goal, steps):
    if pos == goal: return 0
    next = []
    for node, dist in graph[pos]:
        if node in steps: continue
        m = move(graph, node, goal, steps.union({pos}))
        if m != -1: next.append(dist + m)
    if next == [] or next == -1: return -1
    return max(next)

print("Part 1: ", move(graph1, 1j, goal, set()))
print("Part 2: ", move(graph2, 1j, goal, set()))