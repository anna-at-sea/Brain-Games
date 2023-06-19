#!/usr/bin/env python3


from brain_games.games import even_game
from brain_games.games_logic import any_game


def main():
    any_game(even_game.game_rules, even_game.question_and_answer)


if __name__ == '__main__':
    main()
