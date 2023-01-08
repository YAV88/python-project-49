import prompt

# How to find out the name


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello,', name + '!')
    return name
