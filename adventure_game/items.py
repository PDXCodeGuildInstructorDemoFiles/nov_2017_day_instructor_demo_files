from random import choice, randint

class Weapon:
    weapon_names = [
        "Nightmare", "Lifebender", "Shadowfall", "Hysteria", "Knight's Crux",
        "Fusion Fan", "Frail Idol", "Frostguard, Focus of Grieving Widows",
        "Snowflake, Seal of the Lone Victor", "Frostward, Globule of Wraiths",
    ]
    def __init__(self):
        self.name = choice(self.weapon_names)
        self.speed = randint(1, 5)
        self.damage = randint(10, 20)
        self.dps = self.damage * self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

class Potion:
    potion_names = [
        "Draught of Rose Petals", "Vial of Rejuvenation",
        "Philter of Intuition", "Phial of Enhanced Sight", "Draught of Demons",
        "Phial of Caution", "Elixir of Protection", "Potion of the Archer",
        "Vial of Smoke", "Elixir of Fireworks",
    ]

    def __init__(self):
        self.name = choice(self.potion_names)
        self.restore = randint(5, 50)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()
