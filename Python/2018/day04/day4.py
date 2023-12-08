files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f:
    lines =  [a.strip() for a in f.readlines()]

def parseLine(lines):
    id = int(lines[0][lines[0].index("#")+1:lines[0].index("begins")])

    month = int(lines[0][lines[0].index("1518-")+5:lines[0].index("1518-")+7])
    day = int(lines[0][lines[0].index("1518-")+8:lines[0].index("1518-")+10])
    date = (month,day)

    sleep = set()
    asleep = False
    ind = 1
    for i in range(60):
        if ind < len(lines) and i ==  int(lines[ind][lines[ind].index(":")+1:lines[ind].index("]")]):
            asleep = not asleep
            ind += 1
        if asleep: sleep.add(i)

    return id, date, sleep

guards = {}
lines.sort()
day = [lines[0]]
for line in lines[1:]:
    if "begins shift" in line:
        id, date, sleep = parseLine(day)
        l = guards.get(id,[])
        l.append((id,sleep))
        guards[id] = l
        day = [line]
    else: day.append(line)

id, date, sleep = parseLine(day)
l = guards.get(id,[])
l.append((id,sleep))
guards[id] = l

sleepiest = (-1,-1)
for guard in guards:
    totalSleep = 0
    for day in guards[guard]:totalSleep += len(day[1])
    if totalSleep > sleepiest[1]: sleepiest = (guard, totalSleep)

def sleepiestMin(guards, id):
    sleepDict = {}
    for day in guards[id]:
        for min in day[1]: sleepDict[min] = sleepDict.get(min, 0) + 1
    if bool(sleepDict):
        min = max(sleepDict, key=sleepDict.get)
        return min, sleepDict[min]
    else:
        return -1,-1

sleepSingle = (-1,-1,-1)
for guard in guards:
    min, amount = sleepiestMin(guards,guard)
    print(max(amount,sleepSingle[2]))
    if amount > sleepSingle[2]:
        sleepSingle = (guard,min,amount)
        print(sleepSingle)


print("Part 1: ", sleepiest[0]*sleepiestMin(guards, sleepiest[0])[0])
print("Part 2: ", sleepSingle[0]*sleepSingle[1])
