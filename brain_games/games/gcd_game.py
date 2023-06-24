import random


RULES = 'Find the greatest common divisor of given numbers.'


def question_and_answer():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    question = f'{number_1} {number_2}'
    divisor = number_1
    while divisor > 0:
        if number_1 % divisor == 0 and number_2 % divisor == 0:
            correct_answer = str(divisor)
            break
        divisor -= 1
    return question, correct_answer
