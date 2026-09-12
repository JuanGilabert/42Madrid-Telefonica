

def ft_kaboom_1() -> None:
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    elements: str = "Bats, frogs, arsenic and eyeball"
    try:
        from alchemy.grimoire.dark_spellbook import dark_spell_record
        spell_record = dark_spell_record('Death', elements)
        print(f"Testing record dark spell: {spell_record}")
    except Exception as err:
        print(f"ImportError: {err}")


if __name__ == "__main__":
    try:
        ft_kaboom_1()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
    except BaseException as base_err:
        print(f"\nAn unexpected error occurred: {base_err}")
