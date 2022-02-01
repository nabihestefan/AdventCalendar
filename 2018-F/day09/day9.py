#Only importing cause running without is too long
from collections import deque, defaultdict
files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f:
    words = f.readlines()[0].strip().split()
    players = int(words[0])
    marbles = int(words[6])

# No libraries, take 5+ minutes to run
def OGrun(marbles):
    scores = {}
    circle = [0]
    for marble in range(1, marbles+1):
        print(marble, marbles)
        if marble%23 == 0:
            circle = circle[-7:] + circle[:-7]
            scores[marble%players] = scores.get(marble%players, 0) + marble + circle.pop()
            circle = circle[1:] + circle[:1]
        else:
            circle = circle[1:] + circle[:1]
            circle.append(marble)
    return max(scores.values())

#libraries, takes ~2 secs to run
def run(marbles):
    scores = defaultdict(int)
    circle = deque([0])
    for marble in range(1, marbles+1):
        if marble%23 == 0:
            circle.rotate(7)
            scores[marble%players] += marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)
    return max(scores.values())

print("Part 1: ", run(marbles))
print("Part 2: ", run(marbles*100))
