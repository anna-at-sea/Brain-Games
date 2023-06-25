import random


RULES = 'What number is missing in the progression?'


def question_and_answer():
    progression = []
    number = random.randint(1, 20)
    step = random.randint(1, 10)
    i = 1
    while i <= 10:
        progression.append(number)
        number += step
        i += 1
    random_index = random.randint(0, 9)
    correct_answer = str(progression[random_index])
    progression[random_index] = '..'
    question = ' '.join(list(map(str, progression)))
    return question, correct_answer
