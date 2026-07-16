import random

class Skill:
    def __init__(self, name, skill_hit_maximum):
        self.name = name
        self.skill_hit_maximum = skill_hit_maximum

    def hit(self):
        hit_range = random.randint(0, self.skill_hit_maximum)
        print(hit_range)
        return hit_range
        
if __name__ == "__main__":
    attribute1 = Skill("Tac -N- Spray", 50)
    print(attribute1.name)
    print(attribute1.skill_hit_maximum)
    attribute1.hit()

    attribute2 = Skill("Echo Chamber", 75)
    print(attribute2.name)
    print(attribute2.skill_hit_maximum)
    attribute2.hit()

    attribute3 = Skill("Axe Rain", 125)
    print(attribute3.name)
    print(attribute3.skill_hit_maximum)
    attribute3.hit()

    attribute4 = Skill("Loud Bongos", 175)
    attribute4.hit

    attribute5 = Skill("Lighting in a Bottle", 200)
    attribute5.hit