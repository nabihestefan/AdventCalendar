with open('input.txt', 'r') as f: num = int(f.readlines()[0].strip())

def part1():
    buffer = [0]
    curpos = 0
    for i in range(1,2018):
        curpos = (curpos + num) % i + 1
        buffer.insert(curpos, i)
    return buffer[curpos+1]

def part2():
    curpos = 0
    for i in range(1,50000001):
        curpos = (curpos + num) % i + 1
        if curpos == 1: ans = i
    return ans

print("Part 1: ", part1())
print("Part 2: ", part2())
