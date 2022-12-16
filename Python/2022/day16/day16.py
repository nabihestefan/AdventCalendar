files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    data = [x.strip() for x in f.readlines()]

rates = dict()
tunnels = dict()
for i in data:
    name = i[6:8].strip()
    rate = int(i[i.index("=")+1: i.index(";")])
    tunnel = i[i.index("valve")+6:].replace(" ", "").split(",")
    rates[name] = rate
    tunnels[name] = tunnel
    
def findPaths(rates, tunnels, curr, paths, opened):
    options = []
    # Move to next
    for next in tunnels[curr]:
        options.append((paths + [next], opened.copy()))

    # Open Current
    if rates[curr] > 0 and curr not in opened:
        options.append((paths, opened | {curr}))

    return options

def run(partTwo, rates, tunnels, start):
    if not partTwo:
        data = [(0, ([start], []), set())]
    else:
        data = [(0, ([start], [start]), set())]

    time = 31 if not partTwo else 27
    for i in range(1,time):
        if i > 7:
            # Keep top 500000 just to make the data remotely manageable
            # Other inputs might need more or less data kept to work
            # Just found this is a reasonable compromise between consistency and runtime
            data.sort(reverse=True)
            data = data[:500000]
        newData = []
        for pressure, paths, opened in data:
            curr = paths[0][-1]
            if partTwo:
                elephant = paths[1][-1]

            pressure += sum(rates[p] for p in opened)
        
            for newPath, newOpened in findPaths(rates, tunnels, curr, paths[0], opened):
                if not partTwo:
                    newData.append((pressure, (newPath, []), newOpened))
                else: 
                    for pathElephant, openedElephant, in findPaths(rates, tunnels, elephant, paths[1], newOpened):
                        newData.append((pressure, (newPath, pathElephant), openedElephant))

        data = newData
    return max(data)[0]

# print("Part 1: ", run(False, rates, tunnels, "AA"))
print("Part 2: ", run(True, rates, tunnels, "AA"))
