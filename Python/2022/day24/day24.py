files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    data = [x for x in f.readlines()]

walls = set()
blizzards = set()
for y, row in enumerate(data):
    for x, val in enumerate(row):
        if val == "#": walls.add(complex(x,y))
        if val == ">": blizzards.add((complex(x,y), 1))
        if val == "v": blizzards.add((complex(x,y), 1j))
        if val == "<": blizzards.add((complex(x,y), -1))
        if val == "^": blizzards.add((complex(x,y), -1j))

start = complex(1,0)
end = complex(max([x.real for x in walls])-1, max([x.imag for x in walls]))
walls.add(start-1j)
walls.add(end+1j)

def updateBlizzards(blizzards, walls):
    newBlizzards = set()
    for b,dir in blizzards:
        newB = b+dir
        if newB in walls:
            newB -= dir
            while newB not in walls: newB -= dir
            newB += dir
        newBlizzards.add((newB, dir))
    return newBlizzards

def run(walls, blizzards, start, end):
    queue = [(start, 0)]
    prevStep = -1
    T1Done = False
    T2Done = False
    visited = set((start,0))
    while queue:
        pos,steps = queue.pop(0)
        if pos == end and not T1Done: 
            print("Part 1: ", steps)
            queue = [(pos, steps)]
            visited = set((pos,steps))
            T1Done = True
            continue
        if T1Done and not T2Done and pos == start:
            print("Got Back! ", steps)
            queue = [(pos, steps)]
            visited = set((pos,steps))
            T2Done = True
            continue
        if T1Done and T2Done and pos == end:
            print("Part 2: ", steps)
            return
        moves = [0, 1, 1j, -1, -1j]
        if prevStep != steps:
            prevStep = steps
            blizzards = updateBlizzards(blizzards,walls)
        for move in moves:
            newPos = pos + move
            if newPos not in set([x[0] for x in blizzards]) and newPos not in walls and (newPos, steps+1) not in visited:
                queue.append((newPos, steps+1))
                visited.add((newPos, steps+1))
   


run(walls, blizzards, start, end)