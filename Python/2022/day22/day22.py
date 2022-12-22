files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    data = [x for x in f.readlines()]

def parseTiles(tilesRaw):
    openTiles = set()
    closedTiles = set()
    start = None
    for y, row in enumerate(tilesRaw):
        for x, val in enumerate(row):
            if val == ".": 
                openTiles.add(complex(x,y))
                if start == None: start = complex(x,y)

            if val == "#": closedTiles.add(complex(x,y))
    return start, openTiles, closedTiles
def parseInstructions(instructionsRaw):
    instructions = []
    i = 0
    moves = ""
    while i < len(instructionsRaw):
        if instructionsRaw[i] in ["R", "L"]:
            instructions.append(int(moves))
            instructions.append(instructionsRaw[i])
            moves = ""
        else:
            moves += instructionsRaw[i]
        i += 1
    instructions.append(int(moves))

    return instructions
instructions = parseInstructions(data[-1].strip())
start, openTiles, closedTiles = parseTiles(data[:-2])

def nextOpen(partTwo, pos, dir, openTiles, closedTiles):
    next = pos + dir
    if next in openTiles: return next, dir
    if next in closedTiles: return pos, dir
    # Im wrapping around
    if not partTwo:
        next = pos - dir 
        while next in openTiles or next in closedTiles: next -= dir
        next += dir
        newDir = dir
    else:
        # Hard coding the edges cause I cant figure out how to do it for every input
        edge1A = [complex(149,i) for i in range(0,50)]
        edge1B = [complex(99,i) for i in range(100,150)[::-1]]
        if pos in edge1A: next, newDir = edge1B[edge1A.index(pos)], -1
        if pos in edge1B: next, newDir = edge1A[edge1B.index(pos)], -1

        edge2A = [complex(i,49) for i in range(100,150)]
        edge2B = [complex(99, i) for i in range(50,100)]
        if pos in edge2A: next, newDir = edge2B[edge2A.index(pos)], -1
        if pos in edge2B: next, newDir = edge2A[edge2B.index(pos)], -1j

        edge3A = [complex(i, 0) for i in range(100,150)]
        edge3B = [complex(i, 199) for i in range(0,50)]
        if pos in edge3A: next, newDir = edge3B[edge3A.index(pos)], -1j
        if pos in edge3B: next, newDir = edge3A[edge3B.index(pos)], 1j

        edge4A = [complex(i, 0) for i in range(50,100)]
        edge4B = [complex(0, i) for i in range(150,200)]
        if pos in edge4A: next, newDir = edge4B[edge4A.index(pos)], 1
        if pos in edge4B: next, newDir = edge4A[edge4B.index(pos)], 1j

        edge5A = [complex(50, i) for i in range(0,50)]
        edge5B = [complex(0, i) for i in range(100,150)[::-1]]
        if pos in edge5A: next, newDir = edge5B[edge5A.index(pos)], 1
        if pos in edge5B: next, newDir = edge5A[edge5B.index(pos)], 1

        edge6A = [complex(50, i) for i in range(50,100)]
        edge6B = [complex(i, 100) for i in range(0,50)]
        if pos in edge6A: next, newDir = edge6B[edge6A.index(pos)], 1j
        if pos in edge6B: next, newDir = edge6A[edge6B.index(pos)], 1

        edge7A = [complex(i, 149) for i in range(50,100)]
        edge7B = [complex(49, i) for i in range(150,200)]
        if pos in edge7A: next, newDir = edge7B[edge7A.index(pos)], -1
        if pos in edge7B: next, newDir = edge7A[edge7B.index(pos)], -1j

    if next in openTiles: return next, newDir
    if next in closedTiles: return pos, dir

def run(partTwo, instructions, start, openTiles, closedTiles):
    pos = start
    dir = complex(1,0)
    for i in instructions:
        if i == "R": dir *= 1j
        elif i == "L": dir *= -1j
        else:
            for _ in range(i):
                pos, dir = nextOpen(partTwo, pos, dir, openTiles, closedTiles)

    if dir == 1:   facing = 0
    if dir == 1j:  facing = 1
    if dir == -1:  facing = 2
    if dir == -1j: facing = 3
    
    return int(4*(pos.real+1) + 1000*(pos.imag+1) + facing)


print("Part 1: ", run(False, instructions, start, openTiles, closedTiles))
print("Part 2: ", run(True, instructions, start, openTiles, closedTiles))
