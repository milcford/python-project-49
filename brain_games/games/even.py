import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_game():
    num = random.randint(1, 100)
    question = num
    if num % 2 == 0:
        correct_answer = 'yes'
    elif num % 2 != 0:
        correct_answer = 'no'
    return question, correct_answer


if __name__ == '__main__':
    main()
