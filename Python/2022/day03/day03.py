files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    data = [x.strip() for x in f.readlines()]

def run(partTwo, data):
    total = 0
    if not partTwo:
        for i in data:
            char = str(set(i[0:(len(i)//2)]).intersection(set(i[(len(i)//2):])).pop())
            if char.islower(): total += ord(char) - ord("a") + 1
            else: total += ord(char) - ord("A") + 27
    else:
        for i in range(len(data)//3):
            char = str(set(data[(i*3)]).intersection(set(data[(i*3)+1]), set(data[(i*3)+2])).pop())
            if char.islower(): total += ord(char) - ord("a") + 1
            else: total += ord(char) - ord("A") + 27

    return total

print("Part 1: ", run(False, data))
print("Part 2: ", run(True, data))
