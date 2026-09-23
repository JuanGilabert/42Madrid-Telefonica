#!/usr/bin/env python

def ft_check_supported_units(unit: str) -> bool:
    if unit not in ["grams", "packets", "area"]:
        print("Unknown unit type")
        return False
    return True


def ft_get_unit_type_msg(unit: str, quantity: int = 0) -> str:
    if unit == "grams":
        return f"{quantity} grams total"
    elif unit == "packets":
        return f"{quantity} packets available"
    elif unit == "area":
        return f"covers {quantity} square meters"
    return ""


def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if not seed_type or not quantity:
        return None
    if not unit or not ft_check_supported_units(unit):
        return None
    unit_type_msg: str = ft_get_unit_type_msg(unit, quantity)
    print(f"{seed_type.capitalize()} seeds: {unit_type_msg}")
