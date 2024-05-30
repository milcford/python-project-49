import random
import prompt


def simple_num(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


def main():
    count = 0
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while count < 3:
        num1 = random.randint(1, 99)
        print(f'Question: {num1}')
        answer = prompt.string('Your answer: ')
        if answer == 'yes' and simple_num(num1):  # Второе условие проверяет что бы число было простым
            print('Correct!')
            count += 1
        elif answer == 'no' and simple_num(num1) == False:
            print('Correct!')
            count += 1
        else:
            if answer == 'yes' and simple_num(num1) == False:
                print(f"'{answer}' is wrong answer ;(. Correct answer was '{'no'}'.")
                print(f"Let's try again, {name}!")
            else:
                print(f"'{answer}' is wrong answer ;(. Correct answer was '{'yes'}'.")
                print(f"Let's try again, {name}!")
            return None
    if count == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
