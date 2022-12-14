from random import randint, choice


SPECIFICATION = 'What is the result of the expression?'
MIN_NUMBER = 1
MAX_NUMBER = 10
OPERATORS = ['+', '-', '*']


def num_random():
    num_one = randint(MIN_NUMBER, MAX_NUMBER)
    num_two = randint(MIN_NUMBER, MAX_NUMBER)
    sign = choice(OPERATORS)
    question = f'{num_one} {sign} {num_two}'
    if sign == '+':
        correct_answer = num_one + num_two
    elif sign == '-':
        correct_answer = num_one - num_two
    else:
        correct_answer = num_one * num_two
    return question, str(correct_answer)
