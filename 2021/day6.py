## Parsing
with open('day6.txt') as f:
    lines = f.readlines()

fish = []
for i in lines[0]:
    if i != ',' and i !='\n':
        fish.append(int(i))

days = 256 #80

today = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
tomorrow = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
for i in fish:
    today[i] += 1

for i in range(0,days):
    tomorrow[8] = today[0]
    tomorrow[0] = today[1]
    tomorrow[1] = today[2]
    tomorrow[2] = today[3]
    tomorrow[3] = today[4]
    tomorrow[4] = today[5]
    tomorrow[5] = today[6]
    tomorrow[6] = today[7] + today[0]
    tomorrow[7] = today[8]

    today = tomorrow
    tomorrow = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}

total = 0
for i in range(0,9):
    total += today[i]
print(total)
