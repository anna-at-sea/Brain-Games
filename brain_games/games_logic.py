import prompt
from brain_games.welcome import welcome_user


def any_game(game_rules, list_of_questions_and_answers):
    name = welcome_user()
    print(game_rules)
    for question, correct_answer in list_of_questions_and_answers:
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. \
Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            exit()
        print('Correct!')
    print(f'Congratulations, {name}!')
