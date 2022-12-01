## Parsing
files = ['input.txt', 'testInput.txt']
with open(files[0], 'r') as f:
    lines =  [a.strip() for a in f.readlines()]

reindeer = []
for i in lines:
    name = i[0:i.index(" ")]
    speed = i[i.index("fly")+4: i.index("km/s")-1]
    time = i[i.index("km/s")+9: i.index("seconds,")-1]
    rest = i[i.index("rest for")+8: i.index("seconds.")-1]
    #Name, speed, run_time, rest_time, counter, flying, distance, score
    reindeer.append([name, int(speed), int(time), int(rest), int(time), True, 0, 0])

for i in reindeer:
    print(i)

for i in range(2503):
    print()
    print(i)
    j = 0
    while j < len(reindeer):
        if reindeer[j][4] > 0:
            reindeer[j][4] -= 1
        else:
            if reindeer[j][5]:
                reindeer[j][5] = False
                reindeer[j][4] = reindeer[j][3]-1
            else:
                reindeer[j][5] = True
                reindeer[j][4] = reindeer[j][2]-1
        if reindeer[j][5]:
            reindeer[j][6] += reindeer[j][1]
        j += 1
# Part 2
    winning = 0
    for k in reindeer:
        if k[6] > winning:
            winning = k[6]
    k = 0
    print(winning)
    while k in range(len(reindeer)):
        if reindeer[k][6] == winning:
            reindeer[k][7] += 1
            print(reindeer[k][0])
        k += 1

for i in reindeer:
    print(i)
