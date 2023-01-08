from brain_games.cli import welcome_user
import prompt


def games_start(game):

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
