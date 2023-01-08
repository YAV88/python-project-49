from random import randint

SPECIFICATION = 'Answer "yes" if the number is even, otherwise answer "no".'


def even(num):  # Проверка четности
    return num % 2 == 0


def num_random():  # Рандомное число
    num = randint(1, 100)
    correct_answer = 'yes' if even(num) else 'no'
    return num, correct_answer
