#!/usr/bin/env python3


from brain_games.games.even_game import even_game_rules
from brain_games.games.even_game import even_list_of_questions_and_answers
from brain_games.games_logic import any_game


def main():
    any_game(even_game_rules, even_list_of_questions_and_answers)


if __name__ == '__main__':
    main()
