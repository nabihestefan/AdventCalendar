from collections import Counter
## Parsing
files = ['input.txt', 'testInput.txt']
with open(files[0], 'r') as f:
    lines =  [a.strip() for a in f.readlines()]

password1 = ""
password2 = ""
for i in range(len(lines[0])):
    dict = {}
    for j in lines:
        dict[j[i]] = dict.get(j[i], 0) + 1
    # print(dict)
    char1 = list(dict.keys())[list(dict.values()).index(max(list(dict.values())))]
    password1 += char1
    char2 = list(dict.keys())[list(dict.values()).index(min(list(dict.values())))]
    password2 += char2

print("PART1")
print(password1)

print("PART2")
print(password2)
