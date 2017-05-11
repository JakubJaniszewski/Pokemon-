from random import randint
import os
import highscore


def gameplay():

    number_to_guess = get_random_number()
    print(number_to_guess)

    lives = 10

    while not lives == 0:
        print("Lives left: " + str(lives))

        guess = get_guess()
        clues = set_clues(number_to_guess, guess)

        if len(clues) == 0:
            clues.append('Cold')

        if clues == ['Hot', 'Hot', 'Hot']:
            display_file("screens/Win.txt")
            highscore.main()
            break
        elif len(clues) >= 1:
            print(", ".join(clues))
            lives -= 1
        else:
            lives -= 1

        if lives == 0:
            display_file("screens/Lose.txt")


def get_guess():
    guess_check = 0

    while not guess_check == 1:
        guess = input('Guess 3 digits: ')
        while not (guess.isdigit() and len(guess) == 3):
            guess = input('Wrong input! Guess 3 digits: ')

        if guess[0] == guess[1] or guess[1] == guess[2] or guess[0] == guess[2]:
            print("You can't enter the same digits few times!")
        else:
            guess_check = 1
    return guess


def get_random_number():
    number_to_guess = ""
    number_to_guess += str(randint(1, 9))

    while not len(number_to_guess) == 3:
        drawn_number = str(randint(0, 9))
        if drawn_number not in number_to_guess:
            number_to_guess += drawn_number

    return(number_to_guess)


def set_clues(number_to_guess, guess):
    clues = []
    index = 0

    for digit in number_to_guess:
        if digit == guess[index]:
            clues.append('Hot')
        elif guess[index] in number_to_guess:
            clues.append('Warm')
        index += 1

    return clues


def display_file(filename):
    os.system("clear")
    with open(filename, "r") as f:
        screen = f.read()
        print(screen)


def main():
    display_file("screens/Boss_fight.txt")
    gameplay()
