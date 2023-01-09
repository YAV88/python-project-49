#!/usr/bin/env python3
from brain_games.games_logic import games_start
from brain_games.games import game_gcd


def main():
    games_start(game_gcd)


if __name__ == '__main__':
    main()