class Inventory:

    def __init__(self, name, area, store_number, inventory, space_or_select, money, equip):
        self.name = name
        self.area = area
        self.store_number = store_number
        self.inventory = inventory
        self.space_or_select = space_or_select
        self.money = money
        self.equip = equip

    def info(self):
        return self.name, self.store_number, self.inventory, self.money


Player = Inventory("", 0, 0, [], 25, 0, [])
StuffnThings = Inventory("Stuff 'n' Things", 1, 1, [], 0, 0, [])
Wilkinsons = Inventory("Wilkinson's", 2, 2, [], 0, 0, [])
Straitfromtheport = Inventory("Strait from the port", 3, 3, [], 0, 0, [])
BelathorsGoods = Inventory("Belathor's Goods", 4, 4, [], 0, 0, [])
Cassiesoddsandends = Inventory("Cassie's odds and ends", 5, 5, [], 0, 0, [])
TheKrustyKrab = Inventory("The Krusty Krab", 1, 6, [], 0, 0, [])
NosferatuINC = Inventory("Nosferatu INC", 2, 7, [], 0, 0, [])
TheWhitePhial = Inventory("The White Phial", 3, 8, [], 0, 0, [])
Marcussyeoldeimporium = Inventory("Marcus's ye olde imporium", 4, 9, [], 0, 0, [])
HOLEMart = Inventory("HOLE Mart", 5, 10, [], 0, 0, [])


shop_list = [
    StuffnThings,
    Wilkinsons,
    Straitfromtheport,
    BelathorsGoods,
    Cassiesoddsandends,
    TheKrustyKrab,
    NosferatuINC,
    TheWhitePhial,
    Marcussyeoldeimporium,
    HOLEMart,
]
