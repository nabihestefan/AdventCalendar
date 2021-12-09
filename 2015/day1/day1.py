
## Parsing
with open('day1.txt', 'r') as f:
    lines =  f.readlines()[0]

total = 0
for i in range(len(lines)):
    if total == -1:
        print(i)
        break
    if lines[i] == "(":
        total += 1
    if lines[i] == ")":
        total -= 1

print(total)
