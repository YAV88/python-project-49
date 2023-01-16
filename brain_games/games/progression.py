from random import randint


DESCRIPTION = 'What number is missing in the progression?'
MIN_NUMBER = 1  # Min step
MAX_NUMBER = 5  # Max step
START_NUMBER = randint(1, 20)  # Initial number
STOP_NUMBER = randint(60, 100)  # End number
LENGTH = 10  # Amount of numbers


def progression_generation(num_1, num_2, num_3):
    progression = list(range(num_1, num_2, num_3))[:LENGTH]
    return progression


def game_number_generation():
    step = randint(MIN_NUMBER, MAX_NUMBER)
    progression = progression_generation(START_NUMBER, STOP_NUMBER, step)
    index = randint(0, len(progression) - 1)
    correct_answer = progression[index]
    progression[index] = '..'

    s = ''
    for i in progression:
        s += str(i) + ' '

    return s.strip(), str(correct_answer)
