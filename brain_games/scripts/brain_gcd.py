#!/usr/bin/env python3
from brain_games.game_logic import game_start
from brain_games.games import game_gcd


def main():
    game_start(game_gcd)


if __name__ == '__main__':
    main()
