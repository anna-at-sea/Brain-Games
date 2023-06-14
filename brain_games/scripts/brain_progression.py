#!/usr/bin/env python3


from brain_games.games.progression_game import progression_game_rules
from brain_games.games.progression_game import \
    progression_list_of_questions_and_answers
from brain_games.games_logic import any_game


def main():
    any_game(progression_game_rules, progression_list_of_questions_and_answers)


if __name__ == '__main__':
    main()
