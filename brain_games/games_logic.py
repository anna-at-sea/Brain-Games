import prompt
from brain_games.cli import welcome_user


def any_game(game):
    name = welcome_user()
    print(game.RULES)
    for n in range(1, 4):
        question, correct_answer = game.question_and_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. \
Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            exit()
            break
        else:
            print('Correct!')
    print(f'Congratulations, {name}!')
