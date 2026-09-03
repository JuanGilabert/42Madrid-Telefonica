#!/usr/bin/env python

def ft_count_harvest_recursive_aux(day: int, days_until_harvest: int) -> None:
    if day <= days_until_harvest:
        print(f"Day {day}")
        ft_count_harvest_recursive_aux(day + 1, days_until_harvest)


def ft_count_harvest_recursive() -> None:
    days_until_harvest: int = int(input("Days until harvest: "))
    ft_count_harvest_recursive_aux(1, days_until_harvest)
    print("Harvest time!")
