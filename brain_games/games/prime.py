import random


def simple_num(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


def generate_game(correct_answer, question):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')  # Это КОНСТАНТА
    num1 = random.randint(1, 99)
    question = num1

    if simple_num(num1):  # Второе условие проверяет что бы число было простым
        correct_answer = 'yes'
    elif simple_num(num1) == False:
        correct_answer = 'no'
    return question, correct_answer


if __name__ == '__main__':
    main()
