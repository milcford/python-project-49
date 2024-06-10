import random

DESCRIPTION = 'What is the result of the expression?'


def generate_game():
    action = random.choice(['+', '-', '*'])
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    if action == '+':
        correct_answer = num1 + num2
        question = f'{num1} + {num2}'
    elif action == '-':
        correct_answer = num1 - num2
        question = f'{num1} - {num2}'
    elif action == '*':
        correct_answer = num1 * num2
        question = f'{num1} * {num2}'
    return question, correct_answer
