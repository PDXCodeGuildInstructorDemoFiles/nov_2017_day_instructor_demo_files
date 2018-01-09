from items import Weapon, Potion
from random import choice


class Creature:
    monster_names = [ 'Netherserpent', 'Barbsoul', 'Glowpaw', 'Webmorph',
                    'The Cloudy Abomination', 'The Empty Presence',
                    'The Outlandish Brute', 'The Horned World Hawk',
                    'The Scarred Ghost Alligator', 'The Sapphire Horror Bat',
    ]

    def __init__(self):
        self.name = choice(self.monster_names)
        self.location = 'home'
        self.health = 100
        self.weapon = Weapon()

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

if __name__ == '__main__':
    a = Creature()
    # print([a])
    # print(a.name)
    # print(a.weapon.name)
