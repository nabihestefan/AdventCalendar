## Parsing
files = ['day5.txt', 'day5Test.txt']
with open(files[0], 'r') as f:
    lines =  f.readlines()

total = 0
##Part1
banned = ['ab', 'cd', 'pq', 'xy']
vowels = "aeiou"

for i in lines:
    naughty = True

    vow = 0
    for v in vowels:
        vow += i.count(v)

    double = False
    for j in range(len(i)-1):
        if i[j] == i[j+1]:
            double = True

    if double and (vow>=3):
        naughty = False

    for j in banned:
        if j in i:
            naughty = True
    if not naughty:
        total += 1

print("Part 1: ", total)

total = 0

##Part 2
for i in lines:
    naughty = True
    repeater = False
    pair = False

    if len(i) >= 4:
        for j in range(len(i)-3):
            for k in range(j+2,len(i)-1):
                if i[j:j+2] == i[k:k+2]:
                    pair = True


    for j in range(len(i)-2):
        if i[j] == i[j+2]:
            repeater = True

    if repeater and pair:
        naughty = False


    if not naughty:
        total += 1

print("Part 2: ", total)
