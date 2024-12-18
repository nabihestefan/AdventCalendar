files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    data = [map(int, x.strip().split(",")) for x in f.readlines()]

L = 71
# L = 7

def bfsish(spaces, start):
    queue = [start]
    dist = {start: 0}
    parents = dict()
    while queue:
        pos = queue.pop(0)
        for i in [1, -1, 1j, -1j]:
            if pos+i in spaces and pos+i not in dist.keys():
                dist[pos+i] = dist[pos] + 1
                parents[pos+i] = pos
                if pos+i == complex(L-1, L-1): return dist, parents # Bail once we see the end
                queue.append(pos+i)
    return dist, parents

def getPath(parents):
    path = []
    pos = complex(L-1, L-1)
    while pos != 0:
        path.append(pos)
        pos = parents[pos]
    return path

def run(data, partTwo=False):
    spaces = set((complex(i,j)) for i in range(L) for j in range(L))
    i = 1024
    # i = 12
    for x,y in data[:i]: spaces.remove(complex(x,y))
    
    dist, parents = bfsish(spaces, 0)
    if not partTwo: return dist[complex(L-1, L-1)]

    path = getPath(parents)
    while True:
        x,y = data[i]
        spaces.remove(complex(x,y))
        if complex(x,y) in path:
            dist, parents = bfsish(spaces, 0)
            if complex(L-1, L-1) not in dist.keys():
                return x,y
            path = getPath(parents)
        i += 1

print("Part 1: ", run(data))
print("Part 2: ", run(data, True))