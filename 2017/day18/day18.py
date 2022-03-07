with open('input.txt', 'r') as f: lines =  [a.strip().split(" ") for a in f.readlines()]

class Function:
    def __init__(self, name):
        self.played = []
        self.ind = 0
        self.regs = {"a":0, "i":0, "b":0, "f":0, "c":0, "d":0, "p":name}
        self.sent = 0
        self.deadlocked = False

def runInst(fCur, fOther, part1):
    line = lines[fCur.ind]
    inst, a = line[0], line[1]
    if len(line) == 3: b = line[2]

    if inst == "snd":
        fCur.played.append(int(a) if a not in fCur.regs.keys() else fCur.regs[a])
        fCur.sent += 1
        fOther.deadlocked = False
        fCur.ind += 1
    elif inst == "set":
        fCur.regs[a] = int(b) if b not in fCur.regs.keys() else fCur.regs[b]
        fCur.ind += 1
    elif inst == "add":
        fCur.regs[a] += int(b) if b not in fCur.regs.keys() else fCur.regs[b]
        fCur.ind += 1
    elif inst == "mul":
        fCur.regs[a] *= int(b) if b not in fCur.regs.keys() else fCur.regs[b]
        fCur.ind += 1
    elif inst == "mod":
        fCur.regs[a] %= int(b) if b not in fCur.regs.keys() else fCur.regs[b]
        fCur.ind += 1
    elif inst == "rcv":
        if part1: return fCur.played[-1]
        if len(fOther.played) > 0:
            fCur.regs[a] = fOther.played.pop(0)
            fCur.ind += 1
        else:
            fCur.deadlocked = True
    elif inst == "jgz":
        if int(a) if a not in fCur.regs.keys() else fCur.regs[a] > 0:
            fCur.ind += int(b) if b not in fCur.regs.keys() else fCur.regs[b]
        else:
            fCur.ind += 1

    return fCur, fOther

def part1():
    f0 = Function(0)
    f1 = Function(1)
    while True:
        if not f0.deadlocked: res = runInst(f0,f1, True)
        if type(res) == int:
            return res
        else: f0,f1 = res

def part2():
    f0 = Function(0)
    f1 = Function(1)
    while True:
        if not f0.deadlocked: f0,f1 = runInst(f0,f1, False)
        if not f1.deadlocked: f1,f0 = runInst(f1,f0, False)

        if f0.deadlocked and f1.deadlocked: return f1.sent

print("Part 1: ", part1())
print("Part 2: ", part2())
