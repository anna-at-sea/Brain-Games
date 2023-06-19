import random


game_rules = 'Find the greatest common divisor of given numbers.'


# excluding prime numbers greater than 10 to make the game more fun :)
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


def non_prime_number():
    number = random.randint(1, 100)
    while number:
        if number < 10 or not is_prime(number):
            break
        number = random.randint(1, 100)
    return number


def question_and_answer():
    number_1 = non_prime_number()
    number_2 = non_prime_number()
    question = f'{number_1} {number_2}'
    divisor = number_1
    while divisor > 0:
        if number_1 % divisor == 0 and number_2 % divisor == 0:
            correct_answer = str(divisor)
            break
        divisor -= 1
    return question, correct_answer
