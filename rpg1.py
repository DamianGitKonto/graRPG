# Role Play Game

# -*- coding: utf8 -*-
p = ""

p1 = input("Gracz 1. Wybierz postać \nA. Alfons \nB. Girham \nC. Erick \nD. sir Roger ")
if p1 == "a":
    print("Gracz 1 wybiera Alfonsa \n")
elif p1 == "b":
    print("Gracz 1 wybrał Girhama \n")
elif p1 == "c":
    print("Gracz 1 wybiera Ericka \n")
elif p1 == "d":
    print("Gracz 1 wybrał sir Rogera \n")


p2 = input("Gracz 2 Wybierz postać \nA. Alfons \nB. Girham \nC. Erick \nD. sir Roger ")
if p2 == "a":
    p2 = p
    print("Gracz 2 wybrał Alfonsa \n")
if p2 == "b":
    p2 = p
    print("Gracz 2 wybrał Girhama \n")
elif p2 == "c":
    p2 = p
    print("Gracz 1 wybiera Ericka \n")
elif p2 == "d":
    p2 = p
    print("Gracz 1 wybrał sir Rogera \n")


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

# WALKA
######################################################################################################

print(" Stoisz w wielkiej sali kolumnowej, jest tu dość jasno i bogato, na śwodku sali stoi Twój przeciwnik ")
print(p)

interakcja1 = input("Co robisz? \n\nWalczysz w \n czy \nUciekasz u \n")

if interakcja1 == "w":
    obiekt2.hp -= 5
    print(obiekt2.hp)

if interakcja1 == "u" and obiekt2.power + obiekt2.level * 0.15 > obiekt1.strength:
    print("Uciekłes")
else:
    obiekt2.hp -= obiekt1.power + obiekt1.spell1
    print("Dostałeś kulą ognia traciesz {}".format(obiekt1.power + obiekt1.spell1))
    print("Masz {} HP ".format(obiekt2.hp))
