with open('input.txt', 'r') as f:
    lines = [a.strip().split("<->") for a in f.readlines()]

points = dict()
for start, end in lines: points[int(start)] = list(map(int, end.split(",")))

def run(part1):
    groups = 0
    while len(points) > 0:
        visited, prev = set(), set()
        visited.add(list(points.keys())[0])
        while len(prev) != len(visited):
            prev.update(visited)
            for i in prev:
                for j in points[i]: visited.add(j)

        if part1: return len(visited)
        for i in visited: del points[i]
        groups += 1
    return groups

print("Part 1: ", run(True))
print("Part 2: ", run(False))
