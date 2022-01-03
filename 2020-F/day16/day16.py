from copy import deepcopy
files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f: lines =  [a.strip() for a in f.readlines()]

rules = {}
i = 0
while lines[i] != "":
    name = lines[i][:lines[i].index(":")]
    r1 = [int(a) for a in lines[i][lines[i].index(":")+2:lines[i].index(" or")].split("-")]
    r2 = [int(a) for a in lines[i][lines[i].index(" or")+4:].split("-")]
    rules[name] = (r1,r2)
    i+=1



nearby = False
otherTix = []
yourTix = []
while i < len(lines):
    if nearby == True:
        otherTix.append([int(a) for a in lines[i].split(",")])
    if lines[i] == "your ticket:":
        i+=1
        yourTix = [int(a) for a in lines[i].split(",")]
    elif lines[i] == "nearby tickets:":
        nearby = True
    i+=1

tixError = 0
invalid = []
for tix in otherTix:
    for value in tix:
        valid = False
        for key in rules.keys():
            rule = rules[key]
            func = lambda x: (rule[0][0]<=x and x<=rule[0][1]) or (rule[1][0]<=x and x<= rule[1][1])
            valid = valid or func(value)
        if not valid:
            if tix not in invalid:
                invalid.append(tix)
            tixError += value

for i in invalid:
    otherTix.remove(i)

cand = {}
found = {}
for key in rules.keys():
    rule = rules[key]
    func = lambda x: (rule[0][0]<=x and x<=rule[0][1]) or (rule[1][0]<=x and x<= rule[1][1])
    cand[key] = []
    found[key] = -1
    for ind in range(len(yourTix)):
        works = True
        for tix in otherTix:
            works = works and func(tix[ind])
        if works:
            cand[key].append(ind)

while -1 in found.values():
    for key in cand.keys():
        if len(cand[key]) == 1:
            found[key] = cand[key][0]
            for k in cand.keys():
                if found[key] in cand[k]:
                    cand[k].remove(found[key])


dep = 1
for key in found.keys():
    if "departure" in key:
        dep *= yourTix[found[key]]

print("Part 1: ", tixError)
print("Part 2: ", dep)
