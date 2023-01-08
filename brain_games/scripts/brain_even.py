#!/usr/bin/env python3


from brain_games.games_logic import games_start
from brain_games.games import game_even


def main():
    games_start(game_even)


if __name__ == '__main__':
    main()