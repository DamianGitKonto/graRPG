# Role Play Game

# -*- coding: utf8 -*-w
import time
import Ataki
import Powitanie
from Lokacje import story
from Postacie import obiekt1
from Postacie import obiekt2
from Postacie import obiekt3
from Postacie import obiekt4
from Postacie import obiekt5



p = ""

p1 = input("Gracz 1. Wybierz postać \nA. Alfons \nB. Girham \nC. Erick \nD. sir Roger ")


if p1 == "a":
    player1 = obiekt1
    print("Gracz 1 wybiera Alfonsa \n")
elif p1 == "b":
    player1 = obiekt2
    print("Gracz 1 wybrał Girhama \n")
elif p1 == "c":
    player1 = obiekt3
    print("Gracz 1 wybiera Ericka \n")
elif p1 == "d":
    player1 = obiekt4
    print("Gracz 1 wybrał sir Rogera \n")


# Drugi gracz chwilowo jest zablokowany
# p2 = input("Gracz 2 Wybierz postać \nA. Alfons \nB. Girham \nC. Erick \nD. sir Roger ")
# if p2 == "a":
#    p2 = p
#    print("Gracz 2 wybrał Alfonsa \n")
# if p2 == "b":
#    p2 = p
#    print("Gracz 2 wybrał Girhama \n")
# elif p2 == "c":
#   p2 = p
#    print("Gracz 1 wybiera Ericka \n")
# elif p2 == "d":
#    p2 = p
#    print("Gracz 1 wybrał sir Rogera \n")

Powitanie.Powitanie()
time.sleep(3)
print(story[1])
time.sleep(3)
####################
# WALKA
######################################################################################################
interakcja1 = input("Co robisz? \n\nWalczysz w \n czy \nUciekasz u \n")

if interakcja1 == "w":
    Ataki.atak1()
    Ataki.atak2()


elif interakcja1 == "u":
    print("Uciekłes")
else:
    print("Nie możesz tu tego zrobić")
