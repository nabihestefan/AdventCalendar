files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f:
    lines =  [a.strip() for a in f.readlines()]

openers = ("(", "[", "{", "<")
closers = {")": ("(", 3), "]": ("[", 57), "}": ("{", 1197), ">": ("<", 25137)}


score = 0
remover = []
for i in lines:
    line = ""
    for j in i:
        if j in openers: line += j
        else:
            if line[-1] == closers[j][0]: line = line[:-1]
            else:
                score += closers[j][1]
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
        if j in openers: line += j
        else: line = line[:-1]


    for j in reversed(line):
        score *= 5
        score += openers.index(j)+1
    scores.append(score)


scores.sort()
print("PART2")
print(scores[int(len(scores)/2)])
