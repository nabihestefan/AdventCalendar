files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    data = [x for x in f.readlines()]

pairs = []
for i in data:
    sensor, beacon = i.split(": ")
    sensex = int(sensor[sensor.index("x=")+2:sensor.index(",")])
    sensey = int(sensor[sensor.index("y=")+2:])
    beaconx = int(beacon[beacon.index("x=")+2:beacon.index(",")])
    beacony = int(beacon[beacon.index("y=")+2:])
    pairs.append([(sensex,sensey), (beaconx, beacony)])

def part1(pairs):
    empty = set()
    for sensor, beacon in pairs:
        sx, sy = sensor
        bx, by = beacon
        dist = abs(bx-sx) + abs(by-sy)
        if 2000000 in range(sy-dist, sy+dist+1):
            y = 2000000
            yDif = abs(abs(sy-y) - dist)
            for x in range(sx-yDif, sx+yDif+1):
                if (x,y) != beacon and (x,y) != sensor:
                    empty.add((x,y))

    return len(empty)

def part2(pairs):
    # Non z3 solutions, runs too long
    pairs = sorted(pairs, key=lambda x: x[0][0])
    x,y = 0,0
    while y < 4000000:
        x = 0
        while x < 4000000:
            answer = True
            for sensor, beacon in pairs:
                sx, sy = sensor
                bx, by = beacon
                dist = abs(bx-sx) + abs(by-sy)
                if (abs(sx-x) + abs(sy-y) <= dist):
                    answer = False
                    x = sx + dist - abs(sy-y)
                    break
            if answer:
                print(x,y)
                return x * 4000000 + y
            x += 1
        y += 1
    
print("Part 1: ", part1(pairs))
print("Part 2: ", part2(pairs))
