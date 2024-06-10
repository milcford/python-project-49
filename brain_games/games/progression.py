import random

DESCRIPTION = 'What number is missing in the progression?'


def generate_game():
    first_num = random.randint(1, 5)
    step_num = random.randint(-10, 10)
    num_list = []
    for i in range(10):
        num_list.append(str(first_num + step_num * i))
    num_list2 = num_list.copy()
    random_number = random.randrange(1, len(num_list2) - 2)
    num_list2[random_number] = '..'
    question = f'{" ".join(num_list2)}'
    correct_answer = num_list[random_number]
    return question, correct_answer
