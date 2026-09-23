import alchemy.elements as alch_elem


def ft_alembic_2() -> None:
    print("=== Alembic 2 ===")
    print("Accessing alchemy/elements.py using 'import ...' structure")
    print(f"Testing create_earth: {alch_elem.create_earth()}\n")


if __name__ == "__main__":
    try:
        ft_alembic_2()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
    except BaseException as base_err:
        print(f"\nAn unexpected error occurred: {base_err}")
