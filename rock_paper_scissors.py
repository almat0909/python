# Игра «Камень, ножницы, бумага»
# Игра «Угадай число»

import random

def rock_paper_scissors():

    user_choice = 1
    while user_choice != 0:
        random_n = random.randint(1, 3)

        user_choice = int(input('Камень (1), ножницы (2), бумага (3) \n(Введите 0 для выхода с игры): '))
        # Камень бьёт ножницы, ножницы режут бумагу, бумага кроет камень.
        if user_choice == random_n:
            print('Ничья')
            print(random_n)

        elif user_choice not in (0, 1, 2, 3):
            print("Некорректный ввод")

        elif user_choice == 1 and random_n == 2 \
                or user_choice == 2 and random_n == 3 \
                or user_choice == 3 and random_n == 1:
            print('Вы победили')
            print(random_n)
        else:
            print('Вы проиграли')
            print(random_n)

    mainMenu()


def guess_the_number():
    random_n = random.randint(1, 20)

    user_guess = int(input('Угадай число от 1 до 20: '))
    while user_guess != random_n:
        print('Вы не угадали')
        user_guess = int(input('Угадай число: '))

        if user_guess == random_n:
            print('Вы угадали')

    mainMenu()


def mainMenu():
    choose_game = int(input('\nВыберите игру \n(1: "Камень, ножницы, бумага". 2: "Угадай число"): '))
    if choose_game == 1:
        rock_paper_scissors()
    elif choose_game == 2:
        guess_the_number()
    else:
        print("Некорректный ввод")
        mainMenu()


mainMenu()