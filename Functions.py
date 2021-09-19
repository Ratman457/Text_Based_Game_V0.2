# This file holds all of the functions
def initialize():  # This writes the information from .Config.txt files and writes out data in .Temp.py files
    # This section reads the Locations_Config.txt and writes to Locations_Temp.py
    place_names_file = open("Locations_Config.txt", "r")
    place_name_list = place_names_file.readlines()
    loc_temp_file = open("Locations_Temp.py", "w")
    loc_temp_file.write('')
    loc_temp_file.close()
    loc_temp_file = open("Locations_Temp.py", "a")
    loc_temp_file.write('class Locations:\n\n    def __init__(self, name, area, money):\n        '
                        'self.name = name\n        self.area = area\n        self.money = money\n\n\n')
    area_code = 1
    for place_names in place_name_list:  # This loop writes from Locations_Config.txt
        place_init = newline_remover(place_names)
        place_name = newline_space_remover(place_names)
        if int(area_code) == 1:
            loc_temp_file.write(place_name + ' = Locations("' + place_init + '", ' + str(area_code) + ', 0)')
        else:
            loc_temp_file.write('\n' + place_name + ' = Locations("' + place_init + '", ' + str(area_code) +
                                ', 0)')
        area_code += 1
    loc_temp_file.write('\n\nplaces = [\n')
    for place_names in place_name_list:  # This writes an iterable list of all locations
        place_name = newline_space_remover(place_names)
        loc_temp_file.write('    ' + place_name + ',\n')
    loc_temp_file.write("]\n")
    place_names_file.close()
    loc_temp_file.close()
    #  This section will handle the generation of the Inventory class in Inventory_Temp.py
    inventory_temp_file = open("Inventory_Temp.py", "w")
    inventory_temp_file.write('')
    inventory_temp_file.close()
    inventory_temp_file = open("Inventory_Temp.py", "a")
    inventory_temp_file.write('class Inventory:\n\n    '
                              'def __init__(self, name, area, store_number, inventory, space_or_select, money, '
                              'equip):\n        self.name = name\n        self.area = area\n        self.store_number'
                              ' = store_number\n        self.inventory = inventory\n        self.space_or_select = '
                              'space_or_select\n        self.money = money\n        self.equip = equip\n\n    def info'
                              '(self):\n        return self.name, self.store_number, self.inventory, self.money\n\n\n'
                              'Player = Inventory("", 0, 0, [], 25, 0, [])\n')
    shop_name_file = open("Shop_Names_Config.txt")
    shop_name_list = shop_name_file.readlines()
    shop_name_file.close()
    area_code = 1
    store_assign = 1
    for shops_name in shop_name_list:  # This loop writes from Shop_Names_Config.txt
        shop_init = newline_remover(shops_name)
        shop_name = newline_space_remover(shops_name)
        inventory_temp_file.write(shop_name + ' = Inventory("' + shop_init + '", ' + str(area_code) + ', ' +
                                  str(store_assign) + ', [], 0, 0, [])\n')
        area_code += 1
        if area_code > len(place_name_list):
            area_code = 1
        store_assign += 1
    inventory_temp_file.write('\n\nshop_list = [\n')
    for shops_name in shop_name_list:  # These loops write out an iterable list in Shop_Temp.py
        shop_name = newline_space_remover(shops_name)
        inventory_temp_file.write('    ' + shop_name + ',\n')
    inventory_temp_file.write("]\n")
    inventory_temp_file.close()
    # This section reads from all 'name'_Items_Config.txt files and writes to Items_Temp.py
    item_temp_file = open("Items_Temp.py", "w")
    item_temp_file.write('')
    item_temp_file.close()
    item_temp_file = open("Items_Temp.py", "a")
    item_temp_file.write('class Items:\n\n    def __init__(self, item_number, store_assign, amount, name, price, '
                         'what_type, select):\n        self.item_number = item_number\n        '
                         'self.store_assign = store_assign\n        self.amount = amount\n        self.name = name\n'
                         '        self.price = price\n        self.what_type = what_type\n        '
                         'self.select = select\n\n    def info(self):\n        '
                         'return self.item_number, self.store_assign, self.amount, self.name, self.price, '
                         'self.what_type, self.select\n\n\n')
    food_item_file = open("Food_Items_Config.txt", "r")
    food_item_list = food_item_file.readlines()
    food_item_file.close()
    store_code = 1
    item_number_assign = 0
    for foods_name in food_item_list:  # This loop writes from Food_Items_Config.txt
        food_init = newline_remover(foods_name)
        food_name = newline_space_remover(foods_name)
        item_temp_file.write(food_name + ' = Items(' + str(item_number_assign) + ', ' + str(store_code) + ', 0, "' +
                             food_init + '", 0, 0, 0)\n')
        store_code += 1
        item_number_assign += 1
        if store_code > len(shop_name_list):
            store_code = 1
    precious_item_file = open("Precious_items_Config.txt")
    precious_item_list = precious_item_file.readlines()
    precious_item_file.close()
    store_code = 1
    for precious_items in precious_item_list:  # This loop writes from Precious_items_Config.txt
        pre_init = newline_remover(precious_items)
        pre_name = newline_space_remover(precious_items)
        item_temp_file.write(pre_name + ' = Items(' + str(item_number_assign) + ', ' + str(store_code) + ', 0, "' +
                             pre_init + '", 0, 1, 0)\n')
        store_code += 1
        item_number_assign += 1
        if store_code > len(shop_name_list):
            store_code = 1
    tool_item_file = open("Tool_Items_Config.txt")
    tool_item_list = tool_item_file.readlines()
    tool_item_file.close()
    for tools in tool_item_list:  # This loop writes from Tool_Items_Config.txt
        tool_init = newline_remover(tools)
        tool_name = newline_space_remover(tools)
        item_temp_file.write(tool_name + ' = Items(' + str(item_number_assign) + ', ' + str(0) + ', 0, "' +
                             tool_init + '", 0, 2, 0)\n')
        item_number_assign += 1
    # This section writes out an iterable list in Items_Temp.py
    item_temp_file.write('\n\nall_items_list = [\n')
    for foods_name in food_item_list:
        food_name = newline_space_remover(foods_name)
        item_temp_file.write('    ' + food_name + ',\n')
    for precious_items in precious_item_list:
        pre_name = newline_space_remover(precious_items)
        item_temp_file.write('    ' + pre_name + ',\n')
    for tools in tool_item_list:
        tool_name = newline_space_remover(tools)
        item_temp_file.write('    ' + tool_name + ',\n')
    item_temp_file.write("]\n")
    item_temp_file.close()
    # This sets all the inventory lists to contain the item numbers of all sold items
    from Inventory_Temp import shop_list
    from Items_Temp import all_items_list
    for shop in shop_list:
        for item in all_items_list:
            if int(shop.store_number) == int(item.store_assign):
                shop.inventory.append(item.item_number)
    # This sets starting values
    from Inventory_Temp import Player
    from Inventory_Temp import shop_list
    from Locations_Temp import places
    import random
    for place in places:
        place.money = random.randint(1500, 5000)
    for shop in shop_list:
        shop.money = random.randint(300, 700)
    Player.area = 1
    Player.money = random.randint(300, 500)
    Player.name = input("What would you like your name to be?\n")


def in_town():  # This loop gives you in town options
    from Inventory_Temp import Player
    from Locations_Temp import places
    response = ""
    while response != "0":
        for place in places:
            if int(place.area) == int(Player.area):
                response = ""
                print("Welcome to " + location_list("here") + ".")
                while response != "0":
                    in_a_town = open('In_a_town.txt', 'r')
                    print(in_a_town.read())
                    response = input()
                    if response == "1":
                        print("You are in " + location_list("here") + ".\nOther places include " + location_list(
                            "other") + ".")
                    elif response == "2":
                        in_a_town.close()
                        travel()
                        print("Welcome to " + location_list("here") + ".")
                    elif response == "3":
                        print("Reseting all the stores")
                        store_reset()
                    elif response == "4":
                        equipable = False
                        print("You have " + str(Player.money) + " gp.")
                        if len(Player.inventory) == 0:
                            print("Your inventory is empty.\n")
                        else:
                            print("You have these items in these amounts:")
                            for item in Player.inventory:
                                if int(item[4]) == 2 and item[0]:
                                    print('    ' + item[0] + ' ' + str(item[1]) + ' (You could equip this.)')
                                    if item[0] not in Player.equip:
                                        equipable = True
                                else:
                                    print('    ' + item[0] + ' ' + str(item[1]))
                            if equipable:
                                equip()
                            print('\n')
                        if len(Player.equip) > 0:
                            print("You have these items equipped")
                            for item in Player.equip:
                                print(item)
                            print("\n")
                    elif response == "5":
                        in_town_store()
                        print("Welcome to " + location_list("here") + ".")
                    elif response == "9":
                        status()
                    elif response == "0":
                        print("Ok.\n Goodbye!")
                    else:
                        print("That's not what I asked for.\n")
                    in_a_town.close()


def in_town_store():  # This allows the player to buy or sell stuff
    from Inventory_Temp import Player
    from Inventory_Temp import shop_list
    from Locations_Temp import places
    from Items_Temp import all_items_list
    import random
    response = ""
    area = int()
    current_shop = []
    sellable_items = []
    items_sell_prices = []
    for item in all_items_list:
        if int(item.what_type) == 0:
            items_sell_prices.append(item.price + random.randint(3, 10))
        if int(item.what_type) == 1:
            items_sell_prices.append(item.price + random.randint(25, 100))
        if int(item.what_type) == 2:
            items_sell_prices.append(item.price + random.randint(50, 100))
    for place in places:
        if int(place.area) == int(Player.area):
            area = place.area
    while response != "0":  # This is the store select
        print("What store would you like to go to?\n")
        selection = 1
        for store in shop_list:
            store.space_or_select = 0
            if int(area) == int(store.area):
                store.space_or_select = selection
                print('    (' + str(store.space_or_select) + ') ' + store.name)
                selection += 1
        response = input()
        try:
            if int(response) <= len(shop_list):
                for store in shop_list:
                    if int(response) == int(store.space_or_select):
                        current_shop = list(store.info())
                    elif str(response) == "0":
                        print("Ok.\n")
        except ValueError:
            print("That's not what I asked for.\n")
            break
        while response != "0":  # This chooses weather you are buying or selling
            try:
                print("Welcome to " + str(current_shop[0]) + "!\nWould you like to buy or sell today?")
            except IndexError or ValueError:
                print("That's not what I asked for.\n")
                break
            print("    (1) Buy\n    (2) Sell\n    (0) Never-mind")
            response = input()
            if response == "1":  # This is the start of the buy section
                while response != "0":
                    print("You have " + str(Player.money) + " gp and you have " + str(Player.space_or_select) +
                          " space left")
                    print("What would you like to buy?\nItems are arranged in name, amount, price order.\n")
                    selection = 1
                    shop_items = []
                    for item in all_items_list:
                        item.select = 0
                        if item.item_number in current_shop[2] and item.amount > 0:
                            item.select = selection
                            price_mod = int()  # Right here is where i will add the reputation mod from quests
                            print('    (' + str(item.select) + ') ' + item.name + ' ' + str(item.amount) + ' ' +
                                  str(item.price + price_mod) + ' gp')
                            selection += 1
                            shop_items.append(list(item.info()))
                    print("    (0) Never-mind\n")
                    response = input()
                    try:
                        for item_for_sale in shop_items:
                            if str(item_for_sale[6]) == str(response):
                                print("You have " + str(Player.money) + " gp and you have " + str(
                                    Player.space_or_select) +
                                      " space left")
                                amount_to_buy = input(
                                    'How many would you like to buy?\nWe have ' + str(item_for_sale[2]) +
                                    ' of the item ' + item_for_sale[3] + ' for ' + str(item_for_sale[4]) +
                                    ' gp each.\n')
                                if int(amount_to_buy) > item_for_sale[2]:
                                    print("We don't have that many (and you knew that)")
                                elif int(amount_to_buy) == 0:
                                    print("I guess you don't want to buy any.\n")
                                    break
                                else:
                                    total_price = int(item_for_sale[4]) * int(amount_to_buy)
                                    if total_price > int(Player.money):
                                        print("You cannot afford that right now.\n")
                                    elif Player.space_or_select < int(amount_to_buy):
                                        print("You don't seem to have space for that right now.\n")
                                    else:
                                        bought_items = [item_for_sale[3], amount_to_buy, item_for_sale[0], 0,
                                                        item_for_sale[5]]
                                        add_inventory([bought_items])
                                        remove_inventory_item(item_for_sale[0], int(amount_to_buy))
                                        Player.money = Player.money - int(item_for_sale[4] * int(amount_to_buy))
                                        Player.space_or_select = Player.space_or_select - int(amount_to_buy)
                                        print("You bought " + str(amount_to_buy) + " of our " + item_for_sale[
                                            3] + " for " +
                                              str(item_for_sale[4] * int(amount_to_buy)) + " gp.")
                                        print("Thank you, and please come again!\n")
                                        break
                            elif response == "0":
                                print("Ok.")
                                break
                            elif int(response) > len(shop_items):
                                print("That's not what I asked for.")
                                break
                    except ValueError:
                        print("That's not what I asked for.")
            elif response == "2":  # This is the sell section
                while response != "0":
                    if len(Player.inventory) > 0:
                        for item in Player.inventory:
                            if item[2] not in current_shop[2]:
                                sellable_items.append(item[2])
                        if len(sellable_items) > 0:
                            print("What do you want to sell today?\n")
                            selection = 1
                            for item in Player.inventory:
                                item[3] = 0
                                if item[2] not in current_shop[2]:
                                    print('    (' + str(selection) + ') ' + str(item[0]) + ' ' + item[1] + ' ' +
                                          str((items_sell_prices[item[2]])) + 'gp.')
                                    item[3] = selection
                                    selection += 1
                            print("    (0) Never-mind.\n")
                            response = input()
                            for item in Player.inventory:
                                if str(item[3]) == response:
                                    print("How many " + item[0] + " would you like to sell?\nYou have " + str(item[1]) +
                                          " of them, and I'll buy them for " + str(items_sell_prices[item[2]]) +
                                          " gp each.")
                                    response = input()
                                    if response > item[1]:
                                        print("You don't have that many (and you knew that).")
                                    else:  # The barter system would go here-ish
                                        remove_inventory_player([item[0], response])
                                        Player.space_or_select = int(Player.space_or_select) + int(response)
                                        Player.money = Player.money + int(int(items_sell_prices[item[2]]) *
                                                                          int(response))
                                        print("You sold us " + str(response) + " of your " + item[0] + " for " +
                                              str(int(items_sell_prices[item[2]]) * int(response)) + " gp.\n"
                                              "Thank you, and please come again.\n")
                            break
                        else:
                            print("It seems everything you want to sell me, I can already get somewhere else.")
                            break
                    else:
                        print("It seems you have nothing to sell, maybe you would like to buy something?")
                        break
            elif response == "0":
                print("Ok\n")
                break
            else:
                print("That's not what I asked for.")
                break


def equip():
    from Inventory_Temp import Player
    print("You have an equip-able item.\nYou could equip these items:")
    select = 1
    for item in Player.inventory:
        item[3] = 0
        if item[4] == 2:
            item[3] = select
            print('    (' + str(select) + ') ' + item[0])
    print('    (0) Never-mind')
    response = input()
    for item in Player.inventory:
        if int(response) == int(item[3]):
            print("You can equip this " + item[0] + " but this is permanent.\nAre you sure?\n    (1) Yes\n    (0) No\n")
            response = input()
            if int(response) == 1:
                Player.equip.append(item[0])
                if item[0] == "Backpack":
                    print("Backpack equipped.\nPlayer inventory size increased by 25.")
                    Player.space_or_select += 26
                elif item[0] == "Horse":
                    print("You can travel faster now. This decreases the likely-hood of random events.\n"
                          "Quest events are not affected. (None of this is implemented yet)")
                elif item[0] == "Cart":
                    print("Hopefully you have a horse (don't put your cart before the horse) or a tent.\n"
                          "You can carry significantly more now (50 more slots), but your speed is reduced.\n"
                          "This makes random events more likely, quest events are not affected\n"
                          "Currently not implemented (no not even the inventory space).")
                elif item[0] == "Torch":
                    print("This will help you see in the dark. It will go out after one use though so stock up.\n"
                          "Currently not implemented.")
                elif item[0] == "Tent":
                    print("This will allow you to sleep in-between towns. Beware of wolves, and bears and such.\n"
                          "Currently not implemented")
                else:
                    pass
                for items in Player.inventory:
                    if items[2] == item[2]:
                        remove_inventory_player([items[0], 1])
            else:
                pass
        elif response == "0":
            print("Ok.")
            break


def store_reset():  # This resets all item amounts and prices for all stores.
    import random
    from Inventory_Temp import shop_list
    from Items_Temp import all_items_list
    for shop in shop_list:
        shop.money = shop.money + random.randint(50, 200)
    for item in all_items_list:
        if int(item.what_type) == 0:
            if any(letter.isupper() for letter in item.name):
                item.price = random.randint(10, 25)
                item.amount = random.randint(2, 12)
            else:
                item.price = random.randint(5, 15)
                item.amount = random.randint(5, 25)
        elif int(item.what_type) == 1:
            item.price = random.randint(150, 300)
            if random.randint(0, 100) < 26:
                item.amount = random.randint(1, 3)
        elif int(item.what_type) == 2:
            item.price = random.randint(100, 500)
            item.amount = 1
            for shop in shop_list:  # This adds tools to random inventories
                if item.item_number in shop.inventory:
                    shop.inventory.remove(item.item_number)
                if random.randint(0, 100) < 11:
                    shop.inventory.append(item.item_number)


def newline_space_remover(word):  # This removes spaces, newlines and quote marks from the data in placename
    name_from_which_spaces_will_be_taken = ""
    for letter in word:
        if letter in "\n '":
            name_from_which_spaces_will_be_taken = name_from_which_spaces_will_be_taken + ""
        else:
            name_from_which_spaces_will_be_taken = name_from_which_spaces_will_be_taken + letter
    return name_from_which_spaces_will_be_taken


def newline_remover(word):  # This only removes newlines from data in placename
    name_from_which_spaces_will_be_taken = ""
    for letter in word:
        if letter in "\n":
            name_from_which_spaces_will_be_taken = name_from_which_spaces_will_be_taken + ""
        else:
            name_from_which_spaces_will_be_taken = name_from_which_spaces_will_be_taken + letter
    return name_from_which_spaces_will_be_taken


def location_list(which):
    from Locations_Temp import places
    from Inventory_Temp import Player
    if which == "here":
        for place in places:
            if int(place.area) == int(Player.area):
                return place.name
    elif which == "all":
        place_all = ""
        iteration = 1
        for place in places:
            if iteration <= len(places) - 2:
                place_all = place_all + place.name + ', '
            elif iteration == len(places) - 1:
                place_all = place_all + place.name + 'and '
            elif iteration == len(places):
                place_all = place_all + place.name + ' '
            iteration += 1
        return place_all
    elif which == "other":
        place_other = ""
        iteration = 1
        for place in places:
            if place.area != Player.area:
                if iteration <= len(places) - 3:
                    place_other = place_other + place.name + ', '
                elif iteration == len(places) - 2:
                    place_other = place_other + place.name + ' and '
                elif iteration == len(places) - 1:
                    place_other = place_other + place.name + ' '
                iteration += 1
        return place_other


def status():  # This lists all data for cities and the player
    from Locations_Temp import places
    from Inventory_Temp import Player
    from Inventory_Temp import shop_list
    from Items_Temp import all_items_list
    print("\nPlaces Data:")
    print("Name, area number, area money")
    for place in places:
        print('    ' + place.name + ' ' + str(place.area) + ' ' + str(place.money))
    print("\nPlayer Data:")
    print('    Player name: ' + Player.name + '\n    Current time: ' + str(Player.area) +
          '\n    Current inventory: ' + str(Player.inventory) + '\n    Player space (total): ' +
          str(Player.space_or_select) + ' slots.\n    Player money: ' + str(Player.money) + ' gold.\n')
    print("Shop Data:")
    print("Shop name, area number.")
    print("Item name, item amount, item price.\n")
    for shop in shop_list:
        print(shop.name + ', ' + str(shop.area))
        for item in all_items_list:
            if item.item_number in shop.inventory:
                print('    ' + item.name + ' ' + str(item.amount) + ' ' + str(item.price) + ' Gp')
        print("\n")


def travel():  # This changes the current Player.area
    from Locations_Temp import places
    from Inventory_Temp import Player
    print("Where would you like to go?")
    for place in places:
        print('    (' + str(place.area) + ') ' + place.name)
    where = input()
    try:
        for place in places:
            if str(place.area) == str(where) == str(Player.area):
                print("You are already in " + place.name + ".\n")
                break
            elif str(place.area) == str(where) != str(Player.area):
                Player.area = where
                print("You are now in " + place.name + ".\n")
                break
            elif int(where) > len(places):
                print("That's not what I asked for")
                break
    except ValueError:
        print("That's not what I asked for.")


def remove_inventory_player(item_removed):  # This function will remove items from an inventory.
    # This function assumes you are not removing more of an item that you already had and that you are removing
    # items that you actually have. item_removed = remove_inventory_player(["name", amount])
    from Inventory_Temp import Player
    for item_player in Player.inventory:
        if str(item_removed[0]) == str(item_player[0]):
            item_player[1] = int(item_player[1]) - int(item_removed[1])
            if int(item_player[1]) == 0:
                Player.inventory.pop(Player.inventory.index(item_player))


def remove_inventory_item(item_number, amount):
    from Items_Temp import all_items_list
    for item in all_items_list:
        if int(item.item_number) == int(item_number):
            item.amount = item.amount - int(amount)
            if item.amount < 0:
                item.amount = 0


def add_inventory(items_added):  # This adds items as a list of lists into Player.inventory.
    # This function takes items_added in this form: add_inventory([["name", amount, item number, 0, type]])
    # Make sure these things match the item list format of Items_Temp.py Items.info function minus store assign!!
    # Do not use this from player input
    # TODO This is messy as fuck input plz fix me. Maybe generalize the input for all item adds and removes
    from Inventory_Temp import Player
    if len(Player.inventory) == 0:
        for item_added in items_added:
            if int(item_added[1]) > 0:
                Player.inventory.append(item_added)
        return
    else:
        temp_player_inventory = tuple(Player.inventory)
        for item_added in items_added:
            was_item_added = False
            for item_player in temp_player_inventory:
                if str(item_player[0]) == str(item_added[0]):
                    item_player[1] = int(item_player[1]) + int(item_added[1])
                    was_item_added = True
                elif temp_player_inventory.index(item_player) == len(temp_player_inventory) - 1:
                    if not was_item_added:
                        if int(item_added[1]) > 0:
                            Player.inventory.append(item_added)
