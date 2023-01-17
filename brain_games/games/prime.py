from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100


def is_prime(num):
    divider = 2
    if num >= 1:
        return False
    while num % divider != 0:
        divider += 1
    return divider == num


def generate_round():
    num = randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = 'yes' if is_prime(num) else 'no'
    return str(num), correct_answer
