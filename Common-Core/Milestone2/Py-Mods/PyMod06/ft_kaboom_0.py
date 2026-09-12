import alchemy.grimoire as alch_grim


def ft_kaboom_0() -> None:
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    print(
        "Testing record light spell: "
        f"{alch_grim.light_spell_record('Fantasy', 'Earth, wind and fire')}\n"
    )


if __name__ == "__main__":
    try:
        ft_kaboom_0()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
    except BaseException as base_err:
        print(f"\nAn unexpected error occurred: {base_err}")
