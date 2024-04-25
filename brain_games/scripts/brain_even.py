import random
import prompt


def main():
    count = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while count < 3:
        num = random.randint(1, 100)
        print(f'Question: {num}')
        answer = prompt.string('May I have your name? ')
        if num % 2 == 0 and answer == 'yes':
            print('Correct!')
            count += 1
        elif num % 2 != 0 and answer == 'no':
            print('Correct!')
            count += 1
        else:
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again, {name}!")
            break
    if count == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
