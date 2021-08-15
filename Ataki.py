

from Postacie import obiekt1
from Postacie import obiekt2
from Postacie import obiekt3
from Postacie import obiekt4
from Postacie import obiekt5
from rozgrywka import player1

# Ghoul Atak


def atak1():
    player1.hp -= obiekt5.power
    print("Ghoul bierze zamach wielką łapą i masakruje Twoje ramię pazurami")
    print("Masz {} HP ".format(player1.hp))


def atak2():
    print("Szybkim ruchem Goul wpada na Ciebie zębami wgryza się w Twoją nogę")
    player1.hp -= obiekt5.spell1
    print("Masz {} HP ".format(player1.hp))
