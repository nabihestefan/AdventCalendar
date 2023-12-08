files = ['input.txt', 'inputTest.txt']
with open(files[1], 'r') as f:
    data = [x for x in f.readlines()[0].strip()]
    
class Rock():
    def __init__(self):
        self.coords = set()
    
    def maxHeight(self):
        maxHeight = 0
        for i in self.coords:
            maxHeight = max(maxHeight, i.imag)
        return maxHeight

    def moveDown(self):
        rock = Rock()
        for i in self.coords:
            rock.coords.add(i - 1j)
        return rock
    
    def moveLeft(self):
        rock = Rock()
        for i in self.coords:
            rock.coords.add(i - 1)
        return rock
    
    def moveRight(self):
        rock = Rock()
        for i in self.coords:
            rock.coords.add(i + 1)
        return rock
    
    @classmethod
    def line(self, x, y):
        rock = Rock()
        start_poss = [
            complex(0, 0),
            complex(1, 0),
            complex(2, 0),
            complex(3, 0),
        ]
        for position in start_poss:
            position += complex(x, y)
            rock.coords.add(position)
        return rock
    
    @classmethod
    def plus(self, x, y):
        rock = Rock()
        start_poss = [
            complex(1, 0),
            complex(0, 1),
            complex(1, 1),
            complex(2, 1),
            complex(1, 2),
        ]
        for position in start_poss:
            position += complex(x, y)
            rock.coords.add(position)
        return rock
    
    @classmethod
    def letter(self, x, y):
        rock = Rock()
        start_poss = [
            complex(0, 0),
            complex(1, 0),
            complex(2, 0),
            complex(2, 1),
            complex(2, 2)
        ]
        for position in start_poss:
            position += complex(x, y)
            rock.coords.add(position)
        return rock
    
    @classmethod
    def vertical(self, x, y):
        rock = Rock()
        start_poss = [
            complex(0, 0),
            complex(0, 1),
            complex(0, 2),
            complex(0, 3),
        ]
        for position in start_poss:
            position += complex(x, y)
            rock.coords.add(position)
        return rock
    
    @classmethod
    def square(self, x, y):
        rock = Rock()
        start_poss = [
            complex(0, 0),
            complex(0, 1),
            complex(1, 0),
            complex(1, 1),
        ]
        for position in start_poss:
            position += complex(x, y)
            rock.coords.add(position)
        return rock

class Cave:
    rocks = [Rock.line, Rock.plus, Rock.letter, Rock.vertical, Rock.square]
    def __init__(self, width, moves):
        self.width = width
        self.moves = moves #input
        self.moveIndex = 0
        self.rockIndex = 0
        self.height = 1
        self._spawnHeight = 3
        self.startX = 2
        self.rockPositions = set()

    @property
    def startY(self):
        return self.height + self._spawnHeight

    def getNextRock(self):
        rock = self.rocks[self.rockIndex](self.startX, self.startY)
        self.rockIndex = (self.rockIndex+1)%len(self.rocks)
        return rock

    def validMove(self, rock):
        if self.rockPositions & rock.coords:
            return False
        for i in rock.coords:
            if (i.real == -1) or (i.real == self.width):
                return False
            if i.imag == 0:
                return False
        return True

    def dropRock(self):
        rock = self.getNextRock()

        while True:
            move = self.moves[self.moveIndex]
            self.moveIndex = (self.moveIndex + 1)%len(self.moves)
            if move == ">":
                nextPos = rock.moveRight()
                if self.validMove(nextPos):
                    rock = nextPos
            elif move == "<":
                nextPos = rock.moveLeft()
                if self.validMove(nextPos):
                    rock = nextPos
            
            nextPos = rock.moveDown()
            if self.validMove(nextPos):
                rock = nextPos
            else:
                self.rockPositions.update(rock.coords)
                heightDiff = rock.maxHeight() + 1 - self.height
                self.height = max(self.height, rock.maxHeight() + 1)
                return 0 if heightDiff < 1 else heightDiff

def findPattern(heights):
    # There are arbitraty and just high enough that the running wont take ages
    # Recommend running with 1,1 if doing first trial
    startPattLen = 3500
    startRange = 125
    max_pattern_length = len(heights) // 2
    for pattern_length in range(startPattLen, max_pattern_length):
        for i in range(startRange, len(heights) - pattern_length):
            window = heights[i : i + pattern_length]
            duplicates = 0
            next_start = i + pattern_length
            next_stop = next_start + pattern_length
            while window == heights[next_start:next_stop]:
                duplicates += 1
                if duplicates >= 3:
                    return i, window
                next_start, next_stop = (
                    next_start + pattern_length,
                    next_stop + pattern_length,
                )
       



def run(partTwo, data):
    cave = Cave(7, data)
    heightChanges = []
    for i in range(25000):
        heightChanges.append(cave.dropRock())
    print("Part 1: ", sum(heightChanges[:2022]))
    start, segment = findPattern(heightChanges)

    startHeight = sum(heightChanges[:start])
    middle, final = divmod(1000000000000-start, len(segment))
    patterned = middle * sum(segment)
    endHeight = sum(segment[:final])

    return int(startHeight + patterned + endHeight)



print("Part 2: ", run(True, data))