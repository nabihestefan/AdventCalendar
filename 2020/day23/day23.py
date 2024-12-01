files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f:
    cups = [int(a) for a in f.read().strip()]

def fastRun(cups, moves):
    current = cups[0]
    mn, mx = min(cups), max(cups)
    clock = dict(zip(cups, cups[1:] + [cups[0]]))
    for _ in range(moves):
        picked = [clock[current]]
        picked.append(clock[picked[0]])
        picked.append(clock[picked[-1]])
        dest = current - 1
        while dest < mn or dest in picked:
            dest-=1
            if dest < mn: dest = mx
        clock[current] = clock[picked[2]]
        clock[picked[2]] = clock[dest]
        clock[dest] = picked[0]
        current = clock[current]

    return clock


cupsP1 = fastRun(cups,10)
order = [cupsP1[1]]
while order[-1] != 1:
    order.append(cupsP1[order[-1]])

cups

cupsP2 = fastRun(cups+list(range(10, 1000001)),10000000)
c1 = cupsP2[1]
c2 = cupsP2[c1]

print("Part 1: ", "".join([str(a) for a in order[:-1]]))
print("Part 2: ", c1*c2)
