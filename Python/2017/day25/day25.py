with open('input.txt', 'r') as f: lines =  [a.strip() for a in f.readlines()]

state = lines[0].split()[-1][:-1]
steps = int(lines[1].split()[-2])

instructions = dict()
i = 0
# Data Parsing
while i < len(lines):
    if "In state" in lines[i]:
        zero = dict()
        zero["W"] = lines[i+2].split()[-1][:-1] == "1"
        zero["M"] = lines[i+3].split()[-1][:-1] == "right"
        zero["N"] = lines[i+4].split()[-1][:-1]
        one = dict()
        one["W"] = lines[i+6].split()[-1][:-1] == "1"
        one["M"] = lines[i+7].split()[-1][:-1] == "right"
        one["N"] = lines[i+8].split()[-1][:-1]
        instructions[lines[i][-2]] = (zero, one)
        i += 9
    i += 1


def part1(state, steps, instructions):
    on = set()
    curInd = 0
    for step in range(steps):
        # Current value (either 0 or 1)
        cur = int(curInd in on)

        # Check what to write (and if it needs to change)
        if instructions[state][cur]["W"]:
            on.add(curInd)
        else:
            if cur == 1: on.remove(curInd)

        # Check where to move
        if instructions[state][cur]["M"]:
            curInd += 1
        else:
            curInd -= 1

        # Update state
        state = instructions[state][cur]["N"]

    return len(on)

print("Part 1: ", part1(state, steps, instructions))
