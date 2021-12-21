from copy import deepcopy
files = ['input.txt', 'inputTest.txt']
## Parsing
lines = []
for line in open(files[0]):
    lines.append(line.strip())

algorithm = lines[0]
extender = 100
screen = []
empty = []
for i in range(len(lines[2])+extender*2):
    empty.append(".")

for i in range(extender):
    screen.append(deepcopy(empty))
for line in lines[2:]:
    splitter = []

    for i in range(extender):
        splitter.append(".")

    for char in line:
        splitter.append(char)

    for i in range(extender):
        splitter.append(".")

    screen.append(splitter)

for i in range(extender):
    screen.append(deepcopy(empty))

def enhance(algorithm, image):
    newImage = deepcopy(image)
    for i in range(len(image)):
        for j in range(len(image[0])):
            if i in [0, len(image)-1] or j in [0, len(image[0])-1]:
                newImage[i][j] = "#" if image[i][j] == "." else "."
            else:
                num = ""
                num += "0" if image[i-1][j-1] == "." else "1"
                num += "0" if image[i-1][j] == "." else "1"
                num += "0" if image[i-1][j+1] == "." else "1"
                num += "0" if image[i][j-1] == "." else "1"
                num += "0" if image[i][j] == "." else "1"
                num += "0" if image[i][j+1] == "." else "1"
                num += "0" if image[i+1][j-1] == "." else "1"
                num += "0" if image[i+1][j] == "." else "1"
                num += "0" if image[i+1][j+1] == "." else "1"
                index = int(num, 2)
                newImage[i][j] = algorithm[index]
    return newImage


def run(times, screen):
    for i in range(times):
        screen = enhance(algorithm, screen)

    on = 0
    for i in screen:
        for j in i:
            if j == "#": on += 1
    return on

print("Part 1: ", run(2, screen))
print("Part 2: ", run(50, screen))
