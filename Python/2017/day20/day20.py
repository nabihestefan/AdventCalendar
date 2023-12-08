with open('input.txt', 'r') as f: lines =  [a.strip() for a in f.readlines()]

class Particle:
    def __init__(self, p, v, a):
        self.p = p
        self.v = v
        self.a = a

    def update(self):
        for i in range(3):
            self.v[i] += self.a[i]
            self.p[i] += self.v[i]

particles = []
for i in lines:
    pos, vel, acc = i.split("<")[1:]
    pos = map(int, pos[0:pos.index(">")].split(","))
    vel = map(int, vel[0:vel.index(">")].split(","))
    acc = map(int, acc[0:acc.index(">")].split(","))
    particles.append(Particle(pos,vel,acc))

def part1():
    manAccs = [sum(map(abs, i.a)) for i in particles]
    return manAccs.index(min(manAccs))

def part2():
    for step in range(100):
        positions = dict()
        for i in particles:
            i.update()
            positions[tuple(i.p)] = positions.get(tuple(i.p), []) + [i]

        for i in positions:
            if len(positions[i]) > 1:
                for p in positions[i]: particles.remove(p)

    return len(particles)

print("Part 1: ", part1())
print("Part 2: ", part2())
