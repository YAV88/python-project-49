from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUMBER = 1      # Min number
MAX_NUMBER = 100    # Max number


def is_prime(num):
    divider = 2
    while num % divider != 0:
        divider += 1
    return divider == num


def game_number_generation():
    num = randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = 'yes' if is_prime(num) else 'no'
    return num, str(correct_answer)
