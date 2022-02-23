scanners = dict()
with open('input.txt', 'r') as f:
    for i in f.readlines():
        line, depth = map(int, i.split(":"))
        scanners[line] = depth

def part1():
    caught = 0
    for key in scanners:
        if key % ((scanners[key]-1)*2) == 0: caught += key*scanners[key]
    return caught
    # return sum(key*scanners[key] for key in scanners if key % ((scanners[key]-1)*2) == 0)

def part2():
    pos = -1
    caught = True
    while caught:
        pos += 1
        caught = False
        for key in scanners:
            if (key+pos) % ((scanners[key]-1)*2) == 0:
                caught = True
                break
    return pos

print("Part 1: ", part1())
print("Part 2: ", part2())
