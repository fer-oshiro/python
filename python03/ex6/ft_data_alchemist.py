#!/usr/bin/env python3

import random


def main() -> None:
    players_name = [
        'Alice', 'bob', 'Charlie',
        'dylan', 'Emma', 'Gregory',
        'john', 'kevin', 'Liam'
        ]
    players_capitalized = [name.capitalize() for name in players_name]
    players_is_capitalized = [
        name for name in players_name
        if name.capitalize() == name
        ]
    players = {name: random.randint(0, 1000) for name in players_capitalized}
    score_avg = round(
        sum(players[player] for player in players) / len(players_name), 2
        )
    players_highscore = {
        name: score for name, score in players.items()
        if score > score_avg
        }

    print("=== Game Data Alchemist ===")
    print(f"Initial list of players: {players_name}")
    print(f"New list with all names capitalized: {players_capitalized}")
    print(f"New list of capitalized names only: {players_is_capitalized}")
    print(f"Score dict: {players}")
    print(f"Score average is {score_avg}")
    print(f"High scores: {players_highscore}")


if __name__ == "__main__":
    main()
