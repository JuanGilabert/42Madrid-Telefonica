import alchemy


def ft_transmutation_2() -> None:
    print("=== Transmutation 2 ===")
    print("Import alchemy module only")
    print(f"Testing lead to gold: {alchemy.lead_to_gold()}\n")


if __name__ == "__main__":
    try:
        ft_transmutation_2()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
    except BaseException as base_err:
        print(f"\nAn unexpected error occurred: {base_err}")
