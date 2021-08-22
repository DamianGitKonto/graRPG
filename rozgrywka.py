# Role Play Game

# -*- coding: utf8 -*-w
########################### IMPORTY
import time
import Powitanie
from Lokacje import Location, location0, location1, location2, designation
from Postacie import obiekt1, obiekt2, obiekt3, obiekt4, obiekt5, Monster, Knight, Mag
# import Komendy
# import Logi
############################ ZMIENNE
p = ""
name = ""
player1 = ""
log = {}
enemy = ""

############################## WYBÓR POSTACI
p1 = input("Gracz 1. Wybierz postać \nA. Alfons \nB. Girham \nC. Erick \nD. sir Roger ")
while p1 == "a" or "b" or "c" or "d":
    if p1 == "a":
        player1 = obiekt1
        print("\n Gracz 1 wybiera: \n" + obiekt1.name + "a")
        break
    elif p1 == "b":
        player1 = obiekt2
        print("\n Gracz 1 wybiera: \n" + obiekt2.name + "a")
        break
    elif p1 == "c":
        player1 = obiekt3
        print("\n Gracz 1 wybiera: \n" + obiekt3.name + "a")
        break
    elif p1 == "d":
        player1 = obiekt4
        print("\n Gracz 1 wybiera: \n" + obiekt4.name + "a")
        break
    elif p1 != "a" or "b" or "c" or "d":
        p1 = input("Nie ma takiej opcji. Spróbuj jeszcze raz")






########################## HISTORIA
Powitanie.Powitanie()
time.sleep(1)
Location.current_location(location0)
time.sleep(1)

######################################## WALKA

# interakcja1 = input("Co robisz? \n\n atakujesz a \n czy \nUciekasz u \n")
# interakcja2 = input("Użyj komendy 'zabij'")
print()
######################### KOMENDY


def komendy():
    player_command = input("podaj komende")
    while player_command == "zabij" or "uciekaj" or "porozmawiaj":
        if player_command == "zabij":
            enemy = obiekt5
            Knight.atak1(player1, player1, enemy)
            break
        elif player_command == "uciekaj":
            print("uff udało Ci się uciec!")
            break
        elif player_command == "porozmawiaj":
            enemy = obiekt5
            print(f"Próbujesz rozmawiać z  {enemy.name}em , jednak widząc jego głupią minę stwierdzasz,\n"
                  f" że nie ma to sensu ")
            break
        elif player_command != "zabij" or "uciekaj" or "porozmawiaj":
            player_command = input("Nie ma takiej komendy!")


komendy()

# if interakcja2 == "zabij":
#     enemy = obiekt5
#     Monster.atak1(enemy, player1, enemy)
#     time.sleep(3)
#     Knight.atak1(player1, player1, enemy)
#     time.sleep(3)
#     Monster.atak2(enemy, player1, enemy)
#
# elif interakcja1 == "u":
#     print("Uciekłes")




