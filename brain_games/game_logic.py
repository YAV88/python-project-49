import prompt


ROUNDS = 3


def start_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    count_rounds = 0
    print(game.DESCRIPTION)

    while count_rounds < ROUNDS:
        count_rounds += 1
        question, correct_answer = game.game_number_generation()
        answer = prompt.string(f'Question: {question} ')
        print(f'Your answer: {answer}')

        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'. "
                  f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
