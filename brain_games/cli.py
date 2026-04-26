import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name

def brains_games_entry():
    welcome_user()

def brain_calc_entry():
    from brain_games.scripts.engine import main
    from brain_games.scripts.games import brain_calc

    main(brain_calc.rules, brain_calc.generate_round)

def brain_even_entry():
    from brain_games.scripts.engine import main
    from brain_games.scripts.games import brain_even

    main(brain_even.rules, brain_even.generate_round)

def brain_gcd_entry():
    from brain_games.scripts.engine import main
    from brain_games.scripts.games import brain_gcd

    main(brain_gcd.rules, brain_gcd.generate_round)

def brain_progression_entry():
    from brain_games.scripts.engine import main
    from brain_games.scripts.games import brain_progression

    main(brain_progression.rules, brain_progression.generate_round)

def brain_prime_entry():
    from brain_games.scripts.engine import main
    from brain_games.scripts.games import brain_prime

    main(brain_prime.rules, brain_prime.generate_round)