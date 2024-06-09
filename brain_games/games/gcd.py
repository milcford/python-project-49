import random


def generate_game(question, correct_answer):
    print('Find the greatest common divisor of given numbers.')  # Это должна быть КОНСТАНТА
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f'{num1} {num2}'  # БУДУТ ЛИ ТУТ ИЗМЕНЯТЬСЯ ЗНАЧЕНИЯ ПОСЛЕ ЦИКЛА ХЗ
    while num1 != num2:
        if num1 > num2:
            num1 -= num2
        else:
            num2 -= num1
    correct_answer = num1
    return question, correct_answer


if __name__ == '__main__':
    main()
