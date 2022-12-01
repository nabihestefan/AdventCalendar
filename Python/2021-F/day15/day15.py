import networkx as nx
files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f: lines =  [a.strip() for a in f.readlines()]

scannedMaze = []
for i in lines:
    line = []
    for j in i: line.append(int(j))
    scannedMaze.append(line)

def increaseRow(row, a):
    incRow = []
    for i in row:
        if i+a > 9:
            incRow.append(i+a-9)
        else:
            incRow.append(i+a)
    return incRow

fullMaze = []
for i in range(5):
    for k in scannedMaze:
        line = []
        for j in range(5):
            line += increaseRow(k, i+j)
        fullMaze.append(line)

def shortestPath(maze):
    G = nx.DiGraph()
    adj = [(1,0), (0,1), (-1,0), (0,-1)]

    for i in range(len(maze)):
        for j in range(len(maze[0])):
            for x,y in adj:
                if 0 <= i+x and i+x < len(maze) and 0 <= j+y and j+y < len(maze[0]):
                    G.add_edge((i,j), (i+x,j+y), weight=maze[i+x][j+y])

    return nx.shortest_path_length(G, (0,0), (len(maze)-1, len(maze[0])-1), weight='weight')

print("PART1")
print(shortestPath(scannedMaze))
print("PART2")
print(shortestPath(fullMaze))
