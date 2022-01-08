## Parsing
files = ['input.txt', 'testInput.txt']
with open(files[0], 'r') as f:
    lines =  [a.split() for a in f.readlines()]


trianglesPart1 = [(int(a[0]), int(a[1]), int(a[2])) for a in lines]
valid = 0

for triangle in trianglesPart1:
    if sum(triangle) - max(triangle) > max(triangle): valid += 1

print("PART1")
print(valid)

trianglesPart2 = []
i = 0
while i < len(lines):
    for j in range(len(lines[i])):
        trianglesPart2.append(
            (int(lines[i][j]), int(lines[i+1][j]), int(lines[i+2][j]))
        )
    i+=3
valid = 0

for triangle in trianglesPart2:
    if sum(triangle) - max(triangle) > max(triangle): valid += 1

print("PART1")
print(valid)
