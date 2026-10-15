from typing import Callable
from functools import wraps
from time import perf_counter


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__} ...")
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        print(f"Spell completed in {end - start:.3f} seconds")
        return result
    return wrapper


@spell_timer
def fireball(power: int):
    return f"Fireball with {power} power"


@spell_timer
def heal(target: str, amount: int = 10):
    return f"Healing {target} for {amount}"


def test_spell_timer() -> None:
    print("Testing spell timer ...")
    fireball_result = fireball(50)
    print(f"Result: {fireball_result}")
    heal_result = heal("Gandalf", amount=20)
    print(f"Result: {heal_result}")
    print()


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(power: int, *args, **kwargs):
            if power >= min_power:
                return func(power, *args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


@power_validator(10)
def fireball_enchantment_validator(power: int):
    return f"Fireball cast with {power} power"


def test_power_validator() -> None:
    print("Testing power validator ...")
    print(fireball_enchantment_validator(15))
    print(fireball_enchantment_validator(5))
    print()


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            f"Spell failed, retrying... "
                            f"(attempt {attempt}/{max_attempts})"
                        )
            return (
                f"Spell casting failed after "
                f"{max_attempts} attempts"
            )
        return wrapper
    return decorator


@retry_spell(3)
def unreliable_spell() -> str:
    raise RuntimeError("Spell failed")


def test_retry_spell() -> None:
    print("Testing retrying spell ...")
    print(unreliable_spell())
    print()


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(
            character.isalpha() or character == " "
            for character in name
        )

    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def test_mage_guild() -> None:
    print("Testing MageGuild ...")
    print(MageGuild.validate_mage_name("Gandalf"))
    print(MageGuild.validate_mage_name("G4ndalf"))
    guild = MageGuild()
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Fireball", 5))
    print()


def main() -> None:
    test_spell_timer()
    test_power_validator()
    test_retry_spell()
    test_mage_guild()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting ...")
    except BaseException as base_err:
        print(f"\n{base_err.__class__.__name__}: {base_err}")
