import prompt


def start_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.RULES)
    for n in range(1, 4):
        question, correct_answer = game.question_and_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. \
Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
        print('Correct!')
    else:
        print(f'Congratulations, {name}!')
