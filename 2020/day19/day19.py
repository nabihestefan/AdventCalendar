files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f: rulesStr, msgStr = f.read().split("\n\n")

rules = {}
messages = msgStr.split("\n")

for rule in rulesStr.split("\n"):
    rule = rule.split(":")
    if "\"" in rule[1]:
        subrules = rule[1][2]
    elif "|" in rule[1]:
        subrules = [[int(a) for a in b.strip().split(" ")] for b in rule[1].strip().split("|")]
    else:
        subrules = [int(a) for a in rule[1].strip().split(" ")]

    rules[int(rule[0])] = subrules

def decodeRule(ind):
    global rules
    rule = rules[ind]
    while not all(type(x) == str for x in rule):
        i = 0
        if type(rule[i]) == list:
            rule = ["["] + rule[0] + ["|"] + rule[1] + ["]"]

        while i < len(rule):
            inst = rule[i]
            if type(inst) == str:
                pass
            else:
                newInst = rules[inst]
                if type(newInst) in [int, str]:
                    rule = rule[:i] + [newInst] + rule[i+1:]
                else:
                  if type(newInst[0]) == int:
                    rule = rule[:i] + newInst + rule[i+1:]
                  else:
                    rule = rule[:i] + ["["] + newInst[0] + ["|"] + newInst[1] + ["]"] + rule[i+1:]
            i+=1

    return "".join(rule)

def getL(rule):
    i, c = 0,0
    while i < len(rule):
        if rule[i] in ["a", "b"]:
            c += 1
        elif rule[i] == "|":
            depth = 1
            while depth > 0:
                i += 1
                if rule[i] == "|":
                    depth += 1
                elif rule[i] == "]":
                    depth -= 1
        i += 1
    return(c)

def isValid(rule,msg):
  pointers = [0]
  mPtr = [0]
  if len(msg) != getL(rule): return False

  while pointers:
    if mPtr[0] >= len(msg):
      return True

    cur = rule[pointers[0]]
    if cur in ["a", "b"]:
      if msg[mPtr[0]] == cur:
        pointers[0] += 1
        mPtr[0] += 1
      else:
        pointers.pop(0)
        mPtr.pop(0)
    elif cur == "[":
      tempPtr, depth = pointers[0] + 1, 1
      while depth > 0:
        if rule[tempPtr] == "[": depth += 1
        elif rule[tempPtr] == "|": depth -= 1
        tempPtr += 1
      pointers.append(tempPtr)
      mPtr.append(mPtr[0])
      pointers[0] += 1
    elif cur == "|":
      depth = 1
      while depth > 0:
        pointers[0] += 1
        if rule[pointers[0]] == "[": depth += 1
        elif rule[pointers[0]] == "]": depth -= 1
      pointers[0] += 1
    else:
      pointers[0] += 1

  return False

rule = decodeRule(0)

valid = 0
for msg in messages:
    if isValid(rule, msg): valid+=1

print("Part 1: ", valid)

rule42, rule31 = decodeRule(42), decodeRule(31)
ruleLen = getL(rule42)
c = 0

for msg in messages:
    if len(msg) % ruleLen != 0 or len(msg) < (ruleLen * 3):
      pass
    elif len(msg) == (ruleLen * 3):
      c += 1 if isValid(rule42 + rule42 + rule31, msg) else 0
    else:
      if isValid(rule42, msg[0:ruleLen]) and isValid(rule42, msg[ruleLen:2*ruleLen]) and isValid(rule31, msg[-ruleLen:]):
        midSegs = int(len(msg) / ruleLen) - 3
        valid42 = all(isValid(rule42, msg[(2+i)*ruleLen:(3+i)*ruleLen]) for i in range(int(midSegs/2) + midSegs%2))

        flag = 42
        for i in range(int(midSegs/2), 0, -1):
          if flag == 42:
            flag = 42 if isValid(rule42, msg[(i+1)*-ruleLen:i*-ruleLen]) else 31
          if flag == 31:
            flag = 31 if isValid(rule31, msg[(i+1)*-ruleLen:i*-ruleLen]) else 0
        c += 1 if flag > 0 and valid42 else 0
      else:
        pass

print("Part 2: ", c)
