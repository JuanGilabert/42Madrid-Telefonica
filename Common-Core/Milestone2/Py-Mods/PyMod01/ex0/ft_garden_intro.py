#!/usr/bin/env python

def ft_garden_intro() -> None:
    print("=== Welcome to My Garden ===")
    plant_name: str = "Rose"
    print(f"Plant: {plant_name}")
    plant_height: float = 25
    print(f"Height: {plant_height}cm")
    plant_age: int = 30
    print(f"Age: {plant_age} days")
    print()
    print("=== End of Program ===")


if __name__ == "__main__":
    ft_garden_intro()
