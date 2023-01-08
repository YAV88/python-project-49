from brain_games.cli import welcome_user
from brain_games.scripts.brain_even import even


def games_start(game):
    count = 0
    correct_count = 0
    name = welcome_user()

    print(game.SPECIFICATION)

    while count < 3:
        count += 1
        num = num_random()
        answer = prompt.string(f'Question: {num} ')
        print(f'Your answer: {answer}')
        correct_answer = even(num)

        if answer == correct_answer:
            correct_count += 1
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'. "
                  f"Let's try again, {name}!")

    print('Congratulations, ', name + '!')


