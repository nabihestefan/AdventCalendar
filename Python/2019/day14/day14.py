files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f:
    lines =  [a.strip() for a in f.readlines()]

def parse(string):
    n,s = string.strip().split()
    return {"item":s, "amount":int(n)}

def ceil(a,b):
    return a//b + (a%b>0)


reactions = {}
for line in lines:
    inputStr,outputStr = line.split(" => ")
    inputs = [parse(input) for input in inputStr.split(",")]
    output = parse(outputStr)
    reactions[output["item"]] = {"parts":output["amount"], "ingredients":inputs}

def makeFUEL(reactions,amount):
    supply = {}
    orders = []
    orders.append({"item":"FUEL", "amount":amount})
    oreNeeded = 0

    while len(orders) > 0:
        order = orders.pop(0)
        if order["item"] == "ORE":
            oreNeeded += order["amount"]
        elif order["amount"] <= supply.get(order["item"],0):
            supply[order["item"]] -= order["amount"]
        else:
            needed = order["amount"] - supply.get(order["item"],0)
            reaction = reactions[order["item"]]
            batches = ceil(needed, reaction["parts"])
            for ingredient in reaction["ingredients"]:
                orders.append({"item":ingredient["item"], "amount":ingredient["amount"]*batches})
            leftover = batches*reaction["parts"] - needed
            supply[order["item"]] = leftover
    return oreNeeded

bottom = 1
top = float('inf')
oreNeeded = 1000000000000
while bottom+1 != top:
    if top == float('inf'):
        guess = bottom*2
    else:
        guess = (top+bottom)//2
    if makeFUEL(reactions,guess) > oreNeeded:
        top = guess
    else: bottom = guess


print("Part 1: ", makeFUEL(reactions,1))
print("Part 2: ", bottom)
