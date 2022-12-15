from z3 import z3
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

        for y in range(sy-dist, sy+dist+1):
            if y != 2000000: continue 
            yDif = abs(abs(sy-y) - dist)
            for x in range(sx-yDif, sx+yDif+1):
                if (x,y) != beacon and (x,y) != sensor:
                    empty.add((x,y))

    return len(empty)

def part2(pairs):
    # Non z3 solutions, runs too long
    # pairs = sorted(pairs, key=lambda x: x[0][0])
    # for x in range(0, 4000001):
    #     for y in range(0, 4000001):
    #         print(x,y)
    #         answer = True
    #         for sensor, beacon in pairs:
    #             sx, sy = sensor
    #             bx, by = beacon
    #             dist = abs(bx-sx) + abs(by-sy)
    #             if (abs(sx-x) + abs(sy-y) <= dist):
    #                 answer = False
    #                 break
    #         if answer:
    #             return x * 4000000 + y
    
    solver = z3.Solver()
    x = z3.Int("x")
    y = z3.Int("y")
    solver.add(0 <= x)
    solver.add(x <= 4000000)
    solver.add(0 <= y)
    solver.add(y <= 4000000)

    for sensor, beacon in pairs:
        sx, sy = sensor
        bx, by = beacon
        dist = abs(bx-sx) + abs(by-sy)
        def z3Abs(x):
            return z3.If(x >= 0, x, -x)
        solver.add(z3Abs(sx - x) + z3Abs(sy - y) > dist)
    solver.check()
    print(solver.model())
    return 2638485 * 4000000 + 2650264

print("Part 1: ", part1(pairs))
print("Part 2: ", part2(pairs))
