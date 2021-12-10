files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f:
    lines =  [a.strip() for a in f.readlines()]

score = 0
remover = []
for i in lines:
    line = ""
    for j in i:
        if j == "(":
            line += "("
        elif j == "[":
            line += "["
        elif j == "{":
            line += "{"
        elif j == "<":
            line += "<"

        elif j == ")":
            if line[-1] =="(":
                line = line[:-1]
            else:
                score += 3
                remover.append(i)
                break

        elif j == "]":
            if line[-1] =="[":
                line = line[:-1]
            else:
                score += 57
                remover.append(i)
                break

        elif j == "}":
            if line[-1] =="{":
                line = line[:-1]
            else:
                score += 1197
                remover.append(i)
                break

        elif j == ">":
            if line[-1] =="<":
                line = line[:-1]
            else:
                score += 25137
                remover.append(i)
                break



print("PART1")
print(score)

for i in remover:
    lines.remove(i)

scores = []
for i in lines:
    score = 0
    line = ""
    for j in i:
        if j == "(":
            line += "("
        elif j == "[":
            line += "["
        elif j == "{":
            line += "{"
        elif j == "<":
            line += "<"

        elif j == ")":
            line = line[:-1]

        elif j == "]":
            line = line[:-1]

        elif j == "}":
            line = line[:-1]

        elif j == ">":
            line = line[:-1]


    for j in reversed(range(len(line))):
        if line[j] == "(":
            score *= 5
            score += 1
        elif line[j] == "[":
            score *= 5
            score += 2
        elif line[j] == "{":
            score *= 5
            score += 3
        elif line[j] == "<":
            score *= 5
            score += 4
    scores.append(score)


scores.sort()
print("PART2")
print(scores[int(len(scores)/2)])
