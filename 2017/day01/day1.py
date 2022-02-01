with open('input.txt', 'r') as f: lines =  [a.strip() for a in f.readlines()]

def run(num, part2):
    skip, pairs = len(num)//2, 0
    for i in range(len(num)):
        if part2: next = i+skip
        else: next = i+1

        if num[i] == num[next%len(num)]:
            pairs += int(num[i])
    return pairs


print("Part 1: ", run(lines[0], False))
print("Part 2: ", run(lines[0], True))
