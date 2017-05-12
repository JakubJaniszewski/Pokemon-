import csv
import time


def get_expierience():
    with open("stats.csv", "r") as f:
        f = f.read()
        imported_items = f.split(",")
        imported_items[-1] = imported_items[-1].replace("\n", "")

        experience = 0
        for item in imported_items:
            if item == "Exp":
                experience += 1
    return experience


def save_highscore(experience):
    name = input()
    current_time = time.ctime()
    to_save = [name, experience, current_time]
    with open("highscore.csv", "a") as f:
        wr = csv.writer(f)
        wr.writerow(to_save)


def get_info():
    list_of_scores = []
    with open("highscore.csv", "r") as f:
        f = f.readlines()
        for element in f:
            element = element.replace("\n", "")
            list_of_scores.append(element)

    list_of_scores = [x.split(',') for x in list_of_scores]
    return list_of_scores


def print_top_10(list_of_scores):
    list_of_scores = sorted(list_of_scores, key=lambda x: int(x[1]), reverse=True)

    print("\nName | Exp | Date:")
    count = 1

    if len(list_of_scores) >= 10:
        for index in range(0, 10):
            for element in list_of_scores[index]:
                print(("#" + str(count)), end=" ")
                print(element, end=" | ")
            count += 1
            print("")
    else:
        for index in range(len(list_of_scores)):
            for element in list_of_scores[index]:
                print(("#" + str(count)), end=" ")
                print(element, end=" | ")
            count += 1
            print("")


def main():
    experience = get_expierience()
    save_highscore(experience)
    list_of_scores = get_info()
    print_top_10(list_of_scores)
