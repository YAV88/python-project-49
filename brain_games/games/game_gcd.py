from random import randint
from math import gcd


SPECIFICATION = 'Find the greatest common divisor of given numbers.'
MIN_NUMBER = 1
MAX_NUMBER = 20


def num_random():
    num_one = randint(MIN_NUMBER, MAX_NUMBER)
    num_two = randint(MIN_NUMBER, MAX_NUMBER)
    question = f'{num_one} {num_two}'
    correct_answer = gcd(num_one, num_two)
    return question, str(correct_answer)
