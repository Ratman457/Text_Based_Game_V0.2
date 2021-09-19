class Locations:

    def __init__(self, name, area, money):
        self.name = name
        self.area = area
        self.money = money


Oakvale = Locations("Oakvale", 1, 0)
Lumbridge = Locations("Lumbridge", 2, 0)
Targovishta = Locations("Targovishta", 3, 0)
Whiterun = Locations("Whiterun", 4, 0)
LasVegas = Locations("Las Vegas", 5, 0)

places = [
    Oakvale,
    Lumbridge,
    Targovishta,
    Whiterun,
    LasVegas,
]
