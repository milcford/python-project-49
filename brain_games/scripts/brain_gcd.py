import random
import prompt
import math


def main():
    count = 0
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Find the greatest common divisor of given numbers.')
    while count < 3:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        print(f'Question: {num1} {num2}')
        answer = prompt.string('Your answer: ')
        gcd = math.gcd(num1, num2)
        if gcd == int(answer):
            print('Correct!')
            count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{gcd}'.")
            print(f"Let's try again, {name}!")
            break
    if count == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
