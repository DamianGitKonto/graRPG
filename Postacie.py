
# KLASY
##########################################################################################



class Mag:
    def __init__(self, name, hp, power, mana, strength,
                 spell1, spell2, level):

        self.name = name
        self.hp = int(hp)
        self.power = int(power)
        self.mana = int(mana)
        self.strength = int(strength)
        self.spell1 = int(spell1)
        self.spell2 = int(spell2)
        self.level = int(level)


class Knight:
    def __init__(self, name, hp, power, mana, strength,
                 spell1, spell2, level):

        self.name = name
        self.hp = int(hp)
        self.power = int(power)
        self.mana = int(mana)
        self.strength = int(strength)
        self.spell1 = int(spell1)
        self.spell2 = int(spell2)
        self.level = int(level)


class Monster:
    def __init__(self, name, hp, power, mana, strength,
                 spell1, spell2, level):
        self.name = name
        self.hp = int(hp)
        self.power = int(power)
        self.mana = int(mana)
        self.strength = int(strength)
        self.spell1 = int(spell1)
        self.spell2 = int(spell2)
        self.level = int(level)


# POSTACIE
###########################################################################################

obiekt1 = Mag("Alfons", 200, 10, 50, 20, 15, 15, 2)
obiekt2 = Mag("Girham", 200, 10, 50, 20, 15, 15, 2)
obiekt3 = Knight("Eryck", 200, 10, 50, 20, 15, 15, 2)
obiekt4 = Knight("sir Roger", 200, 10, 50, 20, 15, 15, 2)
obiekt5 = Monster("Ghoul", 100, 5, 1, 10, 5, 5, 1)




