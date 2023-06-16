import random


game_rules = 'What is the result of the expression?'


def generate_questions_and_answers():
    list_of_questions = []
    list_of_answers = []
    i = 1
    while i <= 3:
        number_1 = random.randint(0, 100)
        number_2 = random.randint(0, 10)
        operator = random.choice(['+', '-', '*'])
        question = f'{number_1} {operator} {number_2}'
        list_of_questions.append(question)
        if operator == '+':
            correct_answer = str(number_1 + number_2)
        elif operator == '-':
            correct_answer = str(number_1 - number_2)
        else:
            correct_answer = str(number_1 * number_2)
        list_of_answers.append(correct_answer)
        i += 1
    return zip(list_of_questions, list_of_answers)


list_of_questions_and_answers = generate_questions_and_answers()
