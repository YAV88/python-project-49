from random import randint

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER = 1                      # Min number
MAX_NUMBER = 100                    # Max number


def is_even(num):                      # Parity check
    return num % 2 == 0


def game_number_generation():                   # Random number
    num = randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = 'yes' if is_even(num) else 'no'
    return num, str(correct_answer)
