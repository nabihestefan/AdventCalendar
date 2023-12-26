files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    data = dict()
    cont = f.read().strip().splitlines()
    for x, line in enumerate(cont):
        for y, char in enumerate(line.strip()):
            data[x+y*1j] = char

def move(beam, dir, data):
    match data[beam]:
        case ".": return [(beam + dir, dir)]
        case "|": 
            if dir.imag == 0: return [(beam + dir, dir)]
            else: return [(beam + 1, 1), (beam - 1, -1)]
        case "-":
            if dir.real == 0: return [(beam + dir, dir)]
            else: return [(beam + 1j, 1j), (beam - 1j, -1j)]
        case "/":
            if dir == 1j: return [(beam - 1, -1)]
            if dir == -1j: return [(beam + 1, 1)]
            if dir == 1: return [(beam - 1j, -1j)]
            if dir == -1: return [(beam + 1j, +1j)]
        case "\\":
            if dir == 1j: return [(beam + 1, +1)]
            if dir == -1j: return [(beam - 1, -1)]
            if dir == 1: return [(beam + 1j, +1j)]
            if dir == -1: return [(beam - 1j, -1j)]
    return []

def run(data, start):
    tiles = dict()
    queue = [start]
    while queue:
        beam, dir = queue.pop(0)
        tiles[beam] = tiles.get(beam, []) + [dir]
        newBeams = move(beam, dir, data)
        for newBeam, newDir in newBeams:
            if newDir not in tiles.get(newBeam, []) and newBeam in data:
                queue.append((newBeam, newDir))
        
    return len(tiles)

print("Part 1: ", run(data, (0, 1j)))
print("Part 2: ", max([run(data, (a, 1j)) for a in range(len(cont))] + 
                      [run(data, (b+(len(cont)-1)*1j, -1j)) for b in range(len(cont))] + 
                      [run(data, (c*1j, 1)) for c in range(len(cont))] + 
                      [run(data, ((len(cont)-1)+d*1j, -1)) for d in range(len(cont))]))