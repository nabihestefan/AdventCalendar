from math import sqrt
with open('input.txt', 'r') as f:
    num = int(f.readlines()[0])

def part1():
    val = 1
    d = dict()
    d[(0,0)] = val
    x,y,layer = 1,0,1
    while val < num:
        val+=1
        d[(x,y)] = val
        x,y,layer = moveNext(x,y,layer)
    return abs(x) + abs(y) - 1

def moveNext(x,y,layer):
    if x == -1*layer:
        if y == -1*layer:
            return x, y+1, layer
        elif y == layer:
            return x+1, y, layer
        else:
            return x, y+1, layer
    elif x == layer:
        if y == -1*layer:
            return x-1, y, layer
        elif y == layer:
            return x+1, y, layer+1
        else:
            return x, y-1, layer
    else:
        if y == -1*layer:
            return x-1, y, layer
        elif y == layer:
            return x+1, y, layer

def part2():
    val = 1
    d = dict()
    d[(0,0)] = val
    x,y,layer = 1,0,1
    while val < num:
        val = 0
        for dx,dy in [(1,0), (1,1), (1,-1), (0,1), (0,-1), (-1,1), (-1,0), (-1,-1)]:
            nx,ny = x+dx, y+dy
            if (nx,ny) in d.keys(): val += d[(nx,ny)]
        d[(x,y)] = val
        x,y,layer = moveNext(x,y,layer)
    return val


print("Part 1: ", part1())
print("Part 2: ", part2())
