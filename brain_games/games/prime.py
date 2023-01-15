from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUMBER = 1      # Min number
MAX_NUMBER = 100    # Max number


def is_prime(num):
    d = 2
    while num % d != 0:
        d += 1
    return d == num


def num_random():
    num = randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = 'yes' if is_prime(num) else 'no'
    return num, correct_answer
