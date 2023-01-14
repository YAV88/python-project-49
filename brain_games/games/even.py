from random import randint

SPECIFICATION = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER = 1                      # Min number
MAX_NUMBER = 100                    # Max number


def even(num):                      # Parity check
    return num % 2 == 0


def num_random():                   # Random number
    num = randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = 'yes' if even(num) else 'no'
    return num, correct_answer
