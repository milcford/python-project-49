import prompt


def run_game(game):
    count = 0
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print(game.DESCRIPTION)

    while count < 3:
        question, correct_answer = game.generate_game()

        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')

        if answer == str(correct_answer):
            print('Correct!')
            count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break

    if count == 3:
        print(f'Congratulations, {name}!')
