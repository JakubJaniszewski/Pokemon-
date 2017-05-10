from random import randint
from time import sleep
import csv
import os
import operator


def create_board(board_name):
    with open(board_name, "r") as maps:
        maps = maps.readlines()
        for y in range(len(maps)):
            maps[y] = list(maps[y])
    return maps


def print_board(board):
    for row in board:
        for char in row:
            print(char, end='')


def insert_player(board, width, height):
    board[height][width] = '@'
    return board


def board_change(board_name, x, y):
    os.system("clear")
    board = create_board(board_name)
    board_with_player = insert_player(board, x, y)
    print_board(board_with_player)


def window(window_name):
    os.system("clear")
    board = create_board(window_name)
    print_board(board)


def main():
    os.system("clear")
    char_alloved = [' ', 'O', '%', '★', '♺', '⚗', ',']
    gameplay(char_alloved)


def gameplay(char_alloved):
    reset_files()
    x, y = first_level(char_alloved)
    second_level(char_alloved, x, y)
    third_level(char_alloved)
    fourth_level(char_alloved)
    fifth_level(char_alloved)


def reset_files():
    inv = {'wooden stick': 1}
    export_file(inv, 'test_inventory.csv')
    stats = {'Health': 40, 'Strength': 10, 'Aglity': 10}
    export_file(stats, 'stats.csv')


def first_level(char_alloved):
    board, x, y = new_board("maps/map1.txt", 5, 26)
    map_number = 1
    while map_number == 1:
        map_number, x, y = map1_action(char_alloved, board, x, y)
    return x, y


def second_level(char_alloved, x, y):
    board, x, y = new_board("maps/map2.txt", x, y)
    map_number = 2
    while map_number == 2:
        map_number, x, y = map2_action(char_alloved, board, x, y)


def third_level(char_alloved):
    board, x, y = new_board("maps/map3.txt", 2, 3)
    map_number = 3
    while map_number == 3:
        map_number, x, y = map3_action(char_alloved, board, x, y)


def fourth_level(char_alloved):
    board, x, y = new_board("maps/map4.txt", 50, 28)
    map_number = 4
    while map_number == 4:
        map_number, x, y = map4_action(char_alloved, board, x, y)


def fifth_level(char_alloved):
    board, x, y = new_board("maps/map5.txt", 97, 27)
    map_number = 5
    while map_number == 5:
        map_number, x, y = map5_action(char_alloved, board, x, y)


def new_board(board_name, x, y):
    os.system("clear")
    board = create_board(board_name)
    board_with_player = insert_player(board, x, y)
    print_board(board_with_player)
    return board, x, y


def get_action(char_alloved, board, x, y, map_file):
    button = getch()
    if button == 'w':
        y = y - 1
        if board[y][x] not in char_alloved:
            y = y + 1
        move(x, y, map_file)

    elif button == 's':
        y = y + 1
        if board[y][x] not in char_alloved:
            y = y - 1
        move(x, y, map_file)

    elif button == 'a':
        x = x - 1
        if board[y][x] not in char_alloved:
            x = x + 1
        move(x, y, map_file)

    elif button == 'd':
        x = x + 1
        if board[y][x] not in char_alloved:
            x = x - 1
        move(x, y, map_file)

    elif button == 'i':
        inv = import_file('test_inventory.csv')[0]
        stats = import_file('stats.csv')[1]
        display_inventory(stats)
        print_table(inv, order=None)
        sleep(2.5)
        board_change('maps/map1.txt', x, y)

    elif button == "x":
        quit()

    return board, x, y, button


def map1_action(char_alloved, board, x, y):
    print(x, y)
    board, x, y, button = get_action(char_alloved, board, x, y, "maps/map1.txt")
    inv = import_file('test_inventory.csv')[0]

    if board[y][x] == '♺':
        if 'pickaxe' not in inv:
            print('need pickaxe')

        elif 'pickaxe' in inv or 'sword' in inv:
            iron_ore = ['iron ore']
            add_to_inventory(inv, iron_ore)
            board[y][x] = ','
        print(inv)

    # smith quest
    if board[y][x] == '⚗':
        x, y = back(button, x, y)

        if 'pickaxe' not in inv and 'sword' not in inv:
            print('I have a quest for you \n i need 5 iron ores')
            sleep(1)
            pickaxe = ['pickaxe']
            inv = add_to_inventory(inv, pickaxe)

        elif 'pickaxe'in inv and 'iron ore' not in inv:
            print('go hurry!')

        elif 'pickaxe'in inv and inv['iron ore'] < 5:
            print('you need 5!')

        elif 'pickaxe' in inv and inv['iron ore'] == 5:
            print('good job')
            del inv['iron ore']
            del inv['pickaxe']
            sword = ['sword']
            inv = add_to_inventory(inv, sword)

        elif 'sword' in inv:
            print('good luck')

    if board[y][x] == ',':
        print('no more ore here')

    if board[y][x] == "★":
        return 2, x, y
    else:
        return 1, x, y


def map2_action(char_alloved, board, x, y):
    print(x, y)
    board, x, y, button = get_action(char_alloved, board, x, y, "maps/map2.txt")

    if board[y][x] == "★":
        return 3, x, y
    else:
        return 2, x, y


def map3_action(char_alloved, board, x, y):
    print(x, y)
    board, x, y, button = get_action(char_alloved, board, x, y, "maps/map3.txt")

    if board[y][x] == "★":
        return 4, x, y
    else:
        return 3, x, y


def map4_action(char_alloved, board, x, y):
    print(x, y)
    board, x, y, button = get_action(char_alloved, board, x, y, "maps/map4.txt")

    if board[y][x] == "★":
        return 5, x, y
    else:
        return 4, x, y


def map5_action(char_alloved, board, x, y):
    print(x, y)
    board, x, y, button = get_action(char_alloved, board, x, y, "maps/map5.txt")

    if board[y][x] == "★":
        return 6, x, y
    else:
        return 5, x, y


def move(x, y, board_name="maps/map1.txt"):
    board = create_board(board_name)
    board_with_player = insert_player(board, x, y)
    os.system("clear")
    print_board(board_with_player)
    sleep(0.1)


def back(button, x, y):
    if button == 'w':
        y = y + 1
    elif button == 's':
        y = y - 1
    elif button == 'a':
        x = x + 1
    elif button == 'd':
        x = x - 1
    move(x, y)
    return x, y

####### INVENTORY #################


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


def export_file(inventory, filename="export_inventory.csv"):
    item_list = []

    for key, value in sorted(inventory.items()):
        for i in range(value):
            item_list.append(key)

    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=",", quotechar=",", quoting=csv.QUOTE_MINIMAL)
        writer.writerow(item_list)


def import_file(filename="import_inventory.csv"):
    inventory = {"wooden stick": 1}
    stats = {"Health": 40, "Strenght": 10, "Agility": 10}
    with open(filename, newline='') as csvfile:
        inv_csv = csv.reader(csvfile, delimiter=',',
                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for row in inv_csv:
            inventory_list = row

        for item in inventory_list:
            if item not in inventory:
                value = inventory_list.count(item)
                inventory[item] = value
                inventory_list = [count for count in inventory_list if count != item]
    return inventory, stats


def print_table(inventory, order=None):
    sum = 0
    keys = []
    values = []
    for key, value in sorted(inventory.items()):
        keys.append(key)
        values.append(str(value))
    longest_key = (max(keys, key=len))
    longest_key_len = len(longest_key)
    longest_value = (max(values, key=len))
    longest_value_len = len(longest_value)

    print('Inventory:')
    print('  count    ' + ' ' * (longest_key_len - 9) + 'item name')
    print('-' * 11 + '-' * longest_key_len)

    for key, value in sorted(inventory.items(), key=operator.itemgetter(1), reverse=True):
        sum += value
        print(' ' * (7 - len(str(value))) + str(value) + ' ' * 4 + ' ' * (longest_key_len - len(key)) + key)
    print('-' * 11 + '-' * longest_key_len)
    print('Total number of items: ' + str(sum))


def display_inventory(inventory):
    sum = 0
    for key, value in sorted(inventory.items(), key=operator.itemgetter(1), reverse=True):
        sum += value
        print(key, ':', value, end=' | ')
    print('\n')


##########################################
def getch():
    import sys
    import tty
    import termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


if __name__ == "__main__":
    main()
