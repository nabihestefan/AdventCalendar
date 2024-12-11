files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    data = map(int, f.read().split(" "))

stones = dict()
for s in data: stones[s] = stones.get(s, 0) + 1

def nextState(stones):
    newStones = dict()
    for s in stones:
        if s == 0: moves = [1]
        elif len(str(s))%2 == 0:  moves = [int(str(s)[0:len(str(s))//2]), int(str(s)[len(str(s))//2:])]
        else: moves = [s*2024]
        for nextStones in moves:
            newStones[nextStones] = newStones.get(nextStones, 0) + stones[s]
    return newStones
    
def run(stones):
    for i in range(75):
        if i == 25: p1 = sum(stones.values())
        stones = nextState(stones)
    return p1, sum(stones.values())

print("Part 1&2: ", run(stones))