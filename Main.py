'''
TODO Add welcome function --
TODO Think of a name for this game
TODO Add descriptions and plural names for all items (pain in the ass)
TODO Check all functions for handling of improper inputs (ongoing for new player handled functions)
TODO Add 'time' system (make travel cost time) (add day tracker) --
TODO Make store inventory reset every day not everytime you enter a store. --
TODO Make the money system more complicated (reasons)
TODO Add a hunger system for player (something to do with food other than sell it. Capital letter food is better.) --
TODO Expand travel system to include events (add events)
TODO Create combat system (weapons, armor, enemies its gonna suck)
TODO Create quest system (also generate city money value for quest rewards or something) (Reputation levels)
TODO Create Apothecary (and potions)
TODO Add description capability to items and cities
TODO Add a tavern in each town open at any time as a special store (with interact-able patrons maybe) --
'''

from Functions import initialize

from Functions import store_reset

from Functions import in_town


initialize()
store_reset()
in_town()
