files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    data = [x.split() for x in f.readlines()]

dirs = {"R": (0,1), "L":(0,-1), "U": (1,0), "D":(-1,0)}

def inRange(head,tail):
    di = dj = 0
    difi, difj = head[0]-tail[0], head[1]-tail[1]

    if abs(difi) > 1:
        if difj != 0: dj = (difj/abs(difj))
        di = (difi/abs(difi))
    elif abs(difj) > 1:
        if difi != 0: di = (difi/abs(difi))
        dj = (difj/abs(difj))
        
    return di, dj

def run(partTwo, data):
    tailPos = set()
    if not partTwo: ropeLen = 2
    else: ropeLen = 10

    rope = [[0,0] for _ in range(ropeLen)]
    tailPos.add(tuple(rope[-1]))

    for dir, size in data:
        for step in range(int(size)):
            rope[0][0] += dirs[dir][0]
            rope[0][1] += dirs[dir][1]
            for r in range(1, ropeLen):
                dx,dy = inRange(rope[r-1], rope[r])
                rope[r][0] += dx
                rope[r][1] += dy
            tailPos.add(tuple(rope[-1]))

    return len(tailPos)

print("Part 1: ", run(False, data))
print("Part 2: ", run(True, data))
