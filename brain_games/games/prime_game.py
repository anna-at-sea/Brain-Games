import random
from brain_games.prime_module import is_prime


game_rules = 'Answer "yes" if given number is prime. \
Otherwise answer "no".'


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


list_of_questions_and_answers = generate_questions_and_answers()
