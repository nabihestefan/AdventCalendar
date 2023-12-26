files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    lines = [x.strip() for x in f.readlines()]

data = []
for line in lines:
    winning, mine = line.split(":")[1].split("|")
    data.append(len(set(winning.split()).intersection(set(mine.split()))))
    
def run(data):
    p1 = 0
    myCards = {}
    for i, card in enumerate(data):
        myCards[i] = myCards.get(i, 0) + 1
        if card > 0: p1 += 2**(card-1)
        for j in range(1, min(card, len(data))+1):
            myCards[i+j] = myCards.get(i+j, 0) + myCards[i]

    return p1, sum(myCards[key] for key in myCards.keys())
    
print("Part 1 & 2: ", run(data))