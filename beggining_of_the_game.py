import os
import csv
import getch


def welcome_screen():
    button = ""
    while not button == "s":
        display_screen("screens/Welcome.txt")
        button = getch.getch()
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
        button = getch.getch()


def help_screen():
    button = ""
    while not button == "x":
        display_screen("screens/Help.txt")
        button = getch.getch()


def character_creation():
    button = ""
    allowed_to_press = ["1", "2", "3", "4", "5"]
    while button not in allowed_to_press:
        display_screen("screens/Character_creation1.txt")
        button = getch.getch()

    character = get_character(button)
    button = ""

    while button not in allowed_to_press:
        display_screen("screens/Character_creation2.txt")
        button = getch.getch()

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


def display_screen(filename):
    os.system("clear")
    with open(filename, "r") as f:
        screen = f.read()
    print(screen)


def set_color(board):
    blue = "\033[1;34m"
    red = "\033[1;31m"
    green = "\033[0;32m"
    yellow = "\033[0;33m"
    cyan = "\033[1;36m"
    off = "\033[0;0m"

    for i in range(len(board)):
        for index in range(len(board[i])):
            if board[i][index] == "🌊":
                board[i][index] = blue + "🌊" + off
                surf = board[i][index]

            if board[i][index] == "#":
                board[i][index] = green + "#" + off
                hash_character = board[i][index]

            if board[i][index] == "⤩":
                board[i][index] = red + "⤩" + off
                blades = board[i][index]

            if board[i][index] == "♕":
                board[i][index] = yellow + "♕" + off
                crown = board[i][index]

            if board[i][index] == "(":
                board[i][index] = cyan + "(" + off
                parenthesis1 = board[i][index]

            if board[i][index] == ")":
                board[i][index] = cyan + ")" + off
                parenthesis2 = board[i][index]

            if board[i][index] == "★":
                board[i][index] = yellow + "★" + off
                star = board[i][index]

    return board
