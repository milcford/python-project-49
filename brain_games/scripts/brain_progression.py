import math
import random
import prompt


def main():
    count = 0
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('What number is missing in the progression?')
    while count < 3:
        num1 = random.randint(1, 5) # Случайное число от 1 до 5 включительно
        num2 = random.randint(50, 100) # Случайное число от 5 до 50 включительно
        num3 = random.randint(-10, 10)
        num_list = [str(i) for i in range(num1, num2, num3)] # Генерируем список, начальное значение
        num_list2 = num_list.copy()
        question = random.randrange(1, len(num_list2) - 2) # Число длинны списка, выбираем из него рандомное
        num_list2[question] = '..' # Меняем по индексу элемент списка на две точки
        print(f'Question: {" ".join(num_list2)}')
        answer = prompt.string('Your answer: ')
        if answer == num_list[question]:
            print('Correct!')
            count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{num_list[question]}'.")
            print(f"Let's try again, {name}!")
            break
    if count == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()