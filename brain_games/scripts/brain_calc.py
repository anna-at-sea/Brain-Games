#!/usr/bin/env python3


from brain_games.games.calc_game import calc_game_rules
from brain_games.games.calc_game import calc_list_of_questions_and_answers
from brain_games.games_logic import any_game


def main():
    any_game(calc_game_rules, calc_list_of_questions_and_answers)


if __name__ == '__main__':
    main()
