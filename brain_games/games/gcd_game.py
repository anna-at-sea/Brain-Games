import random


RULES = 'Find the greatest common divisor of given numbers.'


def gcd(num1, num2):
    divisor = num1
    while divisor > 0:
        if num1 % divisor == 0 and num2 % divisor == 0:
            break
        divisor -= 1
    return divisor


def question_and_answer():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f'{num1} {num2}'
    correct_answer = str(gcd(num1, num2))
    return question, correct_answer
