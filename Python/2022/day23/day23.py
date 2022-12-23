files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    data = [x for x in f.readlines()]
elves = set()
for y, row in enumerate(data):
    for x, val in enumerate(row):
        if val == "#": elves.add(complex(x,y))

def vis(elves):
    minX = int(min([x.real for x in elves]))
    maxX = int(max([x.real for x in elves]))
    minY = int(min([x.imag for x in elves]))
    maxY = int(max([x.imag for x in elves]))
    print(minX, minY)
    for y in range(minY, maxY+1):
        row = ""
        for x in range(minX, maxX+1):
            if complex(x,y) in elves: row += "#"
            else: row += "."
        print(row)
    print("="*100)
def adjacent(elf):
    x,y = elf.real, elf.imag
    # N, NE, E, SE, S, SW, W, NW
    yield complex(x,y-1)
    yield complex(x+1,y-1)
    yield complex(x+1,y)
    yield complex(x+1,y+1)
    yield complex(x,y+1)
    yield complex(x-1,y+1)
    yield complex(x-1,y)
    yield complex(x-1,y-1)

def move(elves, step):
    moves = dict()
    for elf in elves:
        adj = list(adjacent(elf))
        if len(set(adj) & elves) == 0: continue

        N = (set([adj[7], adj[0], adj[1]]), -1j)
        S = (set(adj[3:6]), 1j)
        E = (set(adj[1:4]), 1)
        W = (set(adj[5:]), -1)
        dirs = [N,S,W,E]
        elfMoved = False
        for i in range(4):
            if len(elves & dirs[(i+step)%4][0]) == 0:
                existing = moves.get(elf+dirs[(i+step)%4][1], [])
                existing.append(elf)
                moves[elf+dirs[(i+step)%4][1]] = existing
                elfMoved = True
                break

    moved = False
    for key in moves.keys():
        if len(moves[key]) == 1:
            moved = True
            elves.discard(moves[key][0])
            elves.add(key)
    return elves, moved


def run(elves):
    print(elves)
    for step in range(100000000):
        print(step)
        if step == 10: 
            minX = int(min([x.real for x in elves]))
            maxX = int(max([x.real for x in elves]))
            minY = int(min([x.imag for x in elves]))
            maxY = int(max([x.imag for x in elves]))

            empty = 0
            for x in range(minX, maxX+1):
                for y in range(minY, maxY+1):
                    if complex(x,y) not in elves: empty += 1
            print("Part 1: ", empty)
        elves, moved = move(elves, step)
        if not moved:
        
            print("Part 2: ", step+1)
            return

run(elves)