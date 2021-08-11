def Postacie():
    # KLASY
    ##########################################################################################

    class Mag:
        name = ""
        hp = int
        power = int
        mana = int
        strength = int
        spell1 = int
        spell2 = int
        level = int

    class Knight:
        name = ""
        hp = int
        power = int
        strength = int
        attack1 = int
        attack2 = int
        level = int
        armor = int

    # POSTACIE
    ###########################################################################################

    obiekt1 = Mag()
    obiekt1.name = "Alfons"
    obiekt1.level = 1
    obiekt1.power = 10
    obiekt1.mana = 50
    obiekt1.strength = 20
    obiekt1.spell1 = 15
    obiekt1.spell2 = 15
    obiekt1.hp = 200 + obiekt1.level

    obiekt2 = Mag()
    obiekt2.name = "Girham"
    obiekt2.level = 1
    obiekt2.power = 10
    obiekt2.mana = 50
    obiekt2.strength = 20
    obiekt2.spell2 = 15
    obiekt2.spell2 = 15
    obiekt2.hp = 200 + obiekt2.level

    obiekt3 = Knight()
    obiekt3.name = "Eryck"
    obiekt3.level = 1
    obiekt3.power = 15
    obiekt3.armor = 50
    obiekt3.strength = 25
    obiekt3.attack1 = 25
    obiekt3.attack2 = 25
    obiekt3.hp = 200 + obiekt1.level * 0.10 + obiekt3.armor

    obiekt4 = Knight()
    obiekt4.name = "sir Roger"
    obiekt4.level = 1
    obiekt4.power = 15
    obiekt4.armor = 50
    obiekt4.strength = 25
    obiekt4.attack1 = 25
    obiekt4.attack2 = 25
    obiekt4.hp = 200 + obiekt1.level * 0.10 + obiekt3.armor
