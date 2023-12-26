files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    monkeyData = [x.split("\n") for x in f.read().split("\n\n")]

class Monkey:
    def __init__(self, items, operation, test):
        self.inspected = 0
        self.items = [int(i) for i in items[18:].split(',')]

        operation = operation.split()
        if operation[4] == "+":
            if operation[5] == "old":
                self.operation = lambda x: x+x
            else:
                self.operation = lambda x: x+int(operation[5])
        elif operation[4] == "*":
            if operation[5] == "old":
                self.operation = lambda x: x*x
            else:
                self.operation = lambda x: x*int(operation[5])

        self.test = int(test[0].split()[3])
        self.true = int(test[1].split()[5])
        self.false = int(test[2].split()[5])

def run(partTwo, monkeyData):
    monkeys = []
    LCM = 1
    for data in monkeyData:
        monkeys.append(Monkey(data[1], data[2], data[3:]))
        if LCM % monkeys[-1].test != 0: LCM *= monkeys[-1].test

    steps = 20 if not partTwo else 10000
    for step in range(steps):
        for monkey in monkeys:
            monkey.inspected +=len(monkey.items)

            for item in monkey.items:
                item = monkey.operation(item)
                if not partTwo: item //= 3
                else: item %= LCM

                if item % monkey.test == 0:
                    monkeys[monkey.true].items.append(item)
                else:
                    monkeys[monkey.false].items.append(item)
            monkey.items = []

    monkeys = sorted(monkeys, key=lambda monkey: monkey.inspected, reverse=True)
    return monkeys[0].inspected * monkeys[1].inspected

print("Part 1: ", run(False, monkeyData))
print("Part 2: ", run(True, monkeyData))
