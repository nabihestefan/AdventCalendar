## Parsing
files = ['input.txt', 'testInput.txt']
with open(files[0], 'r') as f:
    rooms = [(a[0:a.index("[")-4].replace("-", ""),a[a.index("[")-3:a.index("[")],a[a.index("[")+1:a.index("]")]) for a in f.readlines()]


def isReal(room):
    name = "".join(sorted(room[0]))
    id = room[1]
    check = room[2]
    dict = {}

    for i in name:
        dict[i] = dict.get(i, 0) + 1
    maxed = []
    while True:
        maxed.append(max(dict, key=dict.get))
        dict[max(dict, key=dict.get)] = -1
        if len(maxed) >= 5:
            break
    if "".join(maxed) == check:
        return True

total = 0
valid = []
for i in rooms:
    if isReal(i):
        total += int(i[1])
        valid.append((i[0], i[1]))

def decrypt(text,s):
    result = ""

    for i in range(len(text)):
        result += chr((ord(text[i]) + (1*s) - 97) % 26 + 97)

    return result


solved = []
for i in valid:
    solved.append((decrypt(i[0],int(i[1])), i[1]))

print("PART1")
print(total)
print("PART2")
for i in solved :
    if "northpole" in i[0]:
        print(i[1])
