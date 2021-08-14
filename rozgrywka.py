# Role Play Game

# -*- coding: utf8 -*-w
import Powitanie
import Lokacje
from Postacie import obiekt1
from Postacie import obiekt2
from Postacie import obiekt3
from Postacie import obiekt4
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

Powitanie.Powitanie()
Lokacje.lokacje()

####################
# WALKA
######################################################################################################
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
