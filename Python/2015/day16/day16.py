## Parsing
files = ['input.txt', 'testInput.txt']
with open(files[0], 'r') as f:
    lines =  [a.strip() for a in f.readlines()]

aunts = []
def extractItem(item):
    thing = item[0:item.index(':')]
    cuant = item[item.index(':')+1:]
    
for i in lines:
    item1 = i[i.index(":")+2: i.index(",")]
    i = i[i.index(",")+1:]
    item2 = i[1: i.index(",")]
    i = i[i.index(",")+1:]
    item3 = i[1:]

    aunts.append(((item1[0:item1.index(':')],int(item1[item1.index(':')+1:])), \
    (item2[0:item2.index(':')],int(item2[item2.index(':')+1:])), \
    (item3[0:item3.index(':')],int(item3[item3.index(':')+1:]))))

remember = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, \
"akitas": 0, "vizslas": 0, "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1}

def hasItem(thing):
    item = thing[0]
    number = thing[1]
    if item == "cats" or item == "trees":
        return number > remember[item]
    elif item == "pomeranians" or item == "goldfish":
        return number < remember[item]
    else:
        return number == remember[item]

valids = []
for ind,i in enumerate(aunts):
    if hasItem(i[0]) and hasItem(i[1]) and hasItem(i[2]):
        print(ind+1)
