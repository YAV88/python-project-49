import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello,', name + '!')
    return name


def game_start(game):

    name = welcome_user()
    count = 0
    correct_count = 0
    print(game.SPECIFICATION)

    while count < 3:
        count += 1
        question, correct_answer = game.num_random()
        answer = prompt.string(f'Question: {question} ')
        print(f'Your answer: {answer}')

        if answer == correct_answer:
            correct_count += 1
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'. "
                  f"Let's try again, {name}!")
    if correct_count == 3:
        print('Congratulations, ', name + '!')
    else:
        print('You have made a mistake.')
