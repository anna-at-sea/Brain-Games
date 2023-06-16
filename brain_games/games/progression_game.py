import random


game_rules = 'What number is missing in the progression?'


def generate_progression():
    progression = []
    number = random.randint(1, 20)
    step = random.randint(1, 10)
    i = 1
    while i <= 10:
        progression.append(number)
        number += step
        i += 1
    pop_element = random.randint(0, 9)
    correct_answer = progression[pop_element]
    progression.pop(pop_element)
    progression.insert(pop_element, '..')
    question = ''
    for elem in progression:
        question += f'{elem} '
    question = question.strip()
    return question, str(correct_answer)


def generate_questions_and_answers():
    list_of_questions = []
    list_of_answers = []
    i = 1
    while i <= 3:
        question, correct_answer = generate_progression()
        list_of_questions.append(question)
        list_of_answers.append(correct_answer)
        i += 1
    return zip(list_of_questions, list_of_answers)


list_of_questions_and_answers = generate_questions_and_answers()
