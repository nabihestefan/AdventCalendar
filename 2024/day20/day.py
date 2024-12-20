files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    lines = [x.strip() for x in f.readlines()]

spaces = set()
start = end = 0
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == '.': spaces.add(complex(x, y))
        elif char == 'S':
            start = complex(x, y)
            spaces.add(start)
        elif char == 'E':
            end = complex(x, y)
            spaces.add(end)
        
def dist(a, b):
    return abs(a.real - b.real) + abs(a.imag - b.imag)


def run(spaces, start, end, partTwo=False):
    distances = {end: 0}
    pos = end
    while pos != start:
        for d in [1, -1, 1j, -1j]:
            newPos = pos + d
            if newPos in spaces and newPos not in distances:
                    distances[newPos] = distances[pos] + 1
                    pos = newPos
                    break
            
    cheats = set()
    for s in spaces:
        for e in spaces:
            d = dist(s, e)
            if s != e and d <= (20 if partTwo else 2):
                cheats.add((s, e, d))

    total = 0
    for s, e, d in cheats:
        total += (distances[e] - distances[s] - d) >= 100
    return total

print("Part 1: ", run(spaces, start, end))
print("Part 2: ", run(spaces, start, end, True))