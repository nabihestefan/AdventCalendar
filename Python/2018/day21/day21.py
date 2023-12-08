#decoding done in decode.txt and then paper
seen = set()
c = 0
lastC = -1
part1 = True
while True:
    a = c | 65536
    c = 12772194

    while True:
        c = (((c + (a & 255)) & 16777215) * 65899) & 16777215

        if 256 > a:
            if part1:
                print("Part 1: ", c)
                part1 = False
            if c not in seen:
                seen.add(c)
                lastC = c
                break
            else:
                print("Part 2: ", lastC)
                exit()
        else: a //= 256
