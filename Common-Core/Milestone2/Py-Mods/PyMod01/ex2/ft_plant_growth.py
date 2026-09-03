#!/usr/bin/env python

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self.height_in_cm: float = height
        self.age_in_days: int = age

    def show(self) -> None:
        height_str_msg = f"{self.height_in_cm:.2f}cm"
        age_str_msg = f"{self.age_in_days} days old"
        print(f"{self.name}: {height_str_msg}, {age_str_msg}")

    def age(self) -> None:
        self.age_in_days += 1

    def grow(self, grow: float) -> None:
        self.height_in_cm += grow


def ft_plant_growth() -> None:
    print("=== Garden Plant Growth ===")
    rose: Plant = Plant("Rose", 25, 30)
    rose.show()
    rose_growth = 0.8
    for i in range(7):
        print(f"=== Day {i + 1} ===")
        rose.grow(rose_growth)
        rose.age()
        rose.show()
    print(f"Growth this week: {(rose_growth * 7):.1f}cm")


if __name__ == "__main__":
    ft_plant_growth()
