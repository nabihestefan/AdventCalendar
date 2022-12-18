files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    data = set(tuple(map(int, x.split(","))) for x in f.readlines())

def adjacent(cube):
    x,y,z = cube
    yield x+1, y, z
    yield x-1, y, z
    yield x, y+1, z
    yield x, y-1, z
    yield x, y, z+1
    yield x, y, z-1

def run(partTwo, data):
    if partTwo:
        minX = min(x for x,y,z in data)
        maxX = max(x for x,y,z in data)
        minY = min(y for x,y,z in data)
        maxY = max(y for x,y,z in data)
        minZ = min(z for x,y,z in data)
        maxZ = max(z for x,y,z in data)

        xRange = range(minX, maxX+1)
        yRange = range(minY, maxY+1)
        zRange = range(minZ, maxZ+1)   
            
        outside = set()

        def isOutside(cube):
            if cube in data: return False
            
            checked = set()
            queue = [(cube)]

            while queue:
                cube = queue.pop()
                if cube in checked: continue
                checked.add(cube)

                if cube in outside:
                    outside.update(checked - data)
                    return True
                if cube[0] not in xRange or cube[1] not in yRange or cube[2] not in zRange:
                    outside.update(checked - data)
                    return True

                if cube not in data:
                    queue += adjacent(cube)
            return False
    
    sides = 0

    for cube in data:
        for adj in adjacent(cube):
            if not partTwo and adj not in data: sides += 1
            if partTwo and isOutside(adj): sides += 1
        
    return sides

print("Part 1: ", run(False, data))
print("Part 2: ", run(True, data))
