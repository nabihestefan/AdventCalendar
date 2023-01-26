files = ['input.txt', 'inputTest.txt']
## Parsing
rules = {}
with open(files[0], 'r') as f:
    for line in f:
        line = line.split(" bags contain ")
        line[1] = line[1].split(",")
        bags = []
        for bag in line[1]:
            bags.append(bag.strip(" ").split(" "))
        cBags = []
        for bag in bags:
            if "other" in bag: cBags.append("None")
            else: cBags.append((bag[1] + " " + bag[2], int(bag[0])))
            rules[line[0]] = cBags

bags = ["shiny gold"]
for bag in bags:
    for rule in rules:
        for tup in rules[rule]:
            if bag == tup[0]:
                if rule not in bags:
                    bags.append(rule)
print("Part 1: ", len(bags)-1)


bags = ["shiny gold"]
for bag in bags:
    for tup in rules[bag]:
        if tup != "None":
            for i in range(tup[1]):
                bags.append(tup[0])
print("Part 2: ", len(bags)-1)
