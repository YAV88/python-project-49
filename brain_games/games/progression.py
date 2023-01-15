from random import randint

DESCRIPTION = 'What number is missing in the progression?'
MIN_NUMBER = 1  # Min step
MAX_NUMBER = 5  # Max step
START_NUMBER = randint(1, 20)  # Initial number
STOP_NUMBER = randint(60, 100)  # End number
LENGTH = randint(5, 10)  # Amount of numbers


def num_random():
    step = randint(MIN_NUMBER, MAX_NUMBER)
    progression = list(range(START_NUMBER, STOP_NUMBER, step))[:LENGTH]
    index = randint(0, len(progression) - 1)
    correct_answer = progression[index]
    progression[index] = '..'

    s = ''
    for i in progression:
        s += str(i) + ' '

    return s.strip(), str(correct_answer)
