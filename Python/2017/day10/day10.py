with open('input.txt', 'r') as f: lines = f.readlines()[0].strip()

def reverse(values, pointer, length):
    shifted = values[pointer:] + values[:pointer]
    shifted = shifted[:length][::-1] + shifted[length:]
    return shifted[-pointer:] + shifted[:-pointer]

def part1():
    nums =  map(int,lines.split(","))
    values = list(range(256))
    pos = skip = 0

    for length in nums:
        values = reverse(values, pos, length)
        pos = (pos + length + skip) % len(values)
        skip += 1
    return values[0] * values[1]

def part2():
    nums = list(map(ord, lines)) + [17, 31, 73, 47, 23]
    skip = pos = 0
    values = list(range(256))

    for _ in range(64):
        for length in nums:
            values = reverse(values, pos, length)
            pos = (pos + length + skip) % len(values)
            skip += 1

    dense = ""
    for i in range(16):
        num = 0
        for j in range(16): num ^= values[i*16 + j]
        dense += hex(num)[2:].zfill(2)

    return dense

print("Part 1: ", part1())
print("Part 2: ", part2())
