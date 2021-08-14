
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


# POSTACIE
###########################################################################################

obiekt1 = Mag("Alfons", 1, 200, 10, 50, 20, 15, 15)
obiekt2 = Mag("Girham", 1, 200, 10, 50, 20, 15, 15)
obiekt3 = Knight("Eryck", 1, 200, 10, 50, 20, 15, 15)
obiekt4 = Knight("sir Roger", 1, 200, 10, 50, 20, 15, 15)




