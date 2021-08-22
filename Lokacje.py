# LOKACJE
############################################################################################################
designation = {0: "Stoisz w małym ciemnym pomieszczeniu.\n"
                    "Na ścianach wiszą jakiś niewyraźne obrazy. \n"
                    "W rogu stoi niewielki stolik, obok przy ścianie proste drewniane łóżko.\n",
               1: "W miejscu w którym jesteś migocze ciemne, niewyraźne światło, \n"
                  "dlatego ciężko określić co to za pomieszczenie . \n"
                    "Wygląda na to że walka lub ucieczka są nieuniknione",
               2: "Jasna ogromna sala."
               }


class Location:
    def __init__(self, designation, coordinates, exits,):
        self.designation = designation
        self.coordinates = int(coordinates)
        self.exits = int(exits)

    def current_location(self):
        print(location0.designation)

    def go_north(self):
        pass

    def go_south(self):
        pass

    def go_east(self):
        pass

    def go_west(self):
        pass

    def take(self):
        pass


location0 = Location(designation[0], coordinates=0,
                     exits=1)

location1 = Location(designation[1], coordinates=0,
                     exits=2)

location2 = Location(designation[2], coordinates=0,
                     exits=2)
