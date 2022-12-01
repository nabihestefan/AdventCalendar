## Parsing
from copy import deepcopy
from sys import maxsize
files = ['input.txt', 'testInput.txt']
with open(files[0], 'r') as f:
    lines = f.readlines()
    boss_hp = int(lines[0][lines[0].index(":")+2:].strip())
    boss_dmg = int(lines[1][lines[1].index(":")+2:].strip())

mana, player_hp = 500, 50

class Spell():
       def __init__(self, name, cost, turns=0, dmg=0, heal=0,
                armor=0, mana=0):
        self.name = name
        self.cost = cost
        self.turns = turns
        self.dmg = dmg
        self.heal = heal
        self.armor = armor
        self.mana = mana

spells = (
    Spell('Magic Missile', 53,  dmg=4),
    Spell('Drain',         73,  dmg=2, heal=2),
    Spell('Shield',        113, turns=6, armor=7),
    Spell('Poison',        173, turns=6, dmg=3),
    Spell('Recharge',      229, turns=5, mana=101),
)
leastMana = maxsize

def sim(player_hp, mana, boss_hp, activeSpells, playerTurn, manaUsed, hard):

    if hard:
        player_hp -= 1
        if player_hp <= 0:
            return False

    # print(boss_hp)
    global boss_dmg
    player_armor = 0

    ## Check spells
    stillActiveSpells = []
    for spell in activeSpells:
        if spell.turns >= 0:
            boss_hp -= spell.dmg
            player_hp += spell.heal
            player_armor += spell.armor
            mana += spell.mana
        spell.turns -= 1
        if spell.turns > 0:
            stillActiveSpells.append(deepcopy(spell))

    ## Check end
    if boss_hp <= 0:
        global leastMana
        leastMana = min(leastMana, manaUsed)
        return True

    ## Check Dead end
    if manaUsed >= leastMana:
        return False

    ## Play turn
    if playerTurn:
        for spell in spells:
            spellActive = False
            for activeSpell in stillActiveSpells:
                if activeSpell.name == spell.name:
                    spellActive = True
                    break

            if spell.cost <= mana and not spellActive:
                next = deepcopy(stillActiveSpells)
                next.append(deepcopy(spell))
                sim(player_hp, mana-spell.cost, boss_hp, next, not playerTurn, manaUsed+spell.cost, hard)

    else:
        player_hp -= (boss_dmg - player_armor) if (boss_dmg - player_armor) > 0 else 1
        if player_hp > 0:
            sim(player_hp, mana, boss_hp, activeSpells, not playerTurn, manaUsed, hard)




# Part1
sim(player_hp, mana, boss_hp, [], True, 0, False)
print("Part 1")
print(leastMana)

leastMana = maxsize

#Part 2
sim(player_hp, mana, boss_hp, [], True, 0, True)
print("Part 2")
print(leastMana)
