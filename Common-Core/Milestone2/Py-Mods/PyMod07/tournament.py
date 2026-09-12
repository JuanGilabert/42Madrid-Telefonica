from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    BattleStrategy,
    NormalStrategy,
    DefensiveStrategy,
    AggressiveStrategy,
    InvalidStrategyError,
)


def ft_do_tournament(
    first_opponent: tuple[CreatureFactory, BattleStrategy],
    second_opponent: tuple[CreatureFactory, BattleStrategy]
) -> None:
    first_opponent_factory, first_opponent_strategy = first_opponent
    creature1 = first_opponent_factory.create_base()
    second_opponent_factory, second_opponent_strategy = second_opponent
    creature2 = second_opponent_factory.create_base()
    print("* Battle *")
    print(creature1.describe())
    print("vs.")
    print(creature2.describe())
    print("now fight!")
    try:
        first_opponent_strategy.act(creature1)
        second_opponent_strategy.act(creature2)
    except InvalidStrategyError as error:
        print(f"Battle error, aborting tournament: {error}")
    print()


def battle(
    opponents_list: list[tuple[CreatureFactory, BattleStrategy]]
) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents_list)} opponents involved")
    print()
    for i in range(len(opponents_list)):
        for j in range(i + 1, len(opponents_list)):
            ft_do_tournament(opponents_list[i], opponents_list[j])


def ft_tournament_0() -> None:
    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    battle([
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())
    ])


def ft_tournament_1() -> None:
    print("Tournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle([
        (FlameFactory(), AggressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())
    ])


def ft_tournament_2() -> None:
    print("Tournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle([
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy())
    ])


def main() -> None:
    ft_tournament_0()
    ft_tournament_1()
    ft_tournament_2()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
    except BaseException as base_err:
        print(f"\nAn unexpected error occurred: {base_err}")
