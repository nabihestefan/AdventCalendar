files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    data = [x.strip() for x in f.readlines()]

antennas = dict()
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] != ".":
            antennas[data[i][j]] = antennas.get(data[i][j], []) + [(i, j)]
MAX_X = len(data[0])
MAX_Y = len(data)

def getAntinodes(ant, dx, dy, partTwo):
    antinodes = set()
    x,y = ant[0]+dx, ant[1]+dy
    while 0 <= x < MAX_X and 0 <= y < MAX_Y:
        antinodes.add((x,y))
        x += dx
        y += dy
        if not partTwo: break
    return antinodes - set([ant])

def findAntinodes(ant1, ant2, partTwo):
    dx, dy = ant2[0] - ant1[0], ant2[1] - ant1[1]
    return getAntinodes(ant1, -dx, -dy, partTwo).union(getAntinodes(ant2, dx, dy, partTwo))
    
def run(antennas, partTwo=False):
    antinodes = set(list(sum(list(antennas.values()), []))) if partTwo else set()
    for f in antennas:
        for i in range(len(antennas[f])):
            for j in range(i+1, len(antennas[f])):
                antinodes.update(findAntinodes(antennas[f][i], antennas[f][j], partTwo))
    return len(antinodes)
    
print("Part 1: ", run(antennas))
print("Part 2: ", run(antennas, True))