## Parsing
files = ['input.txt', 'testInput.txt']
with open(files[0], 'r') as f:
    blocked = []
    for i in f.readlines():
        low,high = map(int, i.split("-"))
        blocked.append((lambda x: x < low or x > high, low, high))

maxIP = 4294967295
ip = 0
works = set()
while True and ip <= maxIP:
    valid = True
    for func,low,high in blocked:
        valid = valid and func(ip)
        if not valid:
            ip = high+1
            break
    if valid:
        works.add(ip)
        ip += 1


print("Part 1: ", min(works))
print("Part 1: ", len(works))
