import prompt

from brain_games.cli import welcome_user


def main(rules, generate_round): 
    name = welcome_user()
    print(rules)

    rounds = 3

    for _ in range(rounds):
        question, correct_answer = generate_round()

        print(f'Question: {question}')

        answer = prompt.string('Your answer: ')

        if answer != correct_answer:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")  # noqa: E501
            print(f"Let's try again, {name}!")
            return

        print('Correct!')

    print(f'Congratulations, {name}!')