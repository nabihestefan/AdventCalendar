files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    lines = [x.strip() for x in f.readlines()]

start = end = None
floor = set()
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] in '.SE': floor.add(complex(i, j))
        if lines[i][j] ==  "S": start = complex(i, j)
        if lines[i][j] ==  "E": end = complex(i, j)


def run(floor, start, end):
    queue = [(start, 1j, 0)]
    visited = set()
    distStart = dict()
    minPath = 1e9
    while queue:
        pos, dir, cost = min(queue, key=lambda x: x[2])
        queue.remove((pos, dir, cost))

        if cost > minPath: continue
        if (pos, dir) in visited: continue
        visited.add((pos, dir))
        distStart[(pos, dir)] = cost
        if pos == end: minPath = min(minPath, cost)

        if (pos + dir) in floor: queue.append((pos + dir, dir, cost+1))
        queue.append((pos, dir*1j, cost+1000))
        queue.append((pos, dir*-1j, cost+1000))

    queue = [(end, 1, 0), (end, -1, 0), (end, 1j, 0), (end, -1j, 0)]
    visited = set()
    distEnd = dict()
    while queue:
        pos, dir, cost = min(queue, key=lambda x: x[2])
        queue.remove((pos, dir, cost))

        if cost > minPath: continue
        if (pos, dir) in visited: continue
        distEnd[(pos, dir)] = cost
        visited.add((pos, dir))
        
        if (pos - dir) in floor: queue.append((pos - dir, dir, cost+1))
        queue.append((pos, dir*1j, cost+1000))
        queue.append((pos, dir*-1j, cost+1000))
    
    seats = set()
    for state in distStart:
        if state in distEnd and distStart[state] + distEnd[state] == minPath:
            seats.add(state[0])

    return minPath, len(seats)
    
print("Part 1&2: ", run(floor, start, end))