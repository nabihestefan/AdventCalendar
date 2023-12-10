import sys
sys.setrecursionlimit(20000)

files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    data = [i.strip() for i in f.readlines()]

def findLoop(data, start, loop, dir):
    if start in loop:
        return loop
    if len(loop) > len(set(loop)): return []
    
    i, j = loop[-1]
    if 0 > i or i >= len(data) or 0 > j or j > len(data[0]): return []

    if data[i][j] == "|":
        if dir == "N":
            return findLoop(data, start, loop + [(i-1,j)], dir)
        if dir == "S":
            return findLoop(data, start, loop + [(i+1,j)], dir)
        
    if data[i][j] == "-":
        if dir == "W":
            return findLoop(data, start, loop + [(i,j-1)], dir)
        if dir == "E":
            return findLoop(data, start, loop + [(i,j+1)], dir)
        
    if data[i][j] == "L":
        if dir == "S":
            return findLoop(data, start, loop + [(i,j+1)], "E")
        if dir == "W":
            return findLoop(data, start, loop + [(i-1,j)], "N")
        
    if data[i][j] == "J":
        if dir == "S":
            return findLoop(data, start, loop + [(i,j-1)], "W")
        if dir == "E":
            return findLoop(data, start, loop + [(i-1,j)], "N")
        
    if data[i][j] == "7":
        if dir == "N":
            return findLoop(data, start, loop + [(i,j-1)], "W")
        if dir == "E":
            return findLoop(data, start, loop + [(i+1,j)], "S")
        
    if data[i][j] == "F":
        if dir == "N":
            return findLoop(data, start, loop + [(i,j+1)], "E")
        if dir == "W":
            return findLoop(data, start, loop + [(i+1,j)], "S")

    return []
    

def run(data):
    for i, line in enumerate(data):
        if "S" in line:
            start = (i,line.index("S"))

    loop = []
    for di, dj, dir in [(0,1, "E"),(1,0, "S"),(0,-1, "W"),(-1,0, "N")]:
        if len(loop) == 0:
            loop = findLoop(data, start, [(start[0]+di, start[1]+dj)], dir)

    dx0,dy0 = loop[0][0] - start[0], loop[0][1] - start[1]
    dx1,dy1 = loop[-1][0] - start[0], loop[-1][1] - start[1]
    if (dx0 == -1 and dy1 == 1) or (dx1 == -1 and dy0 == 1) or \
        (dx0 == -1 and dy1 == -1) or (dx1 == -1 and dy0 == -1) or \
        (dx0 + dx1 == 0):
        counters = "LSJ|"
    else: counters = "LJ|"
    
    trapped = 0
    for i, line in enumerate(data):
        for j in range(len(line)):
            if (i,j) in loop: continue
            left = len([x for x in range(j, -1, -1) if (i,x) in loop and data[i][x] in counters])
            if left%2 == 1:  trapped += 1
            
    return len(loop)/2, trapped
            
print("Part 1 & 2: ", run(data))