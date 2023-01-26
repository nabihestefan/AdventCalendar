with open('input.txt', 'r') as f: lines =  [a.strip() for a in f.readlines()]

# Mersenne Numbers!!
def run(part2):
    A = int(lines[0].split()[-1])
    B = int(lines[1].split()[-1])
    AFactor, BFactor, divider = 16807, 48271, 2**31-1
    matches = 0
    for i in range(40000000 if not part2 else 5000000):
        print(i)
        while True:
            A = ((A*AFactor) & divider) + ((A*AFactor) >> 31)
            if not part2 or A % 4 == 0: break

        while True:
            B = ((B*BFactor) & divider) + ((B*BFactor) >> 31)
            if not part2 or B % 8 == 0: break

        if A&0xFFFF == B&0xFFFF: matches += 1

    return matches

print("Part 1: ", run(False))
print("Part 2: ", run(True))
