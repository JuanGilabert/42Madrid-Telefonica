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


def ft_garden_data() -> None:
    print("=== Garden Plant Registry ===")
    rose_plant = Plant("Rose", 25, 30)
    rose_plant.show()
    sunflower_plant = Plant("Sunflower", 80, 45)
    sunflower_plant.show()
    cactus_plant = Plant("Cactus", 15, 120)
    cactus_plant.show()


if __name__ == "__main__":
    ft_garden_data()
