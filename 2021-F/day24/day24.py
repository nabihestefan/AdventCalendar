#Used to extract the values of a, b, and c
lines = []
for line in open("input.txt"):
    lines.append((line[0:3], line[4:-1]))

a = []
b = []
c = []
for ind, i in enumerate(lines):
    print(ind)
    if (ind-4)%18 == 0:
        a.append(int(i[1][2:]))
    if (ind-5)%18 == 0:
        b.append(int(i[1][2:]))
    if (ind-15)%18 == 0:
        c.append(int(i[1][2:]))


print(a)
print(b)
print(c)
