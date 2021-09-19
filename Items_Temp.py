class Items:

    def __init__(self, item_number, store_assign, amount, name, price, what_type, select):
        self.item_number = item_number
        self.store_assign = store_assign
        self.amount = amount
        self.name = name
        self.price = price
        self.what_type = what_type
        self.select = select

    def info(self):
        return self.item_number, self.store_assign, self.amount, self.name, self.price, self.what_type, self.select


egg = Items(0, 1, 0, "egg", 0, 0, 0)
bread = Items(1, 2, 0, "bread", 0, 0, 0)
wheat = Items(2, 3, 0, "wheat", 0, 0, 0)
flour = Items(3, 4, 0, "flour", 0, 0, 0)
milk = Items(4, 5, 0, "milk", 0, 0, 0)
cheese = Items(5, 6, 0, "cheese", 0, 0, 0)
venison = Items(6, 7, 0, "venison", 0, 0, 0)
apple = Items(7, 8, 0, "apple", 0, 0, 0)
peach = Items(8, 9, 0, "peach", 0, 0, 0)
hamhock = Items(9, 10, 0, "ham hock", 0, 0, 0)
pear = Items(10, 1, 0, "pear", 0, 0, 0)
nuts = Items(11, 2, 0, "nuts", 0, 0, 0)
turnip = Items(12, 3, 0, "turnip", 0, 0, 0)
radish = Items(13, 4, 0, "radish", 0, 0, 0)
squash = Items(14, 5, 0, "squash", 0, 0, 0)
fish = Items(15, 6, 0, "fish", 0, 0, 0)
tackle = Items(16, 7, 0, "tackle", 0, 0, 0)
net = Items(17, 8, 0, "net", 0, 0, 0)
potionbase = Items(18, 9, 0, "potion base", 0, 0, 0)
onion = Items(19, 10, 0, "onion", 0, 0, 0)
frog = Items(20, 1, 0, "frog", 0, 0, 0)
chicken = Items(21, 2, 0, "chicken", 0, 0, 0)
yam = Items(22, 3, 0, "yam", 0, 0, 0)
lizard = Items(23, 4, 0, "lizard", 0, 0, 0)
treebark = Items(24, 5, 0, "tree bark", 0, 0, 0)
potato = Items(25, 6, 0, "potato", 0, 0, 0)
barley = Items(26, 7, 0, "barley", 0, 0, 0)
rye = Items(27, 8, 0, "rye", 0, 0, 0)
celery = Items(28, 9, 0, "celery", 0, 0, 0)
butter = Items(29, 10, 0, "butter", 0, 0, 0)
pineapple = Items(30, 1, 0, "pineapple", 0, 0, 0)
travelcake = Items(31, 2, 0, "travel cake", 0, 0, 0)
pemmican = Items(32, 3, 0, "pemmican", 0, 0, 0)
bannock = Items(33, 4, 0, "bannock", 0, 0, 0)
brusselssprouts = Items(34, 5, 0, "brussels sprouts", 0, 0, 0)
berries = Items(35, 6, 0, "berries", 0, 0, 0)
partridge = Items(36, 7, 0, "partridge", 0, 0, 0)
duck = Items(37, 8, 0, "duck", 0, 0, 0)
pork = Items(38, 9, 0, "pork", 0, 0, 0)
veal = Items(39, 10, 0, "veal", 0, 0, 0)
Pie = Items(40, 1, 0, "Pie", 0, 0, 0)
Steak = Items(41, 2, 0, "Steak", 0, 0, 0)
Burger = Items(42, 3, 0, "Burger", 0, 0, 0)
Pasta = Items(43, 4, 0, "Pasta", 0, 0, 0)
Bacon = Items(44, 5, 0, "Bacon", 0, 0, 0)
Cake = Items(45, 6, 0, "Cake", 0, 0, 0)
Dragonfruit = Items(46, 7, 0, "Dragon fruit", 0, 0, 0)
Brownie = Items(47, 8, 0, "Brownie", 0, 0, 0)
Sweetroll = Items(48, 9, 0, "Sweetroll", 0, 0, 0)
Honey = Items(49, 10, 0, "Honey", 0, 0, 0)
PreciousGem = Items(50, 1, 0, "Precious Gem", 0, 1, 0)
Silver = Items(51, 2, 0, "Silver", 0, 1, 0)
GoldBars = Items(52, 3, 0, "Gold Bars", 0, 1, 0)
Coolrock = Items(53, 4, 0, "Cool rock", 0, 1, 0)
Fancyhat = Items(54, 5, 0, "Fancy hat", 0, 1, 0)
BigassMonstertooth = Items(55, 6, 0, "Bigass Monster tooth", 0, 1, 0)
AntiqueSuperoldWine = Items(56, 7, 0, "Antique Super old Wine", 0, 1, 0)
TarotCards = Items(57, 8, 0, "Tarot Cards", 0, 1, 0)
Metalpuzzlepiece = Items(58, 9, 0, "Metal puzzle piece", 0, 1, 0)
Diamond = Items(59, 10, 0, "Diamond", 0, 1, 0)
Backpack = Items(60, 0, 0, "Backpack", 0, 2, 0)
Horse = Items(61, 0, 0, "Horse", 0, 2, 0)
Cart = Items(62, 0, 0, "Cart", 0, 2, 0)
Torch = Items(63, 0, 0, "Torch", 0, 2, 0)
Tent = Items(64, 0, 0, "Tent", 0, 2, 0)


all_items_list = [
    egg,
    bread,
    wheat,
    flour,
    milk,
    cheese,
    venison,
    apple,
    peach,
    hamhock,
    pear,
    nuts,
    turnip,
    radish,
    squash,
    fish,
    tackle,
    net,
    potionbase,
    onion,
    frog,
    chicken,
    yam,
    lizard,
    treebark,
    potato,
    barley,
    rye,
    celery,
    butter,
    pineapple,
    travelcake,
    pemmican,
    bannock,
    brusselssprouts,
    berries,
    partridge,
    duck,
    pork,
    veal,
    Pie,
    Steak,
    Burger,
    Pasta,
    Bacon,
    Cake,
    Dragonfruit,
    Brownie,
    Sweetroll,
    Honey,
    PreciousGem,
    Silver,
    GoldBars,
    Coolrock,
    Fancyhat,
    BigassMonstertooth,
    AntiqueSuperoldWine,
    TarotCards,
    Metalpuzzlepiece,
    Diamond,
    Backpack,
    Horse,
    Cart,
    Torch,
    Tent,
]
