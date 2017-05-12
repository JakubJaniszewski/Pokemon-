from time import sleep
import change_files
import random
import print_functions
import getch


def fight(enemy_health, max_health, strength, agility, exp, x, y):
    print_functions.display_screen('action.txt')
    stats = change_files.import_stats('stats.csv')
    print_functions.display_health(stats['Health'], stats['Max health'])

    enemy_attack_strength = int(strength * 0.5)
    enemy_attack_random = [enemy_attack_strength - 1, enemy_attack_strength, enemy_attack_strength + 1]
    enemy_dodge_chance = agility * 2

    player_attack_strength = int(stats['Strength'] * 0.5)
    player_attack_random = [player_attack_strength - 1, player_attack_strength, player_attack_strength + 1]
    player_dodge_chance = int(stats['Agility'] * 0.5)

    while enemy_health > 0:
        print_functions.display_screen('action.txt')
        print('\nPlayer: ', end='')
        print_functions.display_health(stats['Health'], stats['Max health'])
        print('Enemy: ', end='')
        print_functions.display_health(enemy_health, max_health)
        print("\nAttack: 1 | Run away: 2\n")

        choice = getch.getch()
        while not (choice == '1' or choice == '2'):
            choice = getch.getch()

        if choice == '2':
            break

        if choice == '1':
            dodge = random.randint(0, 99)
            sleep(0.5)
            if dodge <= enemy_dodge_chance:
                print('\nYou miss!')
                sleep(1)
            else:
                damage_dealt = random.choice(player_attack_random)
                enemy_health -= damage_dealt
                print("You hit your enemy for " + str(damage_dealt) + " hp!")
                sleep(1)

            dodge = random.randint(0, 99)
            if dodge <= player_dodge_chance:
                print('\nYou dodged!')
                sleep(1)
            else:
                damage = random.choice(enemy_attack_random)
                stats['Health'] = stats['Health'] - damage
                print("You have lost " + str(damage) + " hp!")
                sleep(1)

            if stats['Health'] <= 0:
                print_functions.display_screen('screens/Lose.txt')
                sleep(1.5)
                quit()

    if enemy_health <= 0:
        change_files.add_to_stats(stats, 0, 0, 0, 0, exp, 0)
    else:
        change_files.add_to_stats(stats, 0, 0, 0, 0, 0, 0)

    return enemy_health
