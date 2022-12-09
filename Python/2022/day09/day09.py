files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    data = [x.split() for x in f.readlines()]

# dirs = {"R": (0,1), "L":(0,-1), "U": (1,0), "D":(-1,0)}
dirs = {"R": 0+1j, "L":0-1j, "U": 1, "D":-1}

def inRange(head,tail):
    movement = 0 + 0j
    dif = head-tail

    if abs(dif.real)>1:
        if dif.imag != 0: movement += complex(0, (dif.imag/abs(dif.imag)))
        movement += (dif.real/abs(dif.real))
    elif abs(dif.imag)>1:
        if dif.real != 0: movement += (dif.real/abs(dif.real))
        movement += complex(0, (dif.imag/abs(dif.imag)))

    return movement
    
def run(partTwo, data):
    tailPos = set()
    if not partTwo: ropeLen = 2
    else: ropeLen = 10

    rope = [complex() for _ in range(ropeLen)]
    tailPos.add(rope[-1])

    for dir, size in data:
        for step in range(int(size)):
            rope[0] += dirs[dir]
            for r in range(1, ropeLen):
                rope[r] += inRange(rope[r-1], rope[r])
            tailPos.add(rope[-1])
    return len(tailPos)

print("Part 1: ", run(False, data))
print("Part 2: ", run(True, data))
