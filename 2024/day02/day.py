files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    data = [map(int, x.strip().split(" ")) for x in f.readlines()]

def is_safe(line):
    increasing = True if (line[0] - line[1] < 0) else False
    for i in range(len(line)-1):
            cur = line[i]
            nxt = line[i+1]
            if (increasing and cur > nxt) or (not increasing and cur < nxt):
                return False
            if abs(cur-nxt) < 1 or 3 < abs(cur-nxt):
                return False
    return True

def run(data, partTwo=False):
    levelSafe = 0
    for i in data:
        if is_safe(i): levelSafe += 1
        elif partTwo:
             for idx in range(len(i)):
                if is_safe(i[:idx] + i[idx+1:]):
                    levelSafe += 1
                    break
    return levelSafe
    
print("Part 1: ", run(data))
print("Part 2: ", run(data, True))