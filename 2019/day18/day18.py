import heapq
import time
files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f:
    grid = [a.strip() for a in f.readlines()]

def run(grid, partTwo):
    linGrid = []
    for i in grid: linGrid += i
    w,h = len(grid[0]), len(grid)
    n = linGrid.index("@")
    x, y = n % w, n // w
    allkeys = set(c for c in linGrid if c.islower())

    if partTwo:
        grid[y-1] = grid[y-1][:x]   +  '#'  + grid[y-1][x+1:]
        grid[  y] = grid[y  ][:x-1] + '###' + grid[y  ][x+2:]
        grid[y+1] = grid[y+1][:x]   +  '#'  + grid[y+1][x+1:]

        pos = (
          (x-1, y-1),
          (x+1, y-1),
          (x-1, y+1),
          (x+1, y+1),
        )
    else:
        pos = ((x,y),)

    def reachableKeys(sx, sy, keys):
        q = [(sx, sy, 0)]
        #print(q)
        seen = set()
        d = ( (-1, 0), (1, 0), (0, -1), (0, 1) )
        while q:
            cx, cy, l = q.pop(0)
            if grid[cy][cx].islower() and grid[cy][cx] not in keys:
                yield l, cx, cy, grid[cy][cx]
                continue
            for dx, dy in d:
                nx, ny = cx + dx, cy + dy
                if ((nx, ny)) in seen:
                    continue
                seen.add((nx, ny))

                c = grid[ny][nx]
                if c != '#' and (not c.isupper() or c.lower() in keys):
                    q.append((nx, ny, l + 1))


    # Shortest path from node "no keys" to node "all keys".
    q = [(0, pos, frozenset())]
    seen = set()
    while q:
        d, cpos, keys = heapq.heappop(q)
        #print(sorted(keys))
        if keys == allkeys:
            return d

        if (cpos, keys) in seen:
            continue
        seen.add((cpos, keys))

        for i, (cx, cy) in enumerate(cpos):
            for l, nx, ny, key in reachableKeys(cx, cy, keys):
                npos = cpos[0:i] + ((nx, ny),) + cpos[i+1:]
                heapq.heappush(q, (d + l, npos, keys | frozenset([key])))

startTime = time.time()
print("Part 1: ", run(grid[:], False))
print("Runtime: ", time.time()-startTime)
startTime = time.time()
print("Part 2: ", run(grid[:], True))
print("Runtime: ", time.time()-startTime)
