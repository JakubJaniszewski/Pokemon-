from random import randint
from time import sleep
import csv
import os
import operator
import random


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
    with open("chosen_character.csv", "r") as f:
        f = f.read()
        chosen_character = f.split(",")
        chosen_character[-1] = chosen_character[-1].replace("\n", "")

    character = chosen_character[0]
    color = chosen_character[1]
    color = change_color(color)
    off = "\033[0;0m"

    board[height][width] = color + character + off
    return board


def change_color(color):
    if color == "yellow":
        color = "\033[1;33m"
    if color == "blue":
        color = "\033[1;34m"
    if color == "red":
        color = "\033[1;31m"
    if color == "green":
        color = "\033[0;32m"
    if color == "white":
        color = "\033[0;0m"
    return color


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
    welcome_screen()
    character_creation()
    gameplay()


def gameplay():
    char_alloved = [' ', 'O', '%', '★', '♺', '⚗', ',', '⤩', '&', '#', '~', '⍑','(',')','⯂','x']
    reset_files()
    x, y = first_level(char_alloved)
    second_level(char_alloved, x, y)
    third_level(char_alloved)
    fourth_level(char_alloved)
    fifth_level(char_alloved)


def reset_files():
    inv = {'wooden stick': 1}
    export_file(inv, 'test_inventory.csv')
    stats = {"Health": 40, "Max health": 40, "Strength": 10, "Agility": 10, "Exp": 0, "Level": 1}
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
    cord_x = [10, 13, 17, 25, 22]
    cord_y = [16, 25, 24, 19, 25]
    for i in range(5):
        board[cord_y[i]][cord_x[i]] = '~'

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
        inv = import_inventory('test_inventory.csv')
        stats = import_stats('stats.csv')
        display_stats(stats)
        print_table(inv, order=None)
        while getch().lower() != 'i':
            sleep(0.1)
        board_change(map_file, x, y)

    elif button == "x":
        quit()

    return board, x, y, button


def map1_action(char_alloved, board, x, y):
    print(x, y)
    board, x, y, button = get_action(char_alloved, board, x, y, "maps/map1.txt")
    inv = import_inventory('test_inventory.csv')
    stats = import_stats('stats.csv')
    level_up(stats['Exp'], stats['Level'])



    if board[y][x] == '♺':
        if 'pickaxe' not in inv:
            print('need pickaxe')

        elif 'pickaxe' in inv or 'sword' in inv:
            iron_ore = ['iron ore']
            add_to_inventory(inv, iron_ore)
            board[y][x] = ','

    # smith quest
    if board[y][x] == '⚗':
        x, y = back(button, x, y)

        if 'pickaxe' not in inv and 'sword' not in inv:
            print('I have a quest for you \n i need 5 iron ores')
            sleep(1)
            pickaxe = ['pickaxe']
            add_to_inventory(inv, pickaxe)

        elif 'pickaxe'in inv and 'iron ore' not in inv:
            print('go hurry!')

        elif 'pickaxe'in inv and inv['iron ore'] < 5:
            print('you need 5!')

        elif 'pickaxe' in inv and inv['iron ore'] == 5:
            print('good job')
            del inv['iron ore']
            del inv['pickaxe']
            sword = ['sword']
            add_to_inventory(inv, sword)
            add_to_stats(stats, 0, 0, 2, 0, 40, 0)

        elif 'sword' in inv:
            print('good luck')

    if board[y][x] == ',':
        print('no more ore here')

    if board[y][x] == '⤩':
        x, y = back(button, x, y)
        fight(85, 85, 15, 15, 20, x, y)
        board_change('maps/map1.txt', x, y)
        print('enemy is dead \n plus 20XP')

    if board[y][x] == '(' or board[y][x] == ')':
        stats['Health'] = stats['Max health']
        add_to_stats(stats, 0, 0, 0, 0, 0, 0)
        print('Full heal')
        sleep(0.2)

    if board[y][x] == '&':
        x, y = back(button, x, y)
        print('w ktróleswie znajdują się lecznicze źródła \n jedno z nich jest za mną, sprawdz sam')

    if 'sword' in inv:
        return 2, x, y
    else:
        return 1, x, y


def map2_action(char_alloved, board, x, y):
    print(x, y)
    board, x, y, button = get_action(char_alloved, board, x, y, "maps/map2.txt")
    inv = import_inventory('test_inventory.csv')
    stats = import_stats('stats.csv')
    level_up(stats['Exp'], stats['Level'])

    if board[y][x] == '⤩':
        x, y = back(button, x, y)
        print('stój kurwa!')
        sleep(1)
        fight(25, 25, 5, 5, 20, x, y)
        board_change('maps/map2.txt', x, y)
        print('enemy is dead \n plus 20XP')

    if board[y][x] == '⚗':
        x, y = back(button, x, y)
        board_change('maps/map2.txt', x, y)
        print('good luck')

    if board[y][x] == '(' or board[y][x] == ')':
        stats['Health'] = stats['Max health']
        add_to_stats(stats, 0, 0, 0, 0, 0, 0)
        print('Full heal')
        sleep(0.2)

    if board[y][x] == "★":
        return 3, x, y
    else:
        return 2, x, y


def map3_action(char_alloved, board, x, y):
    print(x, y)
    board, x, y, button = get_action(char_alloved, board, x, y, "maps/map3.txt")
    inv = import_inventory('test_inventory.csv')
    stats = import_stats('stats.csv')
    level_up(stats['Exp'], stats['Level'])


    if board[y][x] == '~':
        if 'bucket' in inv:
            material = ['material']
            add_to_inventory(inv, material)
            print('+1 material')
            board[y][x] = ','

    if board[y][x] == '⚗':
        x, y = back(button, x, y)
        board_change('maps/map3.txt', x, y)

        if 'bucket' not in inv and 'robe' not in inv:
            print('I have a quest for you \n i need 5 materials')
            sleep(1)
            bucket = ['bucket']
            add_to_inventory(inv, bucket)

        elif 'bucket'in inv and 'material' not in inv:
            print('pole baweły jest na zachodzie')

        elif 'bucket'in inv and inv['material'] < 5:
            print('za mało')

        elif 'bucket' in inv and inv['material'] == 5:
            print('udało ci się')
            del inv['material']
            del inv['bucket']
            robe = ['robe']
            add_to_inventory(inv, robe)
            add_to_stats(stats, 0, 10, 0, 2, 80, 0)

        elif 'robe' in inv:
            print('idz i odzyskaj tron')

    if board[y][x] == '⤩':
        x, y = back(button, x, y)
        board_change('maps/map3.txt', x, y)
        print ('dawaj leszczu')
        sleep(1)
        fight(50, 50, 10, 10, 40, x, y)
        board_change('maps/map3.txt', x, y)
        print('enemy is dead \n plus 40XP')

    if board[y][x] == '⍑':
        x, y = back(button, x, y)
        board_change('maps/map3.txt', x, y)
        print('FIGHT CLUB')

    if board[y][x] == '⯂':
        if 'robe' not in inv:
            x, y = back(button, x, y)
            board_change('maps/map3.txt', x, y)
            print('czego tu szukasz wieśniaku? ... wypierdalaj')
            sleep(0.5)
        elif 'robe' in inv:
            print('zapraszam dostojny panie')
            board[y][x] = " "
            sleep(0.5)

    if board[y][x] == 'x':
        if "robe" not in inv:
            x, y = back(button, x, y)
            board_change('maps/map3.txt', x, y)
            print('czego tu szukasz wieśniaku? ... wypierdalaj')
            sleep(0.5)
        elif "robe" in inv:
            board[y][x] = " "

    if board[y][x] == '(' or board[y][x] == ')':
        stats['Health'] = stats['Max health']
        add_to_stats(stats, 0, 0, 0, 0, 0, 0)
        print('Full heal')
        sleep(0.2)


    if board[y][x] == "★":
        return 4, x, y
    else:
        return 3, x, y


def map4_action(char_alloved, board, x, y):
    print(x, y)
    board, x, y, button = get_action(char_alloved, board, x, y, "maps/map4.txt")
    inv = import_inventory('test_inventory.csv')
    stats = import_stats('stats.csv')
    level_up(stats['Exp'], stats['Level'])

    if board[y][x] == '⚗':
        x, y = back(button, x, y)
        board_change('maps/map4.txt', x, y)

        if 'coin' not in inv and 'permit' not in inv:
            print('''Jestem gueratorem i mam glejt \n jeżeli oswobodzisz przedmieścia z rąk
            bandytów to oddam ci mój glejt \n jako dowód prznieś mi ich głowy \n
            tu masz trochę monet na zachęte''')
            sleep(1)
            coin = ['coin']*120
            add_to_inventory(inv, coin)

        elif 'coin'in inv and 'bandit head' not in inv:
            print('tam giną ludzie, spiesz się')

        elif 'coin'in inv and inv['bandit head'] < 6:
            print('to nie wszscy, tam wciąż są bandyci')

        elif 'coin' in inv and inv['bandit head'] == 6:
            print('oswobodziłeś lud, ale glejt będzie cię kosztował 120 monet')
            del inv['bandit head']
            del inv['coin']
            permit = ['permit']
            add_to_inventory(inv, permit)
            add_to_stats(stats, 0, 0, 0, 0, 250, 0)

    if board[y][x] == '⤩':
        if 'coin' in inv:
            x, y = back(button, x, y)
            board_change('maps/map4.txt', x, y)
            print ('zajebie cie!!')
            sleep(1)

            exp_before = stats['Exp']
            fight(80, 80, 15, 15, 75, x, y)
            board_change('maps/map4.txt', x, y)
            exp_after = stats['Exp']

            if exp_before - exp_after != 0:
                print('enemy is dead \n plus 75XP')
                bandit_head = ['bandit hea']
                add_to_inventory(inv, bandit_head)
                print('+1 bandit_head')
                sleep(0.5)
                board[y][x] = ','

    if board[y][x] == ',':
        x, y = back(button, x, y)
        board_change('maps/map4.txt', x, y)
        print('dead body')
        sleep(0.5)

    if board[y][x] == '⯂':
        if 'permit' not in inv:
            x, y = back(button, x, y)
            board_change('maps/map4.txt', x, y)
            print('bez okazania glejtu nikt nie przejdziesz')
            sleep(0.5)
        elif 'permit' in inv:
            board[y][x] = " "
            print('król czeka')
            sleep(0.5)

    if board[y][x] == 'x':
        if "permit" not in inv:
            x, y = back(button, x, y)
            board_change('maps/map4.txt', x, y)
            print('bez okazania glejtu nikt nie przejdziesz')
            sleep(0.5)
        elif "permit" in inv:
            board[y][x] = " "
            print('król czeka')
            sleep(0.5)

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


def fight(health, max_health, strength, agility, exp, x, y):
    window('action.txt')
    stats = import_stats('stats.csv')
    display_health(stats['Health'], stats['Max health'])

    enemy_attack_strength = int(strength * 0.5)
    enemy_attack_random = [enemy_attack_strength - 1, enemy_attack_strength, enemy_attack_strength + 1]
    enemy_dodge_chance = agility * 2

    player_attack_strength = int(stats['Strength'] * 0.5)
    player_attack_random = [player_attack_strength - 1, player_attack_strength, player_attack_strength + 1]
    plaer_dodge_chance = int(stats['Agility'] * 0.5)

    while health > 0:
        window('action.txt')
        print('Player :', end='-')
        display_health(stats['Health'], stats['Max health'])
        print('Enemy :', end='--')
        display_health(health, max_health)

        choice = input('1 : Attac | 2: Run \n')
        while not (choice == '1' or choice == '2'):
            window('action.txt')
            print('Player :', end='-')
            display_health(stats['Health'], stats['Max health'])
            print('Enemy :', end='--')
            display_health(health, max_health)
            choice = input('1 : Attac | 2: Run \n')

        if choice == '2':
            board_change('maps/map1.txt', x, y)
            break

        if choice == '1':
            dodge = randint(0, 99)
            print(dodge)
            sleep(0.5)
            if dodge <= enemy_dodge_chance:
                print('you miss')
                sleep(0.5)
            else:
                health = health - random.choice(player_attack_random)

            dodge = randint(0, 99)
            if dodge <= plaer_dodge_chance:
                print('dodge')
                sleep(0.5)
            else:
                stats['Health'] = stats['Health'] - random.choice(enemy_attack_random)

            if stats['Health'] <= 0:
                window('screens/Lose.txt')
                sleep(1.5)
                quit()

    if health <= 0:
        add_to_stats(stats, 0, 0, 0, 0, exp, 0)
    else:
        add_to_stats(stats, 0, 0, 0, 0, 0, 0)


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
    inventory = {"wooden stick": 1}

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


def display_stats(stat):
    print('Health :', stat['Health'], '/', stat['Max health'], end=' | ')
    print('Strength :', stat['Strength'], ' | ', 'Agility :',
          stat['Agility'], ' | ', 'Exp :', stat['Exp'], ' | ', 'Level :', stat['Level'])
    print('\n')


def display_health(health, max_health):
    print('Health :', health, '/', max_health)


def display_screen(filename):
    os.system("clear")
    with open(filename, "r") as f:
        screen = f.read()
    print(screen)


def welcome_screen():
    button = ""
    while not button == "s":
        display_screen("screens/Welcome.txt")
        button = getch()
        if button == "h":
            help_screen()
        if button == "c":
            credits_screen()
        if button == "x":
            os.system("clear")
            quit()


def credits_screen():
    button = ""
    while not button == "x":
        display_screen("screens/Credits.txt")
        button = getch()


def help_screen():
    button = ""
    while not button == "x":
        display_screen("screens/Help.txt")
        button = getch()


def character_creation():
    button = ""
    allowed_to_press = ["1", "2", "3", "4", "5"]
    while button not in allowed_to_press:
        display_screen("screens/Character_creation1.txt")
        button = getch()

    character = get_character(button)
    button = ""

    while button not in allowed_to_press:
        display_screen("screens/Character_creation2.txt")
        button = getch()

    color = get_color(button)

    choices_list = [character, color]
    with open("chosen_character.csv", 'w', newline='') as f:
        writer = csv.writer(f, delimiter=",", quotechar=",", quoting=csv.QUOTE_MINIMAL)
        writer.writerow(choices_list)



def get_character(button):
    if button == "1":
        character = "@"
    if button == "2":
        character = "⛹"
    if button == "3":
        character = "§"
    if button == "4":
        character = "ᾥ"
    if button == "5":
        character = "⛄"

    return character


def get_color(button):
    if button == "1":
        color = "blue"
    if button == "2":
        color = "yellow"
    if button == "3":
        color = "green"
    if button == "4":
        color = "red"
    if button == "5":
        color = "white"

    return color

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
