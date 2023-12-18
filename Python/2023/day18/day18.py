files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    data = []
    dirs = {"0": "R", "1": "D", "2": "L", "3": "U"}
    for line in f.readlines():
        move, num, hex = line.strip().split(' ')
        data.append((move, int(num), dirs[hex[-2]], int(hex[2:-2], 16)))

def run(data, partTwo):
    pos = (0, 0)
    sum1, sum2 = 0,0
    edgeLen = 0
    for move, num, moveP2, numP2 in data:
        if partTwo: move, num = moveP2, numP2
        match move:
            case 'U': next = (pos[0]-num, pos[1])
            case 'D': next = (pos[0]+num, pos[1])
            case 'L': next = (pos[0], pos[1]-num)
            case 'R': next = (pos[0], pos[1]+num)
        sum1 += pos[0]*next[1]
        sum2 += pos[1]*next[0]
        edgeLen += int(num)
        pos = next

    return int((abs(sum1-sum2) + edgeLen) / 2 + 1)
               
print("Part 1: ", run(data, False))
print("Part 2: ", run(data, True))