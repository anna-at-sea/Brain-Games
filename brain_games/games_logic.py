import prompt
from brain_games.cli import welcome_user


def any_game(game_rules, question_and_answer):
    name = welcome_user()
    print(game_rules)
    i = 1
    while i <= 3:
        question, correct_answer = question_and_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. \
Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            exit()
            break
        print('Correct!')
        i += 1
    print(f'Congratulations, {name}!')
