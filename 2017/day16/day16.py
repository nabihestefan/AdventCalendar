with open('input.txt', 'r') as f: lines =  f.readlines()[0].strip().split(",")

programs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
def dance(programs):
    for i in lines:
        if i[0] == "s":
            rot = int(i[1:])
            programs = programs[-rot:] + programs[:-rot]

        elif i[0] == "x":
            a,b = map(int, i[1:].split("/"))
            programs[a], programs[b] = programs[b], programs[a]

        elif i[0] == "p":
            A,B = i[1:].split("/")
            a,b = programs.index(A), programs.index(B)
            programs[a], programs[b] = programs[b], programs[a]

    return programs

def part2(programs):
    original = programs[:]
    programs = dance(programs[:])
    step = 1
    while programs != original:
        programs = dance(programs[:])
        step += 1

    for j in range(1000000000%step):
        programs = dance(programs[:])

    return  "".join(programs)


print("Part 1: ", "".join(dance(programs[:])))
print("Part 2: ", part2(programs[:]))
