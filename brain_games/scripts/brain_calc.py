#!/usr/bin/env python3


from brain_games.games import calc_game
from brain_games.games_logic import any_game


def main():
    any_game(calc_game.game_rules, calc_game.question_and_answer)


if __name__ == '__main__':
    main()
