from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1.capability import HealCapability, TransformCapability


def test_healing(factory: HealingCreatureFactory) -> None:
    base_creature = factory.create_base()
    print("base:")
    print(f"{base_creature.describe()}")
    print(base_creature.attack())
    if isinstance(base_creature, HealCapability):
        print(base_creature.heal())
    evolved_creature = factory.create_evolved()
    print("evolved:")
    print(f"{evolved_creature.describe()}")
    print(evolved_creature.attack())
    if isinstance(evolved_creature, HealCapability):
        print(evolved_creature.heal())


def test_transform(factory: TransformCreatureFactory) -> None:
    base_creature = factory.create_base()
    print("base:")
    print(f"{base_creature.describe()}")
    print(base_creature.attack())
    if isinstance(base_creature, TransformCapability):
        print(base_creature.transform())
        print(base_creature.attack())
        print(base_creature.revert())
    evolved_creature = factory.create_evolved()
    print("evolved:")
    print(f"{evolved_creature.describe()}")
    print(evolved_creature.attack())
    if isinstance(evolved_creature, TransformCapability):
        print(evolved_creature.transform())
        print(evolved_creature.attack())
        print(evolved_creature.revert())


def main() -> None:
    healing_factory = HealingCreatureFactory()
    print("Testing Creature with healing capability")
    test_healing(healing_factory)
    transform_factory = TransformCreatureFactory()
    print("\nTesting Creature with transform capability")
    test_transform(transform_factory)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting ...")
    except BaseException as base_err:
        print(f"\nAn unexpected error occurred: {base_err}")
