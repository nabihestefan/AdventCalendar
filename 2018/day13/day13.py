files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f: lines =  [a for a in f.readlines()]

class Cart:
    def __init__(self, x,y, dir):
        self.pos = (x,y)
        self.dir = dir
        self.rot = 0
        self.crashed = False

    def move(self):
        if self.dir == 0:
            self.pos = self.pos[0], self.pos[1]-1
        if self.dir == 1:
            self.pos = self.pos[0]+1, self.pos[1]
        if self.dir == 2:
            self.pos = self.pos[0], self.pos[1]+1
        if self.dir == 3:
            self.pos = self.pos[0]-1, self.pos[1]

    def turn(self, part):
        if part == "\\": self.dir = 3-self.dir

        elif part == "/":
            if self.dir in [0,2]: self.dir +=1
            elif self.dir in[1,3]: self.dir -=1

        elif part == "+":
            if self.rot == 0: self.dir = (self.dir-1)%4
            elif self.rot == 2: self.dir = (self.dir+1)%4
            self.rot = (self.rot+1)%3


turns = {}
carts = []
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c in "<>v^":
            dir = {
                    "^": 0,
                    ">": 1,
                    "v": 2,
                    "<": 3,
                }[c]
            carts.append(Cart(x, y, dir))
        elif c in "\\/+":
            turns[(x,y)] = c

def run(turns, carts, partTwo):
    while len(carts)>1:
        carts.sort(key=lambda x: x.pos)
        for cart in carts:
            if cart.crashed:
                continue
            cart.move()
            for cart2 in carts:
                if cart!=cart2 and cart2.pos == cart.pos and not cart2.crashed:
                    cart.crashed = True
                    cart2.crashed = True
                    if not partTwo:
                        return cart.pos
            if cart.crashed:
                continue
            if cart.pos in turns.keys():
                cart.turn(turns[cart.pos])

        carts = [c for c in carts if not c.crashed]

    return carts[0].pos


print("Part 1: ", run(turns, carts, False))
print("Part 2: ", run(turns, carts, True))
