files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    data = [x.strip() for x in f.readlines()]

blocks = set([complex(x, y) for y in range(len(data)) for x in range(len(data[y])) if data[y][x] == '#'])
start = [complex(x,y) for y in range(len(data)) for x in range(len(data[y])) if data[y][x] == '^'][0]
MAX_X = len(data[0])
MAX_Y = len(data)

def transit(pos, dir, block=-1):
    visited = set()
    path = dict()
    while pos.imag < MAX_Y and pos.imag >= 0 and pos.real < MAX_X and pos.real >= 0:
        if pos+dir in blocks or pos+dir == block:
            dir *= 1j
        else: 
            if pos in visited and dir in path[pos]: return True, visited
            visited.add(pos)
            path[pos] = path.get(pos, []) + [dir]
            pos += dir
    return False, visited

def run(blocks, start):
    pos, dir = start, -1j
    _, visited = transit(pos,dir)

    p2 = 0
    for v in visited: p2 += transit(start, -1j,v)[0]
        
    return len(visited), p2
    
print("Part 1&2: ", run(blocks, start))
