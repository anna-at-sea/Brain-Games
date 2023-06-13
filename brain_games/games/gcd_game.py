import random


gcd_game_rules = 'Find the greatest common divisor of given numbers.'


# excluding prime numbers greater than 10 to make the game more fun :)
def non_prime_number():
    number = random.randint(1, 100)
    while number:
        divisors_list = []
        divisor = number
        while divisor > 0:
            if number % divisor == 0:
                divisors_list.append(divisor)
            divisor -= 1
        if number < 10 or divisors_list != [number, 1]:
            break
        number = random.randint(1, 100)
    return number


def generate_questions_and_answers():
    list_of_questions = []
    list_of_answers = []
    i = 1
    while i <= 3:
        number_1 = non_prime_number()
        number_2 = non_prime_number()
        question = f'{number_1} {number_2}'
        list_of_questions.append(question)
        divisor = number_1
        while number_1 > 0:
            if number_1 % divisor == 0 and number_2 % divisor == 0:
                correct_answer = str(divisor)
                break
            divisor -= 1
        list_of_answers.append(correct_answer)
        i += 1
    return zip(list_of_questions, list_of_answers)


gcd_list_of_questions_and_answers = generate_questions_and_answers()
