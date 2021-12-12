files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f:
    lines =  [a.strip() for a in f.readlines()]

paths = {}

def add_path(start, end):
    if end != "start":
        paths[start] = paths.get(start, []) + [end]

for i in lines:
    start, end = i.split("-")
    add_path(start,end)
    add_path(end, start)


def pathsThrough(visited = ["start"]):
    current = visited[-1]

    if current == "end": return [visited]

    newPaths = []

    for next in paths[current]:
        if next.islower() and next in visited:
            continue
        newPaths.extend(pathsThrough(visited + [next]))
    return newPaths

def pathsThroughRevisit(visited = ["start"], canRevisit = True):
    current = visited[-1]
    if current == "end": return [visited]

    newPaths = []

    for next in paths[current]:
        if next == "start": continue
        if next.islower() and next in visited:
            if canRevisit:
                newPaths.extend(pathsThroughRevisit(visited + [next], False))
        else:
            newPaths.extend(pathsThroughRevisit(visited + [next], canRevisit))
    return newPaths



print("PART1")
print(len(pathsThrough()))
print("PART2")
print(len(pathsThroughRevisit()))
