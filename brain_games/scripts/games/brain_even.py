import random


rules = 'Answer "yes" if the number is even, otherwise answer "no".'

def is_even(n):
    return n % 2 == 0

def generate_round():
    random_number = random.randint(1, 100)
    question = f'{random_number}'

    correct_answer = 'yes' if is_even(random_number) else 'no'

    return question, correct_answer