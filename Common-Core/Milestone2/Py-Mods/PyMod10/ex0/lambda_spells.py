from typing import cast


artifacts_generated: list[dict[str, object]] = [
    {'name': 'Ice Wand', 'power': 81, 'type': 'weapon'},
    {'name': 'Shadow Blade', 'power': 91, 'type': 'relic'},
    {'name': 'Light Prism', 'power': 60, 'type': 'armor'},
    {'name': 'Crystal Orb', 'power': 90, 'type': 'weapon'}
]
mages_generated: list[dict[str, object]] = [
    {'name': 'Jordan', 'power': 89, 'element': 'earth'},
    {'name': 'Morgan', 'power': 93, 'element': 'earth'},
    {'name': 'Morgan', 'power': 97, 'element': 'ice'},
    {'name': 'Casey', 'power': 51, 'element': 'wind'},
    {'name': 'Alex', 'power': 50, 'element': 'shadow'}
]
spells_generated: list[str] = ['tornado', 'lightning', 'fireball', 'heal']


def artifact_sorter(
    artifacts: list[dict[str, object]]
) -> list[dict[str, object]]:
    return sorted(
        artifacts,
        key=lambda artifact: cast(int, artifact["power"]),
        reverse=True
    )


def test_artifact_sorter() -> None:
    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts_generated)
    artifacts_len = len(sorted_artifacts)
    for artifact in sorted_artifacts:
        msg: str = f"{artifact['name']} ({artifact['power']} power)"
        if artifact['name'] != sorted_artifacts[artifacts_len - 1]['name']:
            print(msg, end=" comes before ")
        else:
            print(msg)
    print()


def power_filter(
    mages: list[dict[str, object]], min_power: int
) -> list[dict[str, object]]:
    return list(
        filter(
            lambda mage: cast(int, mage["power"]) >= min_power,
            mages
        )
    )


def test_power_filter() -> None:
    print("Testing power filter...")
    min_power = cast(
        int,
        min(
            mages_generated,
            key=lambda mage: cast(int, mage["power"])
        )["power"]
    )
    for mage in power_filter(mages_generated, min_power):
        print(f"{mage['name']} ({mage['power']} power)")
    print()


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"* {spell} *", spells))


def test_spell_transformer() -> None:
    print("Testing spell transformer...")
    for spell in spell_transformer(spells_generated):
        print(spell, end=" ")
    print("\n")


def mage_stats(mages: list[dict[str, object]]) -> dict[str, object]:
    return {
        "max_power": max(
            mages,
            key=lambda mage: cast(int, mage["power"])
        )["power"],
        "min_power": min(
            mages,
            key=lambda mage: cast(int, mage["power"])
        )["power"],
        "avg_power": round(
            sum(map(lambda mage: cast(
                int, mage["power"]
            ), mages)) / len(mages),
            2
        )
    }


def test_mage_stats() -> None:
    print("Testing mage stats...")
    stats = mage_stats(mages_generated)
    print(f"Max power: {stats['max_power']}")
    print(f"Min power: {stats['min_power']}")
    print(f"Average power: {stats['avg_power']}")
    print()


def main() -> None:
    test_artifact_sorter()
    test_power_filter()
    test_spell_transformer()
    test_mage_stats()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting ...")
    except BaseException as base_err:
        print(f"\n{base_err.__class__.__name__}: {base_err}")
