try:
    from time import sleep
    import os
    import random
    import hot_and_cold
    import beggining_of_the_game
    import change_files
    import print_functions
    import fight
    import getch

except ImportError:
    print("Ooops! Can't connect to the internet!")
    quit()


def create_board(board_name):
    with open(board_name, "r") as maps:
        maps = maps.readlines()
        for i in range(len(maps)):
            maps[i] = list(maps[i])
    return maps


def print_board(board):
    board = beggining_of_the_game.set_color(board)
    for row in board:
        for char in row:
            print(char, end='')


def board_change(board_name, x, y):
    os.system("clear")
    board = create_board(board_name)
    board_with_player = print_functions.insert_player(board, x, y)
    print_board(board_with_player)


def main():
    os.system("clear")
    beggining_of_the_game.welcome_screen()
    beggining_of_the_game.character_creation()
    gameplay()


def gameplay():
    char_alloved = get_allowed_char()
    change_files.reset_files()
    x, y = first_level(char_alloved)
    second_level(char_alloved, x, y)
    third_level(char_alloved)
    fourth_level(char_alloved)
    fifth_level(char_alloved)


def get_allowed_char():
    red = "\033[1;31m"
    green = "\033[0;32m"
    yellow = "\033[0;33m"
    cyan = "\033[1;36m"
    off = "\033[0;0m"

    allowed_char = [' ', 'O', '♺', '⚗', ',', '&', '~', '⍑', '⯂', 'x',
                    yellow + '★' + off,
                    red + '⤩' + off,
                    green + '#' + off,
                    cyan + "(" + off,
                    cyan + ")" + off,
                    yellow + "♕" + off]
    return allowed_char


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
    board_with_player = print_functions.insert_player(board, x, y)
    print_board(board_with_player)
    return board, x, y


def get_action(char_alloved, board, x, y, map_file):
    button = getch.getch()
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
        inv = change_files.import_inventory('test_inventory.csv')
        stats = change_files.import_stats('stats.csv')
        print_functions.display_stats(stats)
        print_functions.print_table(inv, order=None)
        while (getch.getch()).lower() != 'i':
            sleep(0.1)
        board_change(map_file, x, y)

    elif button == "x":
        quit()

    return board, x, y, button


def map1_action(char_alloved, board, x, y):
    print(x, y)
    board, x, y, button = get_action(char_alloved, board, x, y, "maps/map1.txt")
    inv = change_files.import_inventory('test_inventory.csv')
    stats = change_files.import_stats('stats.csv')
    change_files.level_up(stats['Exp'], stats['Level'])

    if board[y][x] == '♺':
        if 'pickaxe' not in inv:
            print('need pickaxe')
            sleep(0.5)

        elif 'pickaxe' in inv or 'sword' in inv:
            iron_ore = ['iron ore']
            change_files.add_to_inventory(inv, iron_ore)
            print('+1 iron ore')
            sleep(0.5)
            board[y][x] = ','

    # smith quest
    if board[y][x] == '⚗':
        x, y = back(button, x, y)

        if 'pickaxe' not in inv and 'sword' not in inv:
            print('I have a quest for you \n i need 5 iron ores')
            sleep(1)
            pickaxe = ['pickaxe']
            print("+1 pickaxe")
            sleep(0.5)
            change_files.add_to_inventory(inv, pickaxe)

        elif 'pickaxe'in inv and 'iron ore' not in inv:
            print('go hurry!')
            sleep(0.5)

        elif 'pickaxe'in inv and inv['iron ore'] < 5:
            print('you need 5!')
            sleep(0.5)

        elif 'pickaxe' in inv and inv['iron ore'] == 5:
            print('good job')
            del inv['iron ore']
            del inv['pickaxe']
            sword = ['sword']
            change_files.add_to_inventory(inv, sword)
            change_files.add_to_stats(stats, 0, 0, 2, 0, 40, 0)

        elif 'sword' in inv:
            print('good luck')
            sleep(0.5)

    if board[y][x] == ',':
        print('no more ore here')
        sleep(0.5)

    if board[y][x] == '(' or board[y][x] == ')':
        stats['Health'] = stats['Max health']
        change_files.add_to_stats(stats, 0, 0, 0, 0, 0, 0)
        print('Full heal')
        sleep(0.2)

    if board[y][x] == '&':
        x, y = back(button, x, y)
        print('w ktróleswie znajdują się lecznicze źródła \n jedno z nich jest za mną, sprawdz sam')
        sleep(1)

    if 'sword' in inv:
        return 2, x, y
    else:
        return 1, x, y


def map2_action(char_alloved, board, x, y):
    print(x, y)
    board, x, y, button = get_action(char_alloved, board, x, y, "maps/map2.txt")
    inv = change_files.import_inventory('test_inventory.csv')
    stats = change_files.import_stats('stats.csv')
    change_files.level_up(stats['Exp'], stats['Level'])

    if board[y][x] == char_alloved[11]:
        print('stój kurwa')
        sleep(0.5)
        enemy_health = fight.fight(25, 25, 5, 5, 25, x, y)
        if enemy_health <= 0:
            board[y][x] = 'x'
            board_change('maps/map2.txt', x, y)
            print('enemy is beaten \n plus 75XP')
            sleep(0.5)
        x, y = back(button, x, y)
        board_change('maps/map2.txt', x, y)

    if board[y][x] == char_alloved[11]:
        x, y = back(button, x, y)
        board_change('maps/map2.txt', x, y)
        print('przepraszam, tylko nie bij')
        sleep(0.5)

    if board[y][x] == '⚗':
        x, y = back(button, x, y)
        board_change('maps/map2.txt', x, y)
        print('good luck')
        sleep(0.5)

    if board[y][x] == char_alloved[13] or board[y][x] == char_alloved[14]:
        stats['Health'] = stats['Max health']
        change_files.add_to_stats(stats, 0, 0, 0, 0, 0, 0)
        print('Full heal')
        sleep(0.2)

    if board[y][x] == '&':
        x, y = back(button, x, y)
        board_change('maps/map2.txt', x, y)
        print('muszę się napić czegoś mocnieszego')
        sleep(0.5)

    if board[y][x] == char_alloved[10]:
        return 3, x, y
    else:
        return 2, x, y


def map3_action(char_alloved, board, x, y):
    print(x, y)
    board, x, y, button = get_action(char_alloved, board, x, y, "maps/map3.txt")
    inv = change_files.import_inventory('test_inventory.csv')
    stats = change_files.import_stats('stats.csv')
    change_files.level_up(stats['Exp'], stats['Level'])

    if board[y][x] == '~':
        if 'bucket' in inv:
            material = ['material']
            change_files.add_to_inventory(inv, material)
            print('+1 material')
            sleep(0.5)
            board[y][x] = ','

    if board[y][x] == '⚗':
        x, y = back(button, x, y)
        board_change('maps/map3.txt', x, y)

        if 'bucket' not in inv and 'robe' not in inv:
            print('I have a quest for you \n i need 5 materials')
            sleep(1)
            bucket = ['bucket']
            change_files.add_to_inventory(inv, bucket)

        elif 'bucket'in inv and 'material' not in inv:
            print('pole baweły jest na zachodzie')
            sleep(0.5)

        elif 'bucket'in inv and inv['material'] < 5:
            print('za mało')
            sleep(0.5)

        elif 'bucket' in inv and inv['material'] == 5:
            print('udało ci się')
            sleep(0.5)
            del inv['material']
            del inv['bucket']
            robe = ['robe']
            change_files.add_to_inventory(inv, robe)
            change_files.add_to_stats(stats, 0, 10, 0, 2, 80, 0)

        elif 'robe' in inv:
            print('idz i odzyskaj tron')
            sleep(0.5)

    if board[y][x] == char_alloved[11]:
        print('awaj leszczu')
        sleep(0.5)
        enemy_health = fight.fight(50, 50, 10, 10, 50, x, y)
        if enemy_health <= 0:
            board[y][x] = '&'
            board_change('maps/map3.txt', x, y)
            print('enemy is beaten \n plus 75XP')
            sleep(0.5)
        x, y = back(button, x, y)
        board_change('maps/map3.txt', x, y)

    if board[y][x] == '&':
        x, y = back(button, x, y)
        board_change('maps/map3.txt', x, y)
        print('nieźle walczysz, wystarczy mi')
        sleep(0.5)

    if board[y][x] == '⍑':
        x, y = back(button, x, y)
        board_change('maps/map3.txt', x, y)
        print('FIGHT CLUB')
        sleep(0.5)

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

    if board[y][x] == char_alloved[13] or board[y][x] == char_alloved[14]:
        stats['Health'] = stats['Max health']
        change_files.add_to_stats(stats, 0, 0, 0, 0, 0, 0)
        print('Full heal')
        sleep(0.2)

    if board[y][x] == 'x':
        if "robe" not in inv:
            x, y = back(button, x, y)
            board_change('maps/map3.txt', x, y)
            print('czego tu szukasz wieśniaku? ... wypierdalaj')
            sleep(0.5)
        elif "robe" in inv:
            board[y][x] = " "

    if board[y][x] == char_alloved[10]:
        return 4, x, y
    else:
        return 3, x, y


def map4_action(char_alloved, board, x, y):
    print(x, y)
    board, x, y, button = get_action(char_alloved, board, x, y, "maps/map4.txt")
    inv = change_files.import_inventory('test_inventory.csv')
    stats = change_files.import_stats('stats.csv')
    change_files.level_up(stats['Exp'], stats['Level'])

    if board[y][x] == '⚗':
        x, y = back(button, x, y)
        board_change('maps/map4.txt', x, y)

        if 'coin' not in inv and 'permit' not in inv:
            print('''Jestem gueratorem i mam glejt \n jeżeli oswobodzisz przedmieścia z rąk
            bandytów to oddam ci mój glejt \n jako dowód prznieś mi ich głowy \n
            tu masz trochę monet na zachęte''')
            sleep(1)
            coin = ['coin']*120
            change_files.add_to_inventory(inv, coin)

        elif 'coin'in inv and 'bandit head' not in inv:
            print('tam giną ludzie, spiesz się')
            sleep(0.5)

        elif 'coin'in inv and inv['bandit head'] < 4:
            print('to nie wszscy, tam wciąż są bandyci')
            sleep(0.5)

        elif 'coin' in inv and inv['bandit head'] == 4:
            print('oswobodziłeś lud, ale glejt będzie cię kosztował 120 monet')
            sleep(1)
            del inv['bandit head']
            del inv['coin']
            permit = ['permit']
            change_files.add_to_inventory(inv, permit)
            change_files.add_to_stats(stats, 0, 0, 0, 0, 250, 0)

        elif 'permit' in inv:
            print("Nie mam czasu, żegnaj!")
            sleep(0.5)

    if board[y][x] == char_alloved[11]:
        print('zajebie cie!')
        sleep(0.5)
        enemy_health = fight.fight(75, 75, 13, 13, 75, x, y)
        if enemy_health <= 0:
            board[y][x] = '&'
            board_change('maps/map4.txt', x, y)
            print('enemy is beaten \n plus 75XP')
            sleep(0.5)
            bandit_head = ['bandit head']
            add_to_inventory(inv, bandit_head)
            print('+1 bandit head')
            sleep(0.25)
        x, y = back(button, x, y)
        board_change('maps/map4.txt', x, y)

    if board[y][x] == '&':
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

    if board[y][x] == char_alloved[13] or board[y][x] == char_alloved[14]:
        stats['Health'] = stats['Max health']
        change_files.add_to_stats(stats, 0, 0, 0, 0, 0, 0)
        print('Full heal')
        sleep(0.2)

    if board[y][x] == char_alloved[10]:
        return 5, x, y
    else:
        return 4, x, y


def map5_action(char_alloved, board, x, y):
    print(x, y)
    board, x, y, button = get_action(char_alloved, board, x, y, "maps/map5.txt")

    if board[y][x] == char_alloved[15]:
        hot_and_cold.main()
        return 6, x, y
    else:
        return 5, x, y


def move(x, y, board_name="maps/map1.txt"):
    board = create_board(board_name)
    board_with_player = print_functions.insert_player(board, x, y)
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


if __name__ == "__main__":
    main()
