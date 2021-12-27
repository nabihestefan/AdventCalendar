import numpy,math
files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f: lines =  f.read().split("\n\n")

class Tile:
    def __init__(self, data):
        data = data.splitlines()
        self.id = int(data[0][5:-1])
        self.content = numpy.array([list(line) for line in data[1:]])
        self.borders = {self.top, self.bottom, self.left, self.right}
        self.rotate(2)
        self.borders.update((self.top,self.bottom, self.left,self.right))
        self.sharedBorders = set()
        self.neighbors = set()

    def rotate(self, n=1):
        self.content = numpy.rot90(self.content, n)

    def flip(self):
        self.content = numpy.flip(self.content, 1)


    @property
    def top(self):
        return "".join(self.content[0, :])

    @property
    def bottom(self):
        return "".join(self.content[-1, :])

    @property
    def left(self):
        return "".join(self.content[:, 0])

    @property
    def right(self):
        return "".join(self.content[:, -1])



tiles = [Tile(line) for line in lines]

def part1(tiles):
    for i, tile in enumerate(tiles):
        for other in tiles[i+1:]:
            shared = other.borders & tile.borders
            if shared:
                tile.neighbors.add(other)
                other.neighbors.add(tile)
                tile.sharedBorders.update(shared)
                other.sharedBorders.update(shared)

    corners = 1
    for i in tiles:
        if len(i.neighbors) ==   2:
            corners *= i.id
    return corners

def part2(tiles):
    for tile in tiles:
        if len(tile.neighbors) == 2: break

    for _ in range(4):
        if {tile.right, tile.bottom}.issubset(tile.sharedBorders): break
        tile.rotate()

    tileMap = [[tile]]
    sideL = int(math.sqrt(len(tiles)))
    for y in range(1, sideL):
        for neighbor in tile.neighbors:
            if tile.right in neighbor.sharedBorders: break
        for j in range(8):
            if neighbor.left == tile.right: break
            neighbor.rotate()
            if j == 4: neighbor.flip()
        tileMap[0].append(neighbor)
        tile = neighbor

    for y in range(1, sideL):
        row = []
        for x in range(sideL):
            tile = tileMap[y-1][x]
            for neighbor in tile.neighbors:
                if tile.bottom in neighbor.sharedBorders: break
            for j in range(8):
                if neighbor.top == tile.bottom: break
                neighbor.rotate()
                if j == 4: neighbor.flip()
            row.append(neighbor)
        tileMap.append(row)

    tileSize = tile.content.shape[0]-2
    imgSide = sideL*tileSize
    image = numpy.empty(shape=(imgSide+2,imgSide+2), dtype=str)

    for y,row in enumerate(tileMap):
        for x,tile in enumerate(row):
            image[y*tileSize:(y+1)*tileSize, x*tileSize:(x+1)*tileSize] = tile.content[1:-1, 1:-1]

    monster = numpy.array((
        list("                  # "),
        list("#    ##    ##    ###"),
        list(" #  #  #  #  #  #   ")
    ))

    monsterSet = {(x,y) for y,x in zip(*numpy.where(monster=="#"))}
    monsterW = len(monster[0])
    monsterH = len(monster)
    foundMonster = False

    for i in range(8):
        allHashtag =  {(x, y) for y, x in zip(*numpy.where(image == "#"))}
        for y in range(imgSide-monsterH):
            for x in range(imgSide-monsterW):
                cropped = image[y:y+monsterH, x:x+monsterW]
                hashtags = set()
                for cy, row in enumerate(cropped):
                    for cx, point in enumerate(row):
                        if point == "#": hashtags.add((cx,cy))
                if monsterSet.issubset(hashtags):
                    foundMonster = True
                    for bx, by in monsterSet&hashtags:
                        pos = (x+bx, y+by)
                        allHashtag.remove(pos)
        if foundMonster: break
        image = numpy.rot90(image)
        if i == 4: image = numpy.flip(image, 1)
    return len(allHashtag)



print("Part 1: ", part1(tiles))
print("Part 2: ", part2(tiles))
