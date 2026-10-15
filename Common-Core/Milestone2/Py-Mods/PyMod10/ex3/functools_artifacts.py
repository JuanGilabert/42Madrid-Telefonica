from typing import Callable, Any
from operator import add as oper_add, mul as oper_mul
from functools import (
    reduce as funct_reduce,
    partial as funct_partial,
    lru_cache as funct_lru_cache,
    singledispatch as funct_singledispatch,
)


generated_fibonacci_tests = [13, 12, 15]
generated_spell_powers = [40, 20, 33, 37, 32, 24]
generated_allowed_spell_operations = ["add", "multiply", "max", "min"]


def spell_reducer(spells: list[int], operation: str) -> int:
    """
    Reduce a list of spell powers using the requested operation.

    Supported operations:
    - add
    - multiply
    - max
    - min

    Empty lists return 0.
    """
    if not spells:
        return 0
    if operation not in generated_allowed_spell_operations:
        raise ValueError(f"Unknown operation: {operation}")
    if operation == 'add':
        return funct_reduce(oper_add, spells)
    if operation == 'multiply':
        return funct_reduce(oper_mul, spells)
    if operation == 'max':
        return funct_reduce(max, spells)
    if operation == 'min':
        return funct_reduce(min, spells)
    return 0


def test_spell_reducer() -> None:
    print("Testing spell reducer...")
    print(f"Sum: {spell_reducer(generated_spell_powers, 'add')}")
    print(f"Product: {spell_reducer(generated_spell_powers, 'multiply')}")
    print(f"Max: {spell_reducer(generated_spell_powers, 'max')}")
    print()


def base_enchantment_funct(power: int, element: str, target: str) -> str:
    return f"Power: {power}, Element: {element}, Target: {target}"


def partial_enchanter(
    base_enchantment: Callable[[int, str, str], str],
) -> dict[str, Callable[[str], str]]:
    """
    Create specialized enchantment functions using functools.partial.

    Each enchantment:
    - uses power=50
    - has its own element
    - receives target when called
    """
    return {
        "fire": funct_partial(base_enchantment, 50, "fire"),
        "ice": funct_partial(base_enchantment, 50, "ice"),
        "shadow": funct_partial(base_enchantment, 50, "shadow")
    }


def test_partial_enchanter() -> None:
    print("Testing partial enchanter...")
    enchantments = partial_enchanter(base_enchantment_funct)
    print(enchantments["fire"]("dragon"))
    print(enchantments["ice"]("goblin"))
    print(enchantments["shadow"]("wizard"))
    print()


@funct_lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """
    Return the nth Fibonacci number using memoization.
    F(n) = F(n-1) + F(n-2)
    """
    if n < 0:
        raise ValueError("Fibonacci number cannot be negative")
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def test_memoized_fibonacci() -> None:
    print("Testing memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    print(f"Cache: {memoized_fibonacci.cache_info()}")
    print()


def spell_dispatcher() -> Callable[[Any], str]:
    """Create and return a single-dispatch spell system."""
    @funct_singledispatch
    def dispatch_spell(spell: Any) -> str:
        return "Unknown spell type"

    @dispatch_spell.register(int)
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @dispatch_spell.register(str)
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @dispatch_spell.register(list)
    def _(spell: list[Any]) -> str:
        return f"Multi-cast: {len(spell)} spells"
    return dispatch_spell


def test_spell_dispatcher() -> None:
    print("Testing spell dispatcher...")
    dispatch_spell = spell_dispatcher()
    print(dispatch_spell(42))
    print(dispatch_spell("fireball"))
    print(dispatch_spell(["fireball", "ice", "shadow"]))
    print(dispatch_spell(3.14))
    print()


def main() -> None:
    test_spell_reducer()
    test_partial_enchanter()
    test_memoized_fibonacci()
    test_spell_dispatcher()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
    except BaseException as base_err:
        print(f"\n{base_err.__class__.__name__}: {base_err}")



"""
Cosas que aañadir al readme que contendra el subject a parte de la hoja de evaluacion

                 functools_artifacts.py
                           │
                           ▼
                         main()
                           │
          ┌────────────────┼─────────────────┐
          ▼                ▼                 ▼
   spell_reducer    partial_enchanter   memoized_fibonacci
          │                │                 │
          ▼                ▼                 ▼
       reduce           partial          lru_cache
          │                │                 │
          ▼                ▼                 ▼
    combina valores   especializa       guarda resultados
                      funciones           anteriores
                           │
                           │
                           ▼
                    spell_dispatcher
                           │
                           ▼
                     singledispatch
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
             int          str          list
              │            │            │
              ▼            ▼            ▼
           damage      enchantment   multi-cast
"""