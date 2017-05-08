from random import randint
from time import sleep
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def create_board(width, height):
    with open("maps.txt", "r") as maps:
        map1 = maps.readlines()
        for y in range(len(map1)):
            map1[y] = list(map1[y])
    return map1


def print_board(board):
    for row in board:
        for char in row:
            print(char, end='')


def insert_player(board, width, height):
    board[height][width] = '⛹'
    return board


def main():

    x = 40
    y = 10
    os.system("clear")
    board = create_board(60, 20)
    board_with_player = insert_player(board, x, y)
    print_board(board_with_player)

    while True:
        print(x, y)
        button = getch()
        if button == 'w':
            y = y-1
            if board[y][x] != ' ' and board[y][x] != 'O':
                y = y+1
            move(x, y)

        elif button == 's':
            y = y+1
            if board[y][x] != ' ' and board[y][x] != 'O':
                y = y-1
            move(x, y)

        elif button == 'a':
            x = x-1
            if board[y][x] != ' ' and board[y][x] != 'O':
                x = x+1
            move(x, y)

        elif button == 'd':
            x = x+1
            if board[y][x] != ' ' and board[y][x] != 'O':
                x = x-1
            move(x, y)

        if board[y][x] == 'O':
            back(button, x, y)

        elif button == "x":
            quit()


def back(button, x, y):
    if button == 'w':
        y = y+1
    elif button == 's':
        y = y-1
    elif button == 'a':
        x = x+1
    elif button == 'd':
        x = x-1
    move(x, y)


def move(x, y):
    board = create_board(60, 20)
    board_with_player = insert_player(board, x, y)
    os.system("clear")
    print_board(board_with_player)
    sleep(0.1)


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


main()
