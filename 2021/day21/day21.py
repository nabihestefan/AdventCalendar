files = ['input.txt', 'inputTest.txt']
## Parsing
lines = []
for line in open(files[0]):
    lines.append(line.strip())

player1Pos = int(lines[0][lines[0].index(":")+2:])
player2Pos = int(lines[1][lines[1].index(":")+2:])

def part1(player1Pos, player2Pos):
    dieVal = 1
    player1Score = 0
    player2Score = 0

    while True:
        player1Pos = (player1Pos + dieVal*3 + 3)%10
        dieVal += 3
        player1Score += player1Pos+1
        if player1Score > 1000:
            return player2Score*(dieVal-1)

        player2Pos = (player2Pos + dieVal*3 + 3)%10
        dieVal += 3
        player2Score += player2Pos+1
        if player2Score > 1000:
            return player1Score*(dieVal-1)

GameState = {}
def part2(player1Pos, player2Pos, player1Score, player2Score):
  if player1Score >= 21:
    return (1,0)
  if player2Score >= 21:
    return (0, 1)
  if (player1Pos, player2Pos, player1Score, player2Score) in GameState:
    return GameState[(player1Pos, player2Pos, player1Score, player2Score)]
  result = (0,0)
  for i in [1,2,3]:
    for j in [1,2,3]:
      for k in [1,2,3]:
        new_player1Pos = (player1Pos+i+j+k)%10
        new_player1Score = player1Score + new_player1Pos + 1

        x1, y1 = part2(player2Pos, new_player1Pos, player2Score, new_player1Score)
        result = (result[0]+y1, result[1]+x1)
  GameState[(player1Pos, player2Pos, player1Score, player2Score)] = result
  return result

print("Part 1: ", part1(player1Pos-1, player2Pos-1))
print("Part 2: ", max(part2(player1Pos-1, player2Pos-1, 0, 0)))
