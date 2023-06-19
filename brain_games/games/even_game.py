import random


game_rules = 'Answer "yes" if the number is even, otherwise answer "no".'


def if_even(number):
    return number % 2 == 0


def question_and_answer():
    question = random.randint(0, 100)
    if if_even(question) is True:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
