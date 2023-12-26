files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f:
    players =  f.read().split("\n\n")

def parsePlayer(player):
    cards = []
    for i in player.splitlines()[1:]: cards.append(int(i.strip()))
    return cards

def getScore(player):
    sum = 0
    i = 1
    for card in player[::-1]:
        sum += card*i
        i += 1
    return sum

def recursiveCombat(p1, p2):
    played = {1:[], 2:[]}
    winner = None
    while len(p1) > 0 and len(p2) > 0:
        if p1 in played[1] and p2 in played[2]: return True, p1, p2
        played[1].append(p1[:])
        played[2].append(p2[:])
        c1 = p1.pop(0)
        c2 = p2.pop(0)
        if c1 <= len(p1) and c2 <= len(p2):
            winnerRound = recursiveCombat(p1[:c1],p2[:c2])[0]
        else: winnerRound = c1 > c2
        if winnerRound: p1.extend([c1,c2])
        else: p2.extend([c2,c1])

    return (len(p1) != 0, p1, p2)



p1 = parsePlayer(players[0])
p2 = parsePlayer(players[1])
copyp1 = p1[:]
copyp2 = p2[:]
while len(p1) > 0 and len(p2) > 0:
    c1 = p1.pop(0)
    c2 = p2.pop(0)
    if c1 > c2: p1.extend([c1,c2])
    elif c1 < c2: p2.extend([c2,c1])

if len(p1) == 0: print("Part 1: ", getScore(p2))
else:  print("Part 1: ", getScore(p1))


winner, p1, p2 = recursiveCombat(copyp1,copyp2)

if winner: print("Part 2: ", getScore(p1))
else:  print("Part 2: ", getScore(p2))
