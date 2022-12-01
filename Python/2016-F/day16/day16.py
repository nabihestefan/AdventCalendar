## Parsing
files = ['input.txt', 'testInput.txt']
with open(files[0], 'r') as f:
    data =  f.readlines()[0].strip()

def expandData(data, diskLen):
    while len(data) < diskLen:
        data = data[:]+"0"+''.join('1' if x == '0' else '0' for x in data[::-1])
    return data[:diskLen]

def makeChecksum(data):
    for char in data: yield "1" if char == next(data) else "0"

def run(data, diskLen):
    data = expandData(data[:], diskLen)
    checksum = "".join(makeChecksum(iter(data)))
    while len(checksum)%2 == 0: checksum = "".join(makeChecksum(iter(checksum)))
    return checksum

print("Part 1: ", run(data[:], 272))
print("Part 2: ", run(data[:], 35651584))
