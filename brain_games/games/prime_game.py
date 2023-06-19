import random


game_rules = 'Answer "yes" if given number is prime. \
Otherwise answer "no".'


def is_prime(number):
    divisor = number
    number_of_divisors = 0
    i = 1
    while divisor > 0:
        if number % divisor == 0:
            number_of_divisors += 1
        divisor -= 1
        i += 1
    return number_of_divisors == 2


def question_and_answer():
    question = random.randint(1, 100)
    if is_prime(question) is True:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
