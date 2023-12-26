import heapq
files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    graph = {(i,j): int(c) for i,r in enumerate(f.readlines()) for j,c in enumerate(r.strip())}

def run(graph, goal, minDist, maxDist):
    visited = set()
    queue = [(0, (0,0), (0,0))]
    while queue:
        heatLoss, pos, dir = heapq.heappop(queue)
        if pos == goal: return heatLoss
        if (pos, dir) in visited: continue
        visited.add((pos, dir))

        for newDir in {(1,0), (0,1), (-1,0), (0,-1)} - {dir, (-dir[0], -dir[1])}:
            newHeat, newPos = heatLoss, pos
            for i in range(1, maxDist+1):
                newPos = (newPos[0]+newDir[0], newPos[1]+newDir[1])
                if newPos in graph:
                    newHeat += graph[newPos]
                    if i >= minDist:
                        heapq.heappush(queue, (newHeat, newPos, newDir))



print("Part 1: ", run(graph, max(graph), 1, 3))
print("Part 2: ", run(graph, max(graph), 4, 10))