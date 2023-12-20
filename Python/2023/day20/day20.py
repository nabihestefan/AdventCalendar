files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    data = [x.strip().split(" -> ") for x in f.readlines()]

class FlipFlop:
    def __init__(self, name, outputs):
        self.name = name
        self.outputs = outputs
        self.state = False
        self.inputs = None

    def addInputs(self, inputs): return None

    def run(self, pulse, input=None):
        if not pulse: 
            self.state = not self.state
            return self.state
        return None 
    
class Conjunction:
    def __init__(self, name, outputs):
        self.name = name
        self.outputs = outputs
        self.state = None
        self.inputs = dict()

    def addInputs(self, inputs):
        for input in inputs:
            self.inputs[input] = False

    def run(self, pulse, input):
        self.inputs[input] = pulse
        if False in self.inputs.values():
            return True
        return False

modules = dict()
conjInputs = dict()
for name, outputs in data:
    outputs = [x.strip() for x in outputs.split(",")]
    if name == "broadcaster":
        modules[name] = outputs
    else:
        type, name = name[0], name[1:]
        modules[name] = FlipFlop(name, outputs) if type == "%" else Conjunction(name, outputs)
    for res in outputs:
        conjInputs[res] = conjInputs.get(res, []) + [name]

for module in conjInputs: 
    if module not in modules.keys(): continue
    modules[module].addInputs(conjInputs[module])

def p1(modules):
    pulses = {True: 0, False: 0}
    for i in range(1000):
        pulses[False] += 1
        queue = []
        for x in modules["broadcaster"]:
            pulses[False] += 1
            queue.append((x, False, "broadcaster"))
        while queue:
            module, pulse, sender = queue.pop(0)
            if module not in modules.keys(): continue
            result = modules[module].run(pulse, sender)
            if result != None:
                for x in modules[module].outputs:
                    queue.append((x, result, module))
                    pulses[result] += 1
    
    return pulses[True] * pulses[False]

def p2(modules, inputs):
    def gcd(n, m):
        if m == 0:
            return n
        return gcd(m, n % m)

    firstTrue = {x:[] for x in inputs}
    i = 0
    while True:
        if False not in [len(x) > 1 for x in firstTrue.values()]: break
        queue = [(x, False, "broadcaster") for x in modules["broadcaster"]]
        while queue:
            module, pulse, sender = queue.pop(0)
            if module not in modules.keys(): continue
            result = modules[module].run(pulse, sender)
            if result != None:
                if module in firstTrue and result:  firstTrue[module].append(i)
                for x in modules[module].outputs:
                    queue.append((x, result, module))
        i += 1

    lcm = 1
    for i in firstTrue.values():
        lcm = (lcm * (i[1]-i[0])) // gcd(lcm, i[1]-i[0])
    return lcm
    
            
print("Part 1: ", p1(modules))
print("Part 2: ", p2(modules, conjInputs[conjInputs["rx"][0]]))