from copy import deepcopy
files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f:
    lines =  f.read().strip().split("\n")

class Group(object):
    def __init__(self,team,units,hp,immune,weak,init,dType,dPow,side):
        self.team = team
        self.units = units
        self.hp = hp
        self.immune = immune
        self.weak = weak
        self.init = init
        self.dmgType = dmgType
        self.dmgPow = dmgPow
        self.side = side
        self.target = None

    def effectivePow(self): return self.units * self.dmgPow
    def damageTo(self, v):
        if self.dmgType in v.immune: return 0
        elif self.dmgType in v.weak: return 2*self.effectivePow()
        else: return self.effectivePow()
    def boostPow(self,boost):
        self.dmgPow += (boost if self.side==0 else 0)

#Parsing
teams = []
for line in lines:
    if "Immune System" in line: nextID, side = 1,0
    elif "Infection" in line: nextID, side = 1,1
    elif line:
        words = line.split()
        units = int(words[0])
        hp = int(words[4])
        immune, weak = set(), set()
        if "(" in line:
            things = line.split("(")[1].split(")")[0]
            def parse(line):
                words = line.split()
                for word in words[2:]:
                    if word.endswith(","): word = word[:-1]
                    (immune if words[0]=="immune" else weak).add(word)
            if ";" in things:
                s1,s2 = things.split(";")
                parse(s1)
                parse(s2)
            else: parse(things)
        init = int(words[-1])
        dmgType, dmgPow = words[-5], int(words[-6])
        team = '{}_{}'.format({1:'Infection', 0:'System'}[side], nextID)
        teams.append(Group(team,units,hp,immune,weak,init,dmgType,dmgPow,side))
        nextID += 1

#Simulate battle
def battle(ogTeams,boost):
    teams=ogTeams[:]

    for t in teams: t.boostPow(boost)
    while True:
        teams.sort(key=lambda x: (-x.effectivePow(), -x.init))
        chosen = set()
        for t in teams:
            def targetKey(ot): return (-t.damageTo(ot), -ot.effectivePow(), -ot.init)
            targets = sorted([ot for ot in teams if ot.side!=t.side and \
                       ot.team not in chosen and t.damageTo(ot)>0], key=targetKey)
            if targets:
                t.target = targets[0]
                chosen.add(targets[0].team)

        teams.sort(key=lambda x:-x.init)
        anyKills = False
        for t in teams:
            if t.target:
                dmg = t.damageTo(t.target)
                killed = min(t.target.units, dmg/t.target.hp)
                if killed > 0: anyKills = True
                t.target.units -= killed

        teams = [t for t in teams if t.units > 0]
        for t in teams: t.target = None


        unitsImmune = sum([t.units for t in teams if t.side == 0])
        unitsInfection = sum([t.units for t in teams if t.side == 1])

        if not anyKills:
            return "Infection", unitsInfection
        if unitsImmune == 0: return "Infection", unitsInfection
        if unitsInfection == 0: return "Immune", unitsImmune


boost = 0
print("Part 1: ", battle(deepcopy(teams), boost)[1])
while "Infection" == battle(deepcopy(teams), boost)[0]: boost += 1
print("Part 2: ", battle(deepcopy(teams), boost)[1])
