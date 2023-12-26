files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    maxI, maxJ = 0,0
    stones = set()
    for i, line in enumerate(f.readlines()):
        maxJ = len(line)
        maxI += 1
        for j, c in enumerate(line.strip()): 
            if c == "#":  stones.add(complex(i,j))
            if c == "S": start = complex(i,j)


def run(start, stones, edge, partTwo):
    cur = set([start])
    next = set()
    goal = 26501365
    quadForm = []
    for i in range(1, 65 if not partTwo else 1000):
        for pos in cur:
            for dx in [1, -1, 1j, -1j]:
                newPos = pos + dx
                x = complex((pos.real+dx.real)%edge, (pos.imag+dx.imag)%edge)
                if x not in stones: next.add(newPos)

        cur, next = next, set()

        if i%edge == goal%edge: quadForm.append(len(cur))
        if partTwo and len(quadForm) > 2:
            # Using day9 logic for quadratic extrapolation!
            difArray = [quadForm[i] - quadForm[i-1] for i in range(1, len(quadForm))]
            secDif = difArray[1]-difArray[0]
            for i in range(3, (goal//maxI)+1):
                difArray.append(difArray[-1] + secDif)
                quadForm.append(quadForm[-1] + difArray[-1])
            return quadForm[-1]
    return len(cur)
    
            
print("Part 1: ", run(start, stones, maxI, False))
print("Part 2: ", run(start, stones, maxI, True))