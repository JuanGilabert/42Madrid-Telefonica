#!/usr/bin/env python

def ft_harvest_total() -> None:
    day_1: int = int(input("Day 1 harvest: "))
    day_2: int = int(input("Day 2 harvest: "))
    day_3: int = int(input("Day 3 harvest: "))
    print(f"Total harvest: {day_1 + day_2 + day_3}")
