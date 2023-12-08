files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f:
    items =  [a[:-2].split(" (contains ") for a in f.readlines()]

cleaned_up = [[set(a[0].split(" ")), set(a[1].split(", "))] for a in items]
wordKey = dict()

for item in cleaned_up:
    for allergen in item[1]:
        if allergen in wordKey.keys():
            wordKey[allergen] = wordKey[allergen] & item[0]
        else:
            wordKey[allergen] = set(item[0])

invalid = set()
for key in wordKey:
    invalid = invalid | wordKey[key]

valid = 0
for item in cleaned_up:
    for ingredient in item[0]:
        if ingredient not in invalid: valid += 1

print("Part 1: ",valid)

finalAllegrens = {}
for i in wordKey: finalAllegrens[i] = "empty"

while "empty" in finalAllegrens.values():
    for key in wordKey:
        if len(wordKey[key]) == 1:
            word = wordKey[key].pop()
            finalAllegrens[key] = word
            wordKey.pop(key)
            for key in wordKey:
                if word in wordKey[key]: wordKey[key].remove(word)
            break

allergens = finalAllegrens.keys()
allergens.sort()
allergenWords = ""
for i in allergens:
    allergenWords += finalAllegrens[i]
    allergenWords += ","

print("Part 2: ", allergenWords[:-1])
