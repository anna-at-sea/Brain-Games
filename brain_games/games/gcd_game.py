import random
from brain_games.prime_module import is_prime


game_rules = 'Find the greatest common divisor of given numbers.'


# excluding prime numbers greater than 10 to make the game more fun :)
def non_prime_number():
    number = random.randint(1, 100)
    while number:
        if number < 10 or is_prime(number) == 'no':
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


def generate_questions_and_answers():
    list_of_questions = []
    list_of_answers = []
    i = 1
    while i <=3:
        question, correct_answer = question_and_answer()
        list_of_questions.append(question)
        list_of_answers.append(correct_answer)
        i += 1
    return zip(list_of_questions, list_of_answers)


list_of_questions_and_answers = generate_questions_and_answers()
