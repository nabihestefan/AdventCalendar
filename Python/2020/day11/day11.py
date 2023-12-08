from copy import deepcopy
files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f:
    seats =  [["."]+list(a.strip())+["."] for a in f.readlines()]
seats = [["." for a in seats[0]]] + seats + [["." for a in seats[0]]]

adj = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
def run(seats, partTwo, adjCount):
    while True:
        newSeats = deepcopy(seats)
        for i in range(1,len(seats)-1):
            for j in range(1,len(seats[i])-1):
                adjacent = []
                for c in adj:
                    m = 1
                    if partTwo:
                        while (0 < i-c[0]*m and i-c[0]*m < len(seats)-1) and \
                        (0 < j-c[1]*m and j-c[1]*m < len(seats[i])-1) and \
                        seats[i-c[0]*m][j-c[1]*m] == ".":
                            m+=1
                    adjacent.append(seats[i-c[0]*m][j-c[1]*m])
                if "#" not in adjacent and newSeats[i][j] != ".":
                    newSeats[i][j] = "#"
                if adjacent.count("#") >= adjCount and newSeats[i][j] != ".":
                    newSeats[i][j] = "L"

        if newSeats == seats:
            break
        seats = deepcopy(newSeats)

    occupied = 0
    for i in seats:
        for j in i:
            if j == "#": occupied += 1
    return occupied

print("Part 1: ", run(seats, False, 4))
print("Part 2: ", run(seats, True, 5))
