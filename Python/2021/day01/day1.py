with open('day1.txt') as f:
    measurements = [int(x) for x in f.readlines()]

def part1():
    increases = 0
    for i in range(1,len(measurements)):
        if measurements[i-1] < measurements[i]: increases += 1
    return increases


def run(partTwo):
    increases = 0
    trios = []
    if measurements[0] < measurements[1]: increases += 1
    for i in range(2,len(measurements)):
        if measurements[i-1] < measurements[i]: increases += 1
        trios.append(measurements[i-2]+measurements[i-1]+measurements[i])

    if not partTwo: return increases
    increases = 0

    for i in range(1,len(trios)):
        if trios[i-1] < trios[i]: increases += 1
    return increases


print("Part 1: ", run(False))
print("Part 2: ", run(True))
