#!/usr/bin/env python

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height_in_cm = height
        self._age_in_days = age

    def show(self) -> None:
        height_str_msg = f"{self._height_in_cm:.2f}cm"
        age_str_msg = f"{self._age_in_days} days old"
        print(f"Created: {self._name}: {height_str_msg}, {age_str_msg}")

    def age(self) -> None:
        self._age_in_days += 1

    def grow(self, grow: float) -> None:
        self._height_in_cm += grow


def ft_create_plant(name: str, height: float, age: int) -> None:
    plant = Plant(name, height, age)
    plant.show()


def ft_plant_factory() -> None:
    print("=== Plant Factory Output ===")
    ft_create_plant("Rose", 25, 30)
    ft_create_plant("Oak", 200, 365)
    ft_create_plant("Cactus", 15, 120)
    ft_create_plant("Sunflower", 80, 45)
    ft_create_plant("Fern", 15, 120)


if __name__ == "__main__":
    ft_plant_factory()
