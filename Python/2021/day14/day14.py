from copy import deepcopy
files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f:
    lines =  [a.strip() for a in f.readlines()]
    pairs = [(a[0:a.index("->")-1], a[a.index("->")+3:]) for a in lines[2:]]

def getDif(steps):
    dict = {}
    for i in range(len(lines[0])-1): dict[lines[0][i:i+2]] = dict.get(lines[0][i:i+2], 0) + 1
    for i in range(steps):
        nextDict = deepcopy(dict)
        for key in pairs:
            if key[0] in dict.keys():
                if dict[key[0]] > 0:
                    prev = key[0][0]+key[1]
                    next = key[1]+key[0][1]
                    nextDict[prev] = nextDict.get(prev, 0) + dict[key[0]]
                    nextDict[next] = nextDict.get(next, 0) + dict[key[0]]
                    nextDict[key[0]] -= dict[key[0]]
        dict = nextDict

    letters = {}
    for i in dict:
        letters[i[0]] = letters.get(i[0], 0) + dict[i]
        letters[i[1]] = letters.get(i[1], 0) + dict[i]

    letters[lines[0][0]] += 1
    letters[lines[0][-1]] += 1

    for i in letters: letters[i] //= 2

    listLetters = letters.values()
    return(max(listLetters) - min(listLetters))

print("PART1")
print(getDif(10))
print("PART2")
print(getDif(40))
