import random

rules = 'What number is missing in the progression?'


def generate_round():
    start = random.randint(1, 15)
    step = random.randint(1, 15)
    length = 10

    progression = [start + i * step for i in range(length)]

    hidden_index = random.randint(0, length - 1)
    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = '..'

    question = ' '.join(str(n) for n in progression)

    return question, correct_answer
