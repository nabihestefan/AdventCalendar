files = ['../input.txt', '../inputTest.txt']
with open(files[0], 'r') as f:
    data = [int(x) for x in f.readlines()]

def run(partTwo, data):
    return None


print("Part 1: ", run(False, data))
print("Part 2: ", run(True, data))
