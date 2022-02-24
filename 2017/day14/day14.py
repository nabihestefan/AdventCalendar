with open('input.txt', 'r') as f: hash =  f.readlines()[0].strip()

#Copied from day 10
def reverse(values, pointer, length):
    shifted = values[pointer:] + values[:pointer]
    shifted = shifted[:length][::-1] + shifted[length:]
    return shifted[-pointer:] + shifted[:-pointer]

#Copied from day 10
def knothash(word):
    nums = list(map(ord, word)) + [17, 31, 73, 47, 23]
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
        dense += hex(num)[2:] if len(hex(num)) == 4 else "0" + hex(num)[2:]

    knothash = ""
    for i in dense: knothash += bin(int(i,base=16))[2:].zfill(4)
    return knothash

def adjacent(x,y):
    squares.remove((x,y))
    for dx,dy in [(1,0), (0,1), (-1,0), (0,-1)]:
        if (x+dx, y+dy) in squares: adjacent(x+dx, y+dy)
    return 1

squares = []
def run():
    for i in range(128):
        khash = knothash(hash + "-" + str(i))
        for ind, c in enumerate(khash):
            if c == "1": squares.append((i,ind))

    p1 = len(squares)
    regions = 0
    while squares: regions += adjacent(squares[0][0], squares[0][1])

    return p1, regions




print("Part 1&2: ", run())
