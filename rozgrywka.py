# Role Play Game

# -*- coding: utf8 -*-w
########################### IMPORTY
import time
import Powitanie
from Lokacje import story
from Postacie import obiekt1, obiekt2, obiekt3, obiekt4, obiekt5
from Postacie import Monster
# import Logi
############################ ZMIENNE
p = ""
name = ""
player1 = ""
log = {}
enemy = ""

############################## WYBÓR POSTACI
p1 = input("Gracz 1. Wybierz postać \nA. Alfons \nB. Girham \nC. Erick \nD. sir Roger ")

if p1 == "a":
    player1 = obiekt1
    print("\n Gracz 1 wybiera: \n" + obiekt1.name + "a")
elif p1 == "b":
    player1 = obiekt2
    print("\n Gracz 1 wybiera: \n" + obiekt2.name + "a")
elif p1 == "c":
    player1 = obiekt3
    print("\n Gracz 1 wybiera: \n" + obiekt3.name + "a")
elif p1 == "d":
    player1 = obiekt4
    print("\n Gracz 1 wybiera: \n" + obiekt4.name + "a")

########################## HISTORIA
Powitanie.Powitanie()
time.sleep(1)
print(story[1])
time.sleep(1)
######################################## WALKA

interakcja1 = input("Co robisz? \n\n atakujesz a \n czy \nUciekasz u \n")

if interakcja1 == "a":
    enemy = obiekt5
    Monster.atak1(Monster, player1, obiekt5)

elif interakcja1 == "u":
    print("Uciekłes")




