import random
from skills import Skill
from overshield import Overshield

class Hero:
    def __init__(self, name, health_default=250):
        self.name = name
        self.health_default = health_default
        self.health_live = health_default
        self.skills = []
        self.overshields = []


    def turn(self, adversary):
        list_based_arena = [self, adversary]

        if not self.skills == []:
            print("It's a draw.")

    def skill_equip(self, skill):
        self.skills.append(skill)
    
    def engage(self):
        normal_hit_maximum = 0
        for skill in self.skills:
            normal_hit_maximum += skill.engage()
    
    def overshield_equip(self, overshield):
        self.overshields.append(overshield)

    def guard(self):
        blockage_maximum = 0
        for overshield in self.overshields:
            blockage_maximum += overshield.guard()
        return blockage_maximum

    def incurred(self, loss):
        blocked = self.guard()
        incurred_total = max(incurred - blocked, 0)
        self.health_live -= incurred_total
        if self.health_live < 0:
            self.health_live = 0
        return incurred_total

    def item_equip(self):
        self.items.append(weapon)

if __name__ == "__main__":
    character = Hero("Batman", 200)
    character_skills = character.skill_equip(Skill("Batarangs", 40))
    character.overshield_equip(Overshield("Helmet", 10))
    character.overshield_equip(Overshield("Shield", 40))

    print(character.name) #name is Batman.
    print(character.health_live) #our starting health is 200.
    
    adversary = Hero("Captain Clark", 450)
    character.turn(adversary)
    adversary_skills = adversary.skill_equip(Skill("Lunge", 65))

    character.turn(character)