files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    data = [[x=="#" for x in line.strip()] for line in f.readlines()]

def findBlanks(data):
    rows = set()
    cols = set()
    for i, row in enumerate(data):
        if True not in row: rows.add(i)
    
    for col in range(len(data[0])):
        if True not in [row[col] for row in data]: cols.add(col)
    
    return rows, cols

def findGalaxies(data):
    galaxies = []
    for i, row in enumerate(data):
        for j, point in enumerate(row):
            if point: galaxies.append((i,j))
    return galaxies

def run(data, partTwo):

    rows, cols = findBlanks(data)
    galaxies = findGalaxies(data)
    distances = 0
    for i, start in enumerate(galaxies):
        for goal in galaxies[i+1:]:
            rowSpan = set(range(min(start[0], goal[0]), max(start[0], goal[0])))
            colSpan = set(range(min(start[1], goal[1]), max(start[1], goal[1])))
            dist = abs(start[0]-goal[0]) + abs(start[1]-goal[1])
            for i in rowSpan.intersection(rows): dist += 999999 if partTwo else 1
            for i in colSpan.intersection(cols): dist += 999999 if partTwo else 1
            distances += dist
    return distances
            
print("Part 1: ", run(data, False))
print("Part 2: ", run(data, True))