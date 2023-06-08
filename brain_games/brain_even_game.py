import prompt


def brain_even_game_logic():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    questions_and_answers = [('15', 'no'), ('6', 'yes'), ('7', 'no')]
    for question, answer in questions_and_answers:
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer != answer:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{answer}'.")
            print(f"Let's try again, {name}!")
            exit()
        print('Correct!')
    print(f'Congratulations, {name}!')
