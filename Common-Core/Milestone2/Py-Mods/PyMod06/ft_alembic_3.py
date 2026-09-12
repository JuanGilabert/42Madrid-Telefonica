from alchemy.elements import create_air


def ft_alembic_3() -> None:
    print("=== Alembic 3 ===")
    structure: str = "'from ... import ...' structure"
    print(f"Accessing alchemy/elements.py using {structure}")
    print(f"Testing create_air: {create_air()}\n")


if __name__ == "__main__":
    try:
        ft_alembic_3()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
    except BaseException as base_err:
        print(f"\nAn unexpected error occurred: {base_err}")
