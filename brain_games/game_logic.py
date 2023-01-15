import prompt


ROUNDS = 3


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello,', name + '!')
    return name


def start_game(game):

    name = welcome_user()
    count_rounds = 0

    print(game.DESCRIPTION)

    while count_rounds < ROUNDS:
        count_rounds += 1
        question, correct_answer = game.num_random()
        answer = prompt.string(f'Question: {question} ')
        print(f'Your answer: {answer}')

        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'. "
                  f"Let's try again, {name}!")
    if count_rounds == ROUNDS:
        print('Congratulations, ', name + '!')
