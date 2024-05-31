import random
import prompt


def func(result, name, count):
    answer = prompt.string('Your answer: ')
    if result == int(answer):
        print('Correct!')
        count += 1
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.")
        print(f"Let's try again, {name}!")
        break

def main():
    count = 0
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('What is the result of the expression?')
    while count < 3:
        action = random.choice(['+', '-', '*'])
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)

        if action == '+':
            result = num1 + num2
            print(f'Question: {num1} + {num2}')
            func(result, name, count)
        elif action == '-':
            result = num1 - num2
            print(f'Question: {num1} - {num2}')
            func(result, name, count)
        elif action == '*':
            result = num1 * num2
            print(f'Question: {num1} * {num2}')
            func(result, name, count)

    if count == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
