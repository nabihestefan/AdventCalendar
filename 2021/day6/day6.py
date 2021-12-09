today = [0,0,0,0,0,0,0,0,0]

with open('day6.txt') as f:
    ints = [int(x) for x in f.readlines()[0].split(',')]
    for i in ints:
        today[i] += 1

for i in range(0,256):
    new_fish = today[0]
    today[0:8] = today[1:]
    today[8] = new_fish
    today[6] += new_fish

print(sum(today))
