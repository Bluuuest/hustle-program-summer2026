import random

class Overshield:
    def __init__(self, name, defense_maximum):
        self.name = name
        self.defense_maximum = defense_maximum

    def cover(self):
        cover_randomized = random.randint(0, self.defense_maximum)
        print(cover_randomized)
        return cover_randomized

if __name__ == "__main__":
    overshield1 = Overshield("Batter's Helmet", 25)
    print(overshield1.name)
    print(overshield1.defense_maximum)
    overshield1.cover()

    overshield2 = Overshield("N95 Mask", 10)
    print(overshield2.name)
    print(overshield2.defense_maximum)
    overshield2.cover()

    overshield3 = Overshield("MK-V Spartan Armor", 50)
    print(overshield3.name)
    print(overshield3.defense_maximum)
    overshield3.cover()