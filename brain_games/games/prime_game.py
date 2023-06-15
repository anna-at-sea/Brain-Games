import random


prime_game_rules = 'Answer "yes" if given number is prime. \
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
    if number_of_divisors == 2:
        return 'yes'
    return 'no'


def generate_questions_and_answers():
    list_of_questions = []
    list_of_answers = []
    i = 1
    while i <= 3:
        question = random.randint(1, 100)
        correct_answer = is_prime(question)
        list_of_questions.append(question)
        list_of_answers.append(correct_answer)
        i += 1
    return zip(list_of_questions, list_of_answers)


prime_list_of_questions_and_answers = generate_questions_and_answers()
