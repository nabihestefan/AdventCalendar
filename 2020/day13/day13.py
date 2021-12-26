files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f: lines =  [a.strip() for a in f.readlines()]

earliest = int(lines[0])
buses = []
for ind, a in enumerate(lines[1].split(",")):
    if a != "x": buses.append((int(a),ind))

def part1(earliest, buses):
    leave = earliest
    while True:
        for i in buses:
            if leave%int(i[0]) == 0:
                return (leave-earliest)*int(i[0])
        leave += 1

def part2(buses):
    delay = 1
    time = 0
    for bus, offset in buses:
        while True:
            time += delay
            if (time+offset)%bus == 0:
                delay *= bus
                break

    return time

print("Part 1: ", part1(earliest, buses))
print("Part 2: ", part2(buses))
