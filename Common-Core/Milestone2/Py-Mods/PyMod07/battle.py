from ex0 import CreatureFactory, FlameFactory, AquaFactory


def test_factory(creature_factory: CreatureFactory) -> None:
    base_creature = creature_factory.create_base()
    print(base_creature.describe())
    print(base_creature.attack())
    evolved_creature = creature_factory.create_evolved()
    print(evolved_creature.describe())
    print(evolved_creature.attack())


def battle(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    creature1 = factory1.create_base()
    creature2 = factory2.create_base()
    print(f"{creature1.describe()} vs. {creature2.describe()} fight!")
    print(creature1.attack())
    print(creature2.attack())


def main() -> None:
    print("Testing factory")
    flame_factory = FlameFactory()
    test_factory(flame_factory)
    print("\nTesting factory")
    aqua_factory = AquaFactory()
    test_factory(aqua_factory)
    print("\nTesting battle")
    battle(flame_factory, aqua_factory)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
    except BaseException as base_err:
        print(f"\nAn unexpected error occurred: {base_err}")
