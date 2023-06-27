import random
import math


RULES = 'Answer "yes" if given number is prime. \
Otherwise answer "no".'


def is_prime(number):
    if number < 2:
        return False
    for divisor in range(2, int(math.sqrt(number)) + 1):
        if number % divisor == 0:
            return False
            break
    else:
        return True


def question_and_answer():
    question = random.randint(1, 100)
    if is_prime(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
