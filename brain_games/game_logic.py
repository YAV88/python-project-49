import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello,', name + '!')
    return name


def start_game(game):

    name = welcome_user()
    count = 0

    print(game.DESCRIPTION)

    while count < 3:
        count += 1
        question, correct_answer = game.num_random()
        answer = prompt.string(f'Question: {question} ')
        print(f'Your answer: {answer}')

        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'. "
                  f"Let's try again, {name}!")
    if count == 3:
        print('Congratulations, ', name + '!')
