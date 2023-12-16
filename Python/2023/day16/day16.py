files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    data = [x.strip() for x in f.readlines()]

def move(beam, dir, data):
    match data[int(beam.real)][int(beam.imag)]:
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
            if newDir not in tiles.get(newBeam, []) and 0 <= newBeam.real < len(data) and 0 <= newBeam.imag < len(data[0]):
                queue.append((newBeam, newDir))
        
    return len(tiles)

print("Part 1: ", run(data, (0, 1j)))
print("Part 2: ", max([run(data, (a, 1j)) for a in range(len(data))] + 
                      [run(data, (b+(len(data[0])-1)*1j, -1j)) for b in range(len(data))] + 
                      [run(data, (c*1j, 1)) for c in range(len(data[0]))] + 
                      [run(data, ((len(data)-1)+d*1j, -1)) for d in range(len(data))]))