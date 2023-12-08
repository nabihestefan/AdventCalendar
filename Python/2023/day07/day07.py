files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    data = {x.strip().split()[0]:int(x.strip().split()[1]) for x in f.readlines()}

def getHandRank(hand, partTwo):
    if partTwo: cards = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']
    else: cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    ocur = {}
    ans = []
    for card in hand:
        ocur[card] = ocur.get(card, 0) + 1
        ans.append(cards.index(card))
    ocur = {k:v for k, v in sorted(ocur.items(), key=lambda x: x[1], reverse=True)}

    if partTwo:
        Js = ocur.pop("J" ,0)
        if not ocur: return [6]+ ans, hand
        ocur[ocur.keys()[0]] += Js

    if len(ocur.keys()) == 1: ans = [6]+ ans
    elif len(ocur.keys()) == 2:
        if ocur[ocur.keys()[0]] == 4: ans = [5] + ans
        else: ans = [4] + ans
    elif len(ocur.keys()) == 3:
        if ocur[ocur.keys()[0]] == 3: ans = [3] + ans
        else: ans = [2] + ans
    elif len(ocur.keys()) == 4: ans = [1] + ans
    else: ans = [0] + ans

    return ans, hand

def run(data, partTwo):
    total = 0
    hands = sorted([getHandRank(hand, partTwo) for hand in data], key = lambda x: (x[0][0], x[0][1], x[0][2], x[0][3], x[0][4], x[0][5]))
    for i in range(len(hands)):
        total += (i+1)* data[hands[i][1]]

    return total
            
print("Part 1: ", run(data, False))
print("Part 2: ", run(data, True))