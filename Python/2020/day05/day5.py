files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f: lines =  [a.strip() for a in f.readlines()]

seatID = lambda row,col: row*8 + col

def makeSeat(string):
    rowStr = string[0:7]
    row = [0,127]
    for c in rowStr:
        if c == "B": row[0] += (row[1]-row[0])//2 + ((row[1]-row[0])%2 > 0)
        else: row[1] -= (row[1]-row[0])//2 + ((row[1]-row[0])%2 > 0)

    colStr = string[-3:]
    col = [0,7]
    for c in colStr:
        if c == "R": col[0] += (col[1]-col[0])//2 + ((col[1]-col[0])%2 > 0)
        else: col[1] -= (col[1]-col[0])//2 + ((col[1]-col[0])%2 > 0)
    return (row[0], col[0])

seats = []
for i in lines:
    seats.append(makeSeat(i))

seatIDs = []
for seat in seats:
    seatIDs.append(seatID(seat[0], seat[1]))

seatIDs.sort()
print("Part 1: ", seatIDs[-1])

for i in range(len(seatIDs)):
    if seatIDs[i+1]-seatIDs[i] != 1:
        print("Part 2: ", seatIDs[i]+1)
        break
