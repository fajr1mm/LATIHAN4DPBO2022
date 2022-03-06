from ship import ship
from airplane import airplane


o_ship = [ship("Queen Mary 2", "Solar", "2695", "Ocean liner", "19 years old", "United Kingdom", "Southhampton", "345 M", "Carnival Corporation"),
    ship("Freedom of the seas", "Solar", "4515", "Freedom-class cruise ship", "17 years old", "Finlandia", "Nassau Bahamas", "337 M", "Royal aribbean cruise")]

o_airplane = [airplane("Antonov An-225 Mriya", "Avtur", "6", "argo freight aircraft", "34 years old", "Ukraine", "An - 225", "92 km/H", "21 December 1988"),
airplane("Nippon Cargo", "Avtur", "0", "Cargo", "12 years old", "USA", "747-8F", "300km/H", "8 Februari 2010")]


print("----------------------S H I P--------------------")
for i in range(2):
    print(o_ship[i].printShip())

print("-------------------A I R  P L A N E--------------")
for i in range (2):
    print(o_airplane[i].printAirplane())

