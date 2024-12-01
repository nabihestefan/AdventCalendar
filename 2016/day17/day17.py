from hashlib import md5
## Parsing
files = ['input.txt', 'testInput.txt']
with open(files[0], 'r') as f:
    data =  f.readlines()[0].strip()

def getMD5(data):
    return md5(data.encode()).hexdigest()[:4]

inRange = lambda p: 0<=p.real<=3 and 0<=p.imag<=3
dirs = {0:-1j, 1:+1j, 2:-1, 3:+1}
dirsChar = {0:"U", 1:"D", 2:"L", 3:"R"}
paths = []

def run(pos, goal, moves, data):
    if pos == goal:
        paths.append(moves)
        return True
    next = getMD5(data+moves)
    for i,c in enumerate(next):
        nextPos = pos + dirs[i]
        if inRange(nextPos) and c in "bcdef":
            run(nextPos, goal, moves+dirsChar[i], data)

run(0, 3+3j, "", data)
print("Part 1: ", min(paths, key=len))
print("Part 2: ", len(max(paths, key=len)))
