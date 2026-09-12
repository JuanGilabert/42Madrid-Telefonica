import alchemy.transmutation as alch_trasmut


def ft_transmutation_1() -> None:
    print("=== Transmutation 1 ===")
    print("Import transmutation module directly")
    print(f"Testing lead to gold: {alch_trasmut.lead_to_gold()}\n")


if __name__ == "__main__":
    try:
        ft_transmutation_1()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
    except BaseException as base_err:
        print(f"\nAn unexpected error occurred: {base_err}")
