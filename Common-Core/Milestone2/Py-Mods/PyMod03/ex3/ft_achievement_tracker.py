import random


achievements: list[str] = [
    "First Steps",
    "Crafting Genius",
    "Strategist",
    "World Savior",
    "Speed Runner",
    "Survivor",
    "Master Explorer",
    "Treasure Hunter",
    "Unstoppable",
    "Collector Supreme",
    "Untouchable",
    "Sharp Mind",
    "Boss Slayer",
    "Hidden Path Finder"
]


def gen_player_achievements() -> set[str]:
    rand_int = random.randint(4, len(achievements) - 1)
    return set(random.sample(achievements, rand_int))


def ft_achievement_tracker() -> None:
    print("=== Achievement Tracker System ===")
    dylan = gen_player_achievements()
    charlie = gen_player_achievements()
    bob = gen_player_achievements()
    alice = gen_player_achievements()
    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")
    all_achievements = set.union(alice, bob, charlie, dylan)
    print(f"All distinct achievements: {all_achievements}")
    common = set.intersection(alice, bob, charlie, dylan)
    print(f"Common achievements: {common}")
    print(f"Only Alice has: {set.difference(alice, bob, charlie, dylan)}")
    print(f"Only Bob has: {set.difference(bob, alice, charlie, dylan)}")
    print(f"Only Charlie has: {set.difference(charlie, alice, bob, dylan)}")
    print(f"Only Dylan has: {set.difference(dylan, alice, bob, charlie)}")
    print(f"Alice is missing: {set.difference(all_achievements, alice)}")
    print(f"Bob is missing: {set.difference(all_achievements, bob)}")
    print(f"Charlie is missing: {set.difference(all_achievements, charlie)}")
    print(f"Dylan is missing: {set.difference(all_achievements, dylan)}")


if __name__ == "__main__":
    try:
        ft_achievement_tracker()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
    except BaseException as base_err:
        print(f"\nAn unexpected error occurred: {base_err}")
