files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    data = [x.strip().split(":") for x in f.readlines()]

class Monkey:
    def __init__(self, name, words):
        self.name = name
        words = words.strip().split(" ")
        if len(words) > 1:
            self.val = None
            self.monkey1, self.operation, self.monkey2 = words
        else:
            self.val = int(words[0])
        
    @property
    def value(self):
        if self.val == None:
            match self.operation:
                case "+":  return int(monkeys[self.monkey1].value + monkeys[self.monkey2].value)
                case "-":  return int(monkeys[self.monkey1].value - monkeys[self.monkey2].value)
                case "*":  return int(monkeys[self.monkey1].value * monkeys[self.monkey2].value)
                case "/":  return int(monkeys[self.monkey1].value / monkeys[self.monkey2].value)
                case "==": return int(monkeys[self.monkey1].value >= monkeys[self.monkey2].value)

        return self.val

monkeys = dict()
for name, words in data: monkeys[name] = Monkey(name, words)

print("Part 1: ", monkeys["root"].value)
m1 = monkeys[monkeys["root"].monkey1]
m2 = monkeys[monkeys["root"].monkey2]

# I need m2 to be the unchangeable one
monkeys["humn"].val = 0
m1Val = m1.value
monkeys["humn"].val = 2
m1ValPost = m1.value
if m1Val == m1ValPost: m1,m2 = m2,m1

low, high = 0, int(1e42)
while low < high:
    mid = (low+high)//2
    monkeys["humn"].val = mid
    dif = m2.value - m1.value
    if dif < 0: high = mid
    elif dif == 0: 
        print("Part 2: ", mid)
        break
    else: low = mid