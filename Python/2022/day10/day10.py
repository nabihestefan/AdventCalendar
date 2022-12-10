files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    data = [x.strip().split() for x in f.readlines()]

def run(data):
    pos = 1
    cycle = 0
    signalStrength = 0
    measured = [20, 60, 100, 140, 180, 220]
    board = [[" " for _ in range(40)] for _ in range(6)]
    
    if abs(pos-(cycle%40)) <= 1: board[cycle//40][cycle%40] = "█"
    if cycle+1 in measured: signalStrength += (pos * (cycle+1))
    
    for ind, i in enumerate(data):
        cycle += 1
        if abs(pos-(cycle%40)) <= 1: board[cycle//40][cycle%40] = "█"
        if cycle+1 in measured: signalStrength += (pos * (cycle+1))

        if len(i) == 2:  
            cycle += 1
            pos += int(i[1])
            if abs(pos-(cycle%40)) <= 1: board[cycle//40][cycle%40] = "█"
            if cycle+1 in measured: signalStrength += (pos * (cycle+1))
        
    print("Part 1: ", signalStrength)
    print("Part 2: ")
    for row in board: print("".join(row))

run(data)