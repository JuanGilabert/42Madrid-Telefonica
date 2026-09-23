#!/usr/bin/env python

def ft_plant_age() -> None:
    plant_age_days: int = int(input("Enter plant age in days: "))
    if plant_age_days > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
