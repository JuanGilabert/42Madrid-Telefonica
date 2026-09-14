import random


players = [
    "Alice",
    "bob",
    "Charlie",
    "dylan",
    "Emma",
    "Gregory",
    "john",
    "kevin",
    "Liam"
]


def ft_data_alchemist() -> None:
    print("=== Game Data Alchemist ===\n")
    print(f"Initial list of players: {players}")
    full_capitalized_players: list[str] = [
        player.capitalize() for player in players
    ]
    print(f"New list with all names capitalized: {full_capitalized_players}")
    only_capitalized_players: list[str] = [
        player for player in players
        if player.capitalize() == player
    ]
    print(f"New list of capitalized names only: {only_capitalized_players}\n")
    first_players_scores_dict: dict[str, int] = {
        player: random.randint(0, 1000) for player in players
    }
    print(f"Score dict: {first_players_scores_dict}")
    players_scores_sum: float = sum(first_players_scores_dict.values())
    score_average: float = players_scores_sum / len(first_players_scores_dict)
    print(f"Score average is {score_average:.2f}")
    second_players_scores_dict: dict[str, int] = {
        player: score
        for player, score in first_players_scores_dict.items()
        if score > score_average
    }
    print(f"High scores: {second_players_scores_dict}")


if __name__ == "__main__":
    try:
        ft_data_alchemist()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
    except BaseException as base_err:
        print(f"\nAn unexpected error occurred: {base_err}")
