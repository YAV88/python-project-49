from random import randint


SPECIFICATION = 'Find the greatest common divisor of given numbers.'
MIN_NUMBER = 1
MAX_NUMBER = 20


def gcd(num_one, num_two):
    if num_two == 0:
        return num_one
    else:
        return gcd(num_two, num_one % num_two)


def num_random():
    num_one = randint(MIN_NUMBER, MAX_NUMBER)
    num_two = randint(MIN_NUMBER, MAX_NUMBER)
    question = f'{num_one} {num_two}'
    correct_answer = gcd(num_one, num_two)
    return question, str(correct_answer)
