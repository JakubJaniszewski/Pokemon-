import csv


def reset_files():
    inv = {'wooden stick': 1}
    export_file(inv, 'test_inventory.csv')
    stats = {"Health": 40, "Max health": 40, "Strength": 10, "Agility": 10, "Exp": 0, "Level": 1}
    export_file(stats, 'stats.csv')


def add_to_inventory(inventory, added_items):
    keys = []
    for key, value in sorted(inventory.items()):
        keys.append(key)
    for item in added_items:
        for key, value in sorted(inventory.items()):
            if item == key:
                inventory[key] = value + 1
            elif item not in keys:
                inventory[item] = 1
                keys.append(item)
    export_file(inventory, 'test_inventory.csv')


def add_to_stats(stat, health, max_health, strength, agility, exp, level):
    stat['Health'] += health
    stat['Max health'] += max_health
    stat['Strength'] += strength
    stat['Agility'] += agility
    stat['Exp'] += exp
    stat['Level'] += level
    export_file(stat, 'stats.csv')


def export_file(inventory, filename="export_inventory.csv"):
    item_list = []

    for key, value in sorted(inventory.items()):
        for i in range(value):
            item_list.append(key)

    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=",", quotechar=",", quoting=csv.QUOTE_MINIMAL)
        writer.writerow(item_list)


def import_inventory(filename="import_inventory.csv"):
    inventory = {'wooden stick': 1}

    with open(filename, newline='') as csvfile:
        inv_csv = csv.reader(csvfile, delimiter=',',
                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for row in inv_csv:
            file_list = row

        for item in file_list:
            if item not in inventory:
                value = file_list.count(item)
                inventory[item] = value
                file_list = [count for count in file_list if count != item]

    return inventory


def import_stats(filename="stats.csv"):
    stats = {"Health": 40, "Max health": 40, "Strength": 10, "Agility": 10, "Exp": 0, "Level": 1}

    with open(filename, newline='') as csvfile:
        inv_csv = csv.reader(csvfile, delimiter=',',
                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for row in inv_csv:
            file_list = row

        for item in file_list:
            value = file_list.count(item)
            stats[item] = value

    return stats


def level_up(exp, level):
    stats = import_stats('stats.csv')
    if level == 1:
        if exp >= 100:
            add_to_stats(stats, 0, 10, 4, 4, 0, 1)
    elif level == 2:
        if exp >= 250:
            add_to_stats(stats, 0, 15, 6, 6, 0, 1)
    elif level == 3:
        if exp >= 500:
            add_to_stats(stats, 0, 20, 8, 8, 0, 1)
    elif level == 4:
        if exp >= 1000:
            add_to_stats(stats, 0, 25, 10, 10, 0, 1)
