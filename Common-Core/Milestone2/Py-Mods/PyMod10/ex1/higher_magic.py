from typing import Callable


def spell_combiner_fireball(target: str) -> str:
    return f"Fireball hits {target}"


def spell_combiner_heal(target: str) -> str:
    return f"Heals {target}"


def spell_combiner(
    spell1: Callable[[str], str],
    spell2: Callable[[str], str],
) -> Callable[[str], tuple[str, str]]:
    return lambda target: (spell1(target), spell2(target))


def test_spell_combiner() -> None:
    print("Testing spell combiner ...")
    combined = spell_combiner(
        spell_combiner_fireball, spell_combiner_heal
    )
    fireball, heal = combined("Dragon")
    print(f"Combined spell result: {fireball}, {heal}")
    print()


def power_amplifier_base_spell(power: int) -> int:
    return power


def power_amplifier(
    base_spell: Callable[[int], int],
    multiplier: int
) -> Callable[[int], int]:
    return lambda power: base_spell(power) * multiplier


def test_power_amplifier() -> None:
    print("Testing power amplifier...")
    mega_fireball = power_amplifier(power_amplifier_base_spell, 3)
    original = f"Original: {power_amplifier_base_spell(10)}"
    print(f"{original}, Amplified: {mega_fireball(10)}")
    print()


def conditional_caster_spell(power: int) -> str:
    return f"A spell with a power of {power} has been cast."


def conditional_caster_condition(power: int) -> bool:
    return power > 10


def conditional_caster(
    condition: Callable[[int], bool],
    spell: Callable[[int], str]
) -> Callable[[int], str]:
    return lambda power: spell(power) if condition(power) else "Spell fizzled"


def test_conditional_caster() -> None:
    print("Testing conditional caster ...")
    cond_cast = conditional_caster(
        conditional_caster_condition, conditional_caster_spell
    )
    print(cond_cast(10))
    print(cond_cast(11))
    print()


def spell_sequence(
    spells: list[Callable[[str], str]]
) -> Callable[[str], list[str]]:
    return lambda target: [spell(target) for spell in spells]


def test_spell_sequence() -> None:
    print("Testing spell sequence ...")
    spell_seq = spell_sequence(
        [spell_combiner_fireball, spell_combiner_heal]
    )
    print(", ".join(spell_seq("Dragon")))
    print()


def main() -> None:
    test_spell_combiner()
    test_power_amplifier()
    test_conditional_caster()
    test_spell_sequence()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting ...")
    except BaseException as base_err:
        print(f"\n{base_err.__class__.__name__}: {base_err}")
