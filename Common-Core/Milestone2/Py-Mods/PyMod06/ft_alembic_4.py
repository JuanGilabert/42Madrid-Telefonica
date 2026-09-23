import alchemy


def ft_alembic_4() -> None:
    print("=== Alembic 4 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    print(f"Testing create_air: {alchemy.create_air()}")
    print("Now show that not all functions can be reached")
    print("This will raise an exception!")
    print("Testing the hidden create_earth:")
    try:
        print(f"{alchemy.create_earth()}")
    except Exception as err:
        print(f"{err.__class__.__name__} {err}")


if __name__ == "__main__":
    try:
        ft_alembic_4()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
    except BaseException as base_err:
        print(f"\nAn unexpected error occurred: {base_err}")
