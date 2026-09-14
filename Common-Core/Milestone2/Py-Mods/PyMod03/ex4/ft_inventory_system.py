import sys


def ft_check_inventory_item(inventory_item_argv: str) -> tuple[str, int]:
    inventory_item_argv_str: str = ""
    try:
        inventory_item_argv_list = inventory_item_argv.split(":")
        if len(inventory_item_argv_list) < 2:
            return ("", 0)
        inventory_item_argv_str = inventory_item_argv_list[0]
        return (inventory_item_argv_list[0], int(inventory_item_argv_list[1]))
    except ValueError as error:
        print(f"Quantity error for '{inventory_item_argv_str}': {error}")
        return ("", -1)


def ft_check_inventory_system_args() -> dict[str, int]:
    inventory_dict: dict[str, int] = {}
    for sys_argv_item in sys.argv[1:]:
        item_dict_key, item_dict_val = ft_check_inventory_item(sys_argv_item)
        if item_dict_val < 1:
            if item_dict_val == 0:
                print(f"Error - invalid parameter '{sys_argv_item}'")
            continue
        if item_dict_key in inventory_dict:
            print(f"Redundant item '{item_dict_key}'- discarding")
            continue
        inventory_dict.update({item_dict_key: item_dict_val})
    return inventory_dict


def ft_get_most_abundant_item(
        inventory_dict: dict[str, int]
) -> tuple[str, int]:
    if not inventory_dict:
        return ("", 0)
    max_item_key: str = list(inventory_dict.keys())[0]
    max_item_val: int = list(inventory_dict.values())[0]
    for key, val in inventory_dict.items():
        if val > max_item_val:
            max_item_val = val
            max_item_key = key
    return (max_item_key, max_item_val)


def ft_get_least_abundant_item(
        inventory_dict: dict[str, int]
) -> tuple[str, int]:
    if not inventory_dict:
        return ("", 0)
    least_item_key = list(inventory_dict.keys())[0]
    least_item_val = list(inventory_dict.values())[0]
    for key, val in inventory_dict.items():
        if val < least_item_val:
            least_item_val = val
            least_item_key = key
    return (least_item_key, least_item_val)


def ft_show_inventory(inventory_dict: dict[str, int]) -> None:
    inventory_dict_keys_list: list[str] = list(inventory_dict.keys())
    inventory_dict_values_list: list[int] = list(inventory_dict.values())
    print(f"Got inventory: {inventory_dict}")
    print(f"Item list: {inventory_dict_keys_list}")
    items_msg = f"items : {sum(inventory_dict_values_list)}"
    print(f"Total quantity of the {len(inventory_dict_keys_list)} {items_msg}")
    for key, val in inventory_dict.items():
        item_percentage = (val / sum(inventory_dict_values_list)) * 100
        print(f"Item {key} represents {item_percentage:.1f}%")
    most_item_key, most_item_val = ft_get_most_abundant_item(
        inventory_dict
    )
    quantity_msg = f"with quantity {most_item_val}"
    print(f"Item most abundant: {most_item_key} {quantity_msg}")
    least_item_key, least_item_val = ft_get_least_abundant_item(
        inventory_dict
    )
    quantity_msg2 = f"with quantity {least_item_val}"
    print(f"Item least abundant: {least_item_key} {quantity_msg2}")
    print(f"Updated inventory: {inventory_dict}")


def ft_inventory_system() -> None:
    if len(sys.argv) < 2:
        return print("At the beginning of the game, "
                     "your inventory is usually empty ;)")
    print("=== Inventory System Analysis ===")
    inventory_dict: dict[str, int] = ft_check_inventory_system_args()
    ft_show_inventory(inventory_dict)


if __name__ == "__main__":
    try:
        ft_inventory_system()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
    except BaseException as base_err:
        print(f"\nAn unexpected error occurred: {base_err}")
