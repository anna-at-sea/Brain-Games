import random


def if_even(number):
    if number % 2 == 0:
        return 'yes'
    return 'no'


even_game_rules = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_questions_and_answers():
    list_of_questions = []
    list_of_answers = []
    i = 1
    while i <= 3:
        list_of_questions.append(f'{random.randint(0, 100)}')
        list_of_answers.append(if_even(int(list_of_questions[-1])))
        i += 1
    return zip(list_of_questions, list_of_answers)


even_list_of_questions_and_answers = generate_questions_and_answers()
