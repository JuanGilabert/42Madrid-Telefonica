import alchemy.transmutation.recipes as alch_trasmut_recip


def ft_transmutation_0() -> None:
    print("=== Transmutation 0 ===")
    print("Using file alchemy/transmutation/recipes.py directly")
    print(f"Testing lead to gold: {alch_trasmut_recip.lead_to_gold()}\n")


if __name__ == "__main__":
    try:
        ft_transmutation_0()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
    except BaseException as base_err:
        print(f"\nAn unexpected error occurred: {base_err}")
