#!/usr/bin/env python3


from brain_games.games.prime_game import prime_game_rules
from brain_games.games.prime_game import prime_list_of_questions_and_answers
from brain_games.games_logic import any_game


def main():
    any_game(prime_game_rules, prime_list_of_questions_and_answers)


if __name__ == '__main__':
    main()
