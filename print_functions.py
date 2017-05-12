import operator
import os


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


def display_screen(filename):
    os.system("clear")
    with open(filename, "r") as f:
        screen = f.read()
    print(screen)
