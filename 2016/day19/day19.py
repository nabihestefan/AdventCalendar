## Parsing
files = ['input.txt', 'testInput.txt']
with open(files[0], 'r') as f:
    elfNum =  int(f.readlines()[0].strip())

class Elf:
    num = 0
    def __init__(self, right=None):
        self.left = None
        self.right = right
        Elf.num += 1
        self.num = Elf.num

    def remove(self):
        self.left.right = self.right
        self.right.left = self.left
        return self.left

def run(elfNum, partTwo=False):
    Elf.num = 0
    elf = Elf()
    prev = elf
    for i in range(elfNum-1):
        prev.left = Elf(prev)
        prev = prev.left
    prev.left = elf

    if partTwo:
        for _ in range(elfNum // 2): elf = elf.left
    else: elf = elf.left

    while elfNum > 1:
        if partTwo:
            elf = elf.remove()
            if elfNum % 2 == 1: elf = elf.left
        else: elf = elf.remove().left
        elfNum -= 1

    return elf.num

print("Part 1: ",run(elfNum))
print("Part 2: ",run(elfNum,True))
