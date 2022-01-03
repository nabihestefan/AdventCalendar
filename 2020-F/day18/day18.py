files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f:
    preLines = [a.strip().split(" ") for a in f.readlines()]

lines = []
for line in preLines:
    newline = []
    for i in line:
        while "(" in i:
            newline.append("(")
            i = i[1:]
        back = []
        while ")" in i:
            back.append(")")
            i = i[:-1]
        newline.append(i)
        for j in back: newline.append(j )
    lines.append(newline)

def evalPt1(line):
    while "+" in line or "*" in line or "(" in line:
        # Recursive ()
        if "(" in line:
            start = line.index("(")
            end = start+1
            level = 1
            while True:
                if line[end] == ")" and level == 1:break
                if line[end] == "(": level += 1
                if line[end] == ")": level -= 1
                end += 1
            line = line[:start] + [str(evalPt1(line[start+1:end]))] + line[end+1:]
        else:
            if line[1] == "+":
                line = [str(int(line[0]) + int(line[2]))] + line[3:]
            elif line[1] == "*":
                line = [str(int(line[0]) * int(line[2]))] + line[3:]

    return int(line[0])

def evalPt2(line):
    while "+" in line or "*" in line or "(" in line:
        # Recursive ()
        if "(" in line:
            start = line.index("(")
            end = start+1
            level = 1
            while True:
                if line[end] == ")" and level == 1:break
                if line[end] == "(": level += 1
                if line[end] == ")": level -= 1
                end += 1
            line = line[:start] + [str(evalPt2(line[start+1:end]))] + line[end+1:]
        else:
            if "+" in line:
                i = line.index("+")
                line = line[:i-1] + [str(int(line[i-1]) + int(line[i+1]))] + line[i+2:]
            elif line[1] == "*":
                line = [str(int(line[0]) * int(line[2]))] + line[3:]

    return int(line[0])

sumPt1 = 0
sumPt2 = 0
for line in lines:
    result = evalPt1(line)
    sumPt1 += result
    result = evalPt2(line)
    sumPt2 += result

print("Part 1: ", sumPt1)
print("Part 2: ", sumPt2)
