files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    data = [[c for c in x.strip()] for x in f.readlines()]

def tilt(data):
    moved = False
    for i in range(1, len(data)):
        for j in range(0, len(data[i])):
            if data[i][j] == "O" and data[i-1][j] == ".":
                data[i][j], data[i-1][j] = ".", "O"
                moved = True
    if moved: 
        data = tilt(data)
    return data

def run(data, partTwo):
    if not partTwo: data = tilt(data)
    else: 
        memory = dict()
        i = 0
        while i < 1000000000:
            memory[str(data)] = memory.get(str(data), []) + [i]
            if len(memory.get(str(data), [])) > 1:
                diff = memory[str(data)][-1] - memory[str(data)][-2]
                while i < 1000000000-diff: i += diff
            data = tilt(data) #N
            data = tilt(list(map(list, zip(*data[::-1])))) #W
            data = tilt(list(map(list, zip(*data[::-1])))) #S
            data = tilt(list(map(list, zip(*data[::-1]))))#E
            data = list(map(list, zip(*data[::-1])))
            i += 1

    return sum([data[i].count("O") * (len(data)-i) for i in range(0, len(data))])

print("Part 1: ", run(data, False))
print("Part 2: ", run(data, True))