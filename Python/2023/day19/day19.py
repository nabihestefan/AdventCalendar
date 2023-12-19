files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    workflowsRaw, partsRaw  = f.read().split('\n\n')

def makeTest(condition):
    if ":" not in condition:
        return (lambda x: True, condition, None)
    test, result = condition.split(":")
    var = test[0]
    op = test[1]
    val = int(test[2:])
    if op == "<": return (lambda part: part[var] < val, result, (var, lambda x: x < val))
    elif op == ">": return (lambda part: part[var] > val, result, (var, lambda x: x > val))
    assert False

workflows = dict()
for workflowStr in workflowsRaw.split('\n'):
    name, workflow = workflowStr[:-1].split('{')
    workflows[name] = [makeTest(condition) for condition in workflow.split(",")]

parts = []
for part in partsRaw.split('\n'):
    for c in 'xmas':
        part = part.replace(f'{c}=', f'"{c}":')
    parts.append(eval(part))

def p1(workflows, part, workflow):
    for condition, result, _ in workflows[workflow]:
        if condition(part):
            if result in ["A", "R"]: return result == "A"
            return p1(workflows, part, result)

def p2(workflows, workflow, x, m, a, s):
    if len(x) == 0 or len(m) == 0 or len(a) == 0 or len(s) == 0: return 0
    if workflow == "A": return len(x) * len(m) * len(a) * len(s)
    if workflow == "R": return 0

    count = 0

    for _, result, condition in workflows[workflow]:
        if condition == None: count += p2(workflows, result, x, m, a, s)
        else:
            var, rule = condition
            match var:
                case "x":
                    count += p2(workflows, result, tuple(filter(rule, x)), m, a, s)
                    x = tuple(filter(lambda v: not rule(v), x))
                case "m":
                    count += p2(workflows, result, x, tuple(filter(rule, m)), a, s)
                    m = tuple(filter(lambda v: not rule(v), m))
                case "a":
                    count += p2(workflows, result, x, m, tuple(filter(rule, a)), s)
                    a = tuple(filter(lambda v: not rule(v), a))
                case "s":
                    count += p2(workflows, result, x, m, a, tuple(filter(rule, s)))
                    s = tuple(filter(lambda v: not rule(v), s))
    return count

print("Part 1: ", sum(sum(part.values()) for part in parts if p1(workflows, part, "in")))
print("Part 2: ", p2(workflows, "in", range(1, 4001), range(1, 4001), range(1, 4001), range(1, 4001)))