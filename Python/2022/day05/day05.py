files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    cratesText, data = [x for x in f.read().split("\n\n")]

    data = [x.split() for x in data.split("\n")]
    cratesText = [list(x) for x in cratesText.split("\n")]

def run(partTwo, cratesText, data):
    # This creates the map of crates, its inside the function because if I do 
    # it outside the order will be changed when Part 2 starts
    crates = []
    for i in range(int(cratesText[-1][-2])): crates.append([])

    for row in cratesText[:-1][::-1]:
        for ind, i in enumerate(row[1:][::4]):
            if i != " ": crates[ind].append(i)
            
    for i in data:
        quant, start, end = map(int, [i[1], i[3], i[5]])
        if not partTwo:
            for _ in range(quant): crates[end-1].append(crates[start-1].pop())
        else:
            crates[end-1] += crates[start-1][(-1*quant):] 
            crates[start-1] = crates[start-1][:(-1*quant)]

    return "".join(i[-1] for i in crates)


print("Part 1: ", run(False, cratesText, data))
print("Part 2: ", run(True, cratesText, data))
