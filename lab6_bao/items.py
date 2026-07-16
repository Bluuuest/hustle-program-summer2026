from skills import Skill

class Weapon(Ability):
  def attack(self):
    """  This method returns a random value
    between one half to the full attack power of the weapon.
    """
    half_hit_maximum = skill_hit_maximum // 2
    return randint(half_hit_maximum, skills_hit_maximum)
    # then return a random integer between half of max_damage and max_damage