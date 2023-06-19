import random


game_rules = 'What number is missing in the progression?'


def question_and_answer():
    progression = []
    number = random.randint(1, 20)
    step = random.randint(1, 10)
    i = 1
    while i <= 10:
        progression.append(number)
        number += step
        i += 1
    pop_element = random.randint(0, 9)
    correct_answer = str(progression[pop_element])
    progression.pop(pop_element)
    progression.insert(pop_element, '..')
    question = ''
    for elem in progression:
        question += f'{elem} '
    question = question.strip()
    return question, correct_answer
