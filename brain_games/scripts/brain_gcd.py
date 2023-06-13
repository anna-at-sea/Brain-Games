#!/usr/bin/env python3


from brain_games.games.gcd_game import gcd_game_rules
from brain_games.games.gcd_game import gcd_list_of_questions_and_answers
from brain_games.games_logic import any_game


def main():
    any_game(gcd_game_rules, gcd_list_of_questions_and_answers)


if __name__ == '__main__':
    main()
