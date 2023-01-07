from random import randint
import prompt


def welcome_user():  # Приветствие
    name = prompt.string('May I have your name? ')
    print('Hello,', name + '!')
    return name


def even(num):  # Проверка четности
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'


def num_random():  # Рандомное число
    return randint(1, 1000)


def main():  # Основная функция игры
    count = 0
    correct_count = 0
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

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
    if correct_count == 3:
        print('Congratulations, ', name + '!')


if __name__ == '__main__':
    main()