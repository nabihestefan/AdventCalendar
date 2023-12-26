from collections import defaultdict
## Parsing
files = ['input.txt', 'testInput.txt']

COMBINATION = (61, 17)


class MicrochipException(Exception): pass


class OutputBin:

    def __init__(self, id=None):
        self.id = id
        self.items = []

    def set_value(self, value):
        self.items.append(value)


class Bot:

    def __init__(self, id=None):
        self.id = None
        self.value = None
        self.target_high = None
        self.target_low = None

    def set_value(self, value):
        if self.value is None:
            self.value = value
        else:
            high = max(self.value, value)
            low = min(self.value, value)
            if high in COMBINATION and low in COMBINATION:
                print("Part 1: bot #", self.id)
            self.target_high.set_value(high)
            self.target_low.set_value(low)
            self.value = None


class Bots:

    def __init__(self):
        self.values = []
        self.bots = defaultdict(Bot)
        self.output_bins = defaultdict(OutputBin)
        self.objects = {
            'bot': self.bots,
            'output': self.output_bins
        }

    def get_object(self, typ, id):
        id = int(id)  # all ids are ints
        obj = self.objects[typ][id]
        if obj.id is None:
            obj.id = id
        return obj

    def set_instruction(self, line):
        p = line.split()
        bot = self.get_object(* p[:2])
        bot.target_low = self.get_object(*p[5:7])
        bot.target_high = self.get_object(*p[-2:])

    def read_instructions(self, f):
        for line in f:
            if line.startswith('bot'):
                self.set_instruction(line)
            else:
                self.values.append(line)

    def run(self):
        for item in self.values:
            p = item.split()
            id, value = int(p[-1]), int(p[1])
            self.bots[id].set_value(value)


bots = Bots()
with open(files[0], 'r') as f:
    bots.read_instructions(f)

bots.run()
ans = 1
for i in range(3):
    ans *=  bots.output_bins[i].items[0]
print("Part 2: ", ans)
