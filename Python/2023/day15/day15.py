files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    data = f.read().strip().split(",") 

hash = lambda x, y: ((y + ord(x)) * 17) % 256

def p1(data):
    total = 0
    for i in data:
        val = 0
        for c in i: val = hash(c, val)
        total += val
    return total
            
def p2(data):
    boxes = [[] for i in range(256)]
    for i in data:
        box = 0
        label = ""
        index = 0
        while i[index] not in "=-":
            label += i[index]
            box = hash((i[index]), box)
            index += 1
        if i[index] == "-":
            for j, x in enumerate(boxes[box]):
                if x[0] == label: boxes[box].pop(j)
            continue
        if i[index] == "=":
            found = False
            for j, x in enumerate(boxes[box]):
                if x[0] == label:
                    found = True
                    boxes[box][j][1] = int(i[index+1:])
            if not found:
                boxes[box].append([label, int(i[index+1:])])
    
    total = 0
    for i, box in enumerate(boxes):
        for j, val in enumerate(box):
            total += (i+1) * (j+1) * val[1]
    return total

print("Part 1: ", p1(data))
print("Part 2: ", p2(data))