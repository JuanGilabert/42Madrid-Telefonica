#!/usr/bin/env python

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name: str = ""
        self.set_name(name)
        self._height_in_cm: float = 0
        self.set_height(height)
        self._age_in_days: int = 0
        self.set_age(age)

    def get_name(self) -> str:
        return self._name

    def set_name(self, new_name: str) -> None:
        if type(new_name) is not str:
            return print("Error, name must be a string")
        if not new_name:
            print("Error, name can't be empty")
            return print("Name update rejected")
        self._name = new_name

    def get_height(self) -> float:
        return self._height_in_cm

    def set_height(self, height: float) -> None:
        if type(height) not in (int, float):
            return print("height must be a number")
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            return print("Height update rejected")
        self._height_in_cm += height

    def get_age(self) -> int:
        return self._age_in_days

    def set_age(self, age: int) -> None:
        if type(age) is not int:
            return print("age must be an integer")
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            return print("Age update rejected")
        self._age_in_days += age

    def grow(self, grow: float) -> None:
        self._height_in_cm += grow

    def show(self) -> None:
        height_str_msg = f"{self._height_in_cm:.2f}cm"
        age_str_msg = f"{self._age_in_days} days old"
        print(f"{self._name}: {height_str_msg}, {age_str_msg}")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color: str = color
        self._has_blooming: bool = False

    def bloom(self) -> None:
        if self._has_blooming:
            return print(f"{self._name} is blooming beautifully!")
        print(f"{self._name} has not bloomed yet")
        self._has_blooming = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter: float = trunk_diameter

    def produce_shade(self) -> None:
        print(f"[asking the {self._name} to produce shade]")
        shade_msg: str = f"a shade of {self._height_in_cm:.1f}cm long"
        diameter_msg: str = f"and {self._trunk_diameter:.1f}cm wide"
        print(f"Tree {self._name} now produces {shade_msg} {diameter_msg}.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float,
                 age: int, harvest_season: str) -> None:
        self._nutritional_value: int = 0
        self._has_plant_nourish: bool = False
        self._harvest_season: str = harvest_season
        super().__init__(name, height, age)

    def set_age(self, age: int) -> None:
        super().set_age(age)
        if self._has_plant_nourish:
            self._nutritional_value += age
        self._has_plant_nourish = True

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")


def ft_show_flowers() -> None:
    print("=== Flower")
    rose_flower = Flower("Rose", 15, 10, "Red")
    rose_flower.show()
    rose_flower.bloom()
    print(f"[asking the {rose_flower.get_name()} to bloom]")
    rose_flower.show()
    rose_flower.bloom()
    print()


def ft_show_trees() -> None:
    print("=== Tree")
    oak_tree = Tree("Oak", 200, 365, 5)
    oak_tree.show()
    oak_tree.produce_shade()
    print()


def ft_show_vegetables() -> None:
    print("=== Vegetable")
    tomato_vegetable = Vegetable("Tomato", 5, 10, "April")
    tomato_vegetable.show()
    print("[make tomato grow and age for 20 days]")
    tomato_vegetable.grow(42)
    tomato_vegetable.set_age(20)
    tomato_vegetable.show()
    print()


def ft_plant_types() -> None:
    print("=== Garden Plant Types ===")
    ft_show_flowers()
    ft_show_trees()
    ft_show_vegetables()


if __name__ == "__main__":
    ft_plant_types()
