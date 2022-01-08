## Parsing
files = ['input.txt', 'testInput.txt']
with open(files[0], 'r') as f:
    directions =  [a.strip() for a in f.readlines()]

def solve(buttons, current):
    password = ""
    for dir in directions:
        for c in dir:
            if c == "U":
                current[0] -= 1
                if buttons[current[0]][current[1]] == "X": current[0] += 1
            if c == "L":
                current[1] -= 1
                if buttons[current[0]][current[1]] == "X": current[1] += 1
            if c == "R":
                current[1] += 1
                if buttons[current[0]][current[1]] == "X": current[1] -= 1
            if c == "D":
                current[0] += 1
                if buttons[current[0]][current[1]] == "X": current[0] -= 1
        print(current)
        password += buttons[current[0]][current[1]]
    return password

board1 = [["X","X","X","X","X"],
          ["X","1","2","3","X"],
          ["X","4","5","6","X"],
          ["X","7","8","9","X"],
          ["X","X","X","X","X"]]

board2 = [["X","X","X","X","X","X","X"],
          ["X","X","X","1","X","X","X"],
          ["X","X","2","3","4","X","X"],
          ["X","5","6","7","8","9","X"],
          ["X","X","A","B","C","X","X"],
          ["X","X","X","D","X","X","X"],
          ["X","X","X","X","X","X","X"]]

print(solve(board1,[2,2]))
print(solve(board2,[3,1]))
