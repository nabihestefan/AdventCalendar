files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    data = [map(int,x.strip()) for x in f.readlines()]

def findPaths(data, start, partTwo):
    paths = []
    stack = [start]
    while stack:
        x,y = stack.pop(0)
        if data[y][x] == 9:
            paths.append((x,y))
            continue
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < len(data[0]) and 0 <= ny < len(data) and data[ny][nx] == data[y][x]+1:
                stack.append((nx,ny))
    return len(paths) if partTwo else len(set(paths))

def run(data, partTwo=False):
    starts = [(x,y) for x in range(len(data[0])) for y in range(len(data)) if data[y][x] == 0]
    paths = 0
    for s in starts:
        paths += findPaths(data,s,partTwo)    
    return paths
    
print("Part 1: ", run(data))
print("Part 2: ", run(data, True))