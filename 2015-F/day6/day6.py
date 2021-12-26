## Parsing
files = ['day6.txt', 'day6Test.txt']
with open(files[0], 'r') as f:
    lines =  f.readlines()

instructions = []
for i in lines:
    i.strip()
    single = []
    ##Instruction
    if i[0:6] == "toggle":
        single.append("toggle")
        indexStart = 7
    elif i[0:7] == "turn on":
        single.append("turn on")
        indexStart = 8
    else:
        single.append("turn off")
        indexStart = 9

    through = i.index("through")
    ##Start
    start = i[indexStart:through-1]
    indexComma = start.index(",")
    single.append((int(start[0: indexComma]), int(start[indexComma+1:])))
    ##End
    end = i[through+len("through")+1:-1]
    indexComma = end.index(",")
    single.append((int(end[0: indexComma]), int(end[indexComma+1:])))
    instructions.append(single)
##Setup
lights = []
for i in range(1000):
    line = []
    for j in range(1000):
        line.append(0)
    lights.append(line)

## Part 1
for inst in instructions:
    for i in range(inst[1][0], inst[2][0]+1):
        for j in range(inst[1][1], inst[2][1]+1):
            if inst[0] == "turn on":
                lights[i][j] += 1 #= True
            if inst[0] == "turn off":
                lights[i][j] -= 1 #= False
                if lights[i][j] < 0:
                    lights[i][j] = 0
            if inst[0] == "toggle":
                lights[i][j] += 2 #= not lights[i][j]

total = 0
for i in lights:
    for j in i:
        total += j
print(total)
