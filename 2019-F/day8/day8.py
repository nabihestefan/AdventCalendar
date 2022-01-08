files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f:
    ints =  [int(a) for a in f.readlines()[0].strip()]



w = 25
h = 6
layers = []
i = 0
while i < len(ints):
    layer = []
    for r in range(h):
        row = []
        for c in range(w):
            row.append(ints[i])
            i+=1
        layer.append(row)
    layers.append(layer)

zeroes = []
for layer in layers:
    zero = 0
    for row in layer:
        for item in row:
            if item == 0: zero += 1
    zeroes.append(zero)

layer = layers[zeroes.index(min(zeroes))]
ones = 0
twos = 0
for row in layer:
    for item in row:
        if item == 1: ones += 1
        if item == 2: twos += 1

def valid(image):
    for row in image:
        if 2 in row: return False
    return True

image = layers[0]
l = 1
while not valid(image):
    for indi, i in enumerate(image):
        for indj, j in enumerate(i):
            if j == 2: image[indi][indj] = layers[l][indi][indj]
    l += 1

print("Part 1: ", ones*twos)
printImg = []
for row in image:
    r = []
    for item in row:
        if item == 1: r.append("#")
        else: r.append(" ")
    printImg.append(r)

print("Part 2: ")
for i in printImg:
    print("".join(i))
