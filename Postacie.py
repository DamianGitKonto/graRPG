# KLASY
##########################################################################################


class Characters:
    def __init__(self, name, hp, power, strength, level):
        self.name = name
        self.hp = int(hp)
        self.power = int(power)
        self.strength = int(strength)
        self.level = int(level)


class Mag (Characters):
    def __init__(self, name, hp, power, strength, level, mana):
        super().__init__(name, hp, power, strength, level)
        self.mana = int(mana)

    # def spell1(self):
    #     log[bot_hp] -= self.mana + self.power

    def spell2(self):
        pass


class Knight (Characters):
    def __init__(self, name, hp, power, strength, level, armor):
        super().__init__(name, hp, power, strength, level)
        self.armor = int(armor)

    # def atak3():
    #     szybkie_ciecie = -10

    def attack1(self):
        pass

    def attack2(self):
        pass


class Monster (Characters):
    def __init__(self, name, hp, power, strength, level):
        super().__init__(name, hp, power, strength, level)

    def atak1(self):
        player1.hp -= obiekt5.power
        print("Ghoul bierze zamach wielką łapą i masakruje Twoje ramię pazurami")
        print("Masz {} HP ".format(player.hp))
    #
    # def atak2():
    #     print("Szybkim ruchem Goul wpada na Ciebie zębami wgryza się w Twoją nogę")
    #     player1.hp -= obiekt5.spell1
    #     print("Masz {} HP ".format(player1.hp))

    def skill1(self):
        pass

    def skill2(self):
        pass

# POSTACIE
###########################################################################################


obiekt1 = Mag(name="Alfons",
              hp=200,
              power=10,
              strength=50,
              level=20,
              mana=15)

obiekt2 = Mag(name="Girham",
              hp=200,
              power=10,
              strength=50,
              level=20,
              mana=2)

obiekt3 = Knight(name="Eryck",
                 hp=200,
                 power=10,
                 strength=50,
                 level=20,
                 armor=2)

obiekt4 = Knight(name="sir Roger",
                 hp=200,
                 power=10,
                 strength=50,
                 level=20,
                 armor=2)

obiekt5 = Monster(name="Ghoul",
                  hp=200,
                  power=10,
                  strength=50,
                  level=20)





