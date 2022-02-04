with open('input.txt', 'r') as f:
    lines =  [a.strip().split(" ") for a in f.readlines()]

def run(partTwo):
    for line in lines:
        if partTwo: line = ["".join(sorted(a)) for a in line]
        if len(line) == len(set(line)): yield 1

print("Part 1: ", sum(run(False)))
print("Part 2: ", sum(run(True)))
