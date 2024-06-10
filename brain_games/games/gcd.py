import random

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_game():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f'{num1} {num2}'
    while num1 != num2:
        if num1 > num2:
            num1 -= num2
        else:
            num2 -= num1
    correct_answer = num1
    return question, correct_answer
