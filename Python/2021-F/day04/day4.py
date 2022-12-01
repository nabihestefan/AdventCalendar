
class Board:
    def __init__(self, l1, l2, l3, l4, l5):
        self.line1 = self.format(l1)
        self.line2 = self.format(l2)
        self.line3 = self.format(l3)
        self.line4 = self.format(l4)
        self.line5 = self.format(l5)
        self.checked = [[False,False,False,False,False],
                        [False,False,False,False,False],
                        [False,False,False,False,False],
                        [False,False,False,False,False],
                        [False,False,False,False,False]]
        self.won = False

    def format(self, str):
        one = int(str[0:2])
        two = int(str[3:5])
        thr = int(str[6:8])
        four = int(str[9:11])
        five = int(str[12:14])
        line = [one, two, thr, four, five]
        return line

    def display(self):
        print(self.line1)
        print(self.line2)
        print(self.line3)
        print(self.line4)
        print(self.line5)
        print()

    def hasNumber(self, number):
        if number in self.line1:
            place = self.line1.index(number)
            self.checked[0][place] = True
            return True
        if number in self.line2:
            place = self.line2.index(number)
            self.checked[1][place] = True
            return True
        if number in self.line3:
            place = self.line3.index(number)
            self.checked[2][place] = True
            return True
        if number in self.line3:
            place = self.line3.index(number)
            self.checked[2][place] = True
            return True
        if number in self.line4:
            place = self.line4.index(number)
            self.checked[3][place] = True
            return True
        if number in self.line5:
            place = self.line5.index(number)
            self.checked[4][place] = True
            return True

    def solved(self):
        for i in range(5):
            if self.checked[i] == [True,True,True,True,True]:
                return True
            elif [self.checked[0][i],self.checked[1][i],self.checked[2][i],self.checked[3][i],self.checked[4][i]] == [True,True,True,True,True]:
                return True

    def unchecked(self):
        sum = 0
        for i in range(5):
            if not self.checked[0][i]:
                sum += self.line1[i]
            if not self.checked[1][i]:
                sum += self.line2[i]
            if not self.checked[2][i]:
                sum += self.line3[i]
            if not self.checked[3][i]:
                sum += self.line4[i]
            if not self.checked[4][i]:
                sum += self.line5[i]
        return sum

def form(str):
    i = 0
    nums = []
    while i < len(str):
        nums.append(int(str[i:i+2]))
        i+=3
    return nums

with open('day4.txt') as f:
    lines = f.readlines()

numbers = map(int, lines.pop(0).split(","))

i = 0
boards =[]
while i < len(lines):
    line1 = lines[i+1]
    line2 = lines[i+2]
    line3 = lines[i+3]
    line4 = lines[i+4]
    line5 = lines[i+5]
    i += 6
    boards.append(Board(line1,line2,line3,line4,line5))

def run(numbers, boards, part2):
    for i in numbers:
        toRemove = []
        for j in boards:
            j.hasNumber(i)
            if j.solved():
                if not part2:
                    return i*j.unchecked()
                elif len(boards) == 1: return i*j.unchecked()
                toRemove.append(j)
        for i in toRemove: boards.remove(i)

print("Part 1: ", run(numbers, boards, False))
print("Part 1: ", run(numbers, boards, True))
