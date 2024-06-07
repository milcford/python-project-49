import random


def generate_game(question, correct_answer):
    print('Answer "yes" if the number is even, otherwise answer "no".') # Эта хуйня должаны быть КОНСТАНТОЙ
    num = random.randint(1, 100) # генерируем рандомное число
    # print(f'Question: {num}') эта строка печатается в движке
    # answer = prompt.string('Your answer: ') ответ от пользователя обрабатывается в движке
    question = num
    if num % 2 == 0: # проверяем что бы число было четным
            # print('Correct!') # это строка выводится в движке после проверки условия
            # count += 1  # счетчик тоже работает теперь на движке
        correct_answer = 'yes' # Если число четное
    elif num % 2 != 0 :
        correct_answer = 'no' # Если число не четное
    return question, correct_answer


if __name__ == '__main__': # ХЗ нужна тут эта конструкция или нет
    main()
