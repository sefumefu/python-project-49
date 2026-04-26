import random


rules = 'What is the result of the expression?'

def generate_round():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    operation = random.choice(['+', '-', '*'])

    question = f"{a} {operation} {b}"
    
    match operation:
        case '+':
            correct_answer = a + b
        case '-':
            correct_answer = a - b
        case '*':
            correct_answer = a * b

    return question, str(correct_answer)