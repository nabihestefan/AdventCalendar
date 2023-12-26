files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f: lines =  [a.strip() for a in f.readlines()]

cardPKey = int(lines[0])
doorPKey = int(lines[1])
m = 20201227

val, loopSize = 1,0
while val != cardPKey:
    val = (val*7)%m
    loopSize += 1

print("Part 1: ", pow(doorPKey, loopSize, m))
