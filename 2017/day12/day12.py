with open('input.txt', 'r') as f:
    lines = [a.strip().split("<->") for a in f.readlines()]

points = dict()
for start, end in lines: points[int(start)] = list(map(int, end.split(",")))

def run(part1):
    groups = 0
    while len(points) > 0:
        visited = set()
        visited.add(list(points.keys())[0])
        added = True
        while added:
            added = False
            for i in set(points.keys()) - visited:
                if len(visited & set(points[i])) > 0:
                    visited.add(i)
                    added = True

        if part1: return len(visited)
        for i in list(visited): del points[i]
        groups += 1
    return groups

print("Part 1: ", run(True))
print("Part 2: ", run(False))
