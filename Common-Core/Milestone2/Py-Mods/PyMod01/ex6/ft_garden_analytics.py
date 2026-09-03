#!/usr/bin/env python
from typing_extensions import override


class Plant:
    class _Stats:
        def __init__(self) -> None:
            self._grow_calls_count: int = 0
            self._age_calls_count: int = 0
            self._show_calls_count: int = 0

        def get_age_calls(self) -> int:
            return self._age_calls_count

        def set_age_calls(self) -> None:
            self._age_calls_count += 1

        def get_grow_calls(self) -> int:
            return self._grow_calls_count

        def set_grow_calls(self) -> None:
            self._grow_calls_count += 1

        def get_show_calls(self) -> int:
            return self._show_calls_count

        def set_show_calls(self) -> None:
            self._show_calls_count += 1

        def show(self) -> None:
            grow_msg: str = f"{self._grow_calls_count} grow"
            age_msg: str = f"{self._age_calls_count} age"
            show_msg: str = f"{self._show_calls_count} show"
            print(f"Stats: {grow_msg}, {age_msg}, {show_msg}")

    def __init__(self, name: str, height: float, age: int) -> None:
        self._stats = self._Stats()
        self._name: str = ""
        self.set_name(name)
        self._height_in_cm: float = 0
        self.set_height(height)
        self._age_in_days: int = 0
        self.set_age(age, False)

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

    def set_age(self, age: int, set_age_calls: bool = True) -> None:
        if type(age) is not int:
            return print("age must be an integer")
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            return print("Age update rejected")
        self._age_in_days += age
        if set_age_calls:
            self._stats.set_age_calls()

    def grow(self, grow: float) -> None:
        self._height_in_cm += grow
        self._stats.set_grow_calls()

    def show(self) -> None:
        self._stats.set_show_calls()
        height_str_msg = f"{self._height_in_cm:.1f}cm"
        age_str_msg = f"{self._age_in_days} days old"
        print(f"{self._name}: {height_str_msg}, {age_str_msg}")

    @staticmethod
    def is_old(self, age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0, 0)

    def get_stats(self) -> None:
        print(f"[statistics for {self._name}]")
        self._stats.show()


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color: str = color
        self._has_blooming: bool = False
        self._hold_number_of_seeds: bool = False

    def bloom(self) -> None:
        if self._has_blooming:
            return print(f"{self._name} is blooming beautifully!")
        print(f"{self._name} has not bloomed yet")
        self._has_blooming = True

    @override
    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self._number_of_seeds: int = 0

    @override
    def bloom(self) -> None:
        super().bloom()
        if self._hold_number_of_seeds:
            self._number_of_seeds = 42
        print(f"Seeds: {self._number_of_seeds}")
        self._hold_number_of_seeds = True

    @override
    def show(self) -> None:
        super().show()


class Tree(Plant):
    class _TreeStats(Plant._Stats):
        def __init__(self) -> None:
            super().__init__()
            self._produce_shade_calls_count: int = 0

        def get_produce_shade_calls(self) -> int:
            return self._produce_shade_calls_count

        def set_produce_shade_calls(self) -> None:
            self._produce_shade_calls_count += 1

        @override
        def show(self) -> None:
            super().show()
            print(f"{self._produce_shade_calls_count} shade")

    def __init__(self, name: str, height: float,
                 age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter: float = trunk_diameter
        self._tree_stats = Tree._TreeStats()

    def produce_shade(self) -> None:
        print(f"[asking the {self._name} to produce shade]")
        shade_msg: str = f"a shade of {self._height_in_cm:.1f}cm long"
        diameter_msg: str = f"and {self._trunk_diameter:.1f}cm wide"
        print(f"Tree {self._name} now produces {shade_msg} {diameter_msg}.")
        self._tree_stats.set_produce_shade_calls()

    @override
    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter:.1f}cm")

    def get_stats(self) -> None:
        print(f"[statistics for {self._name}]")
        self._tree_stats.show()


def ft_show_flowers() -> None:
    print("=== Flower")
    flower = Flower("Rose", 15, 10, "Red")
    flower.show()
    flower.bloom()
    flower.get_stats()
    print(f"[asking the {flower.get_name()} to grow and bloom]")
    flower.grow(8)
    flower.show()
    flower.bloom()
    flower.get_stats()
    print()


def ft_show_trees() -> None:
    print("=== Tree")
    tree = Tree("Oak", 200, 365, 5)
    tree.show()
    tree.get_stats()
    tree.produce_shade()
    tree.get_stats()
    print()


def ft_show_seeds() -> None:
    print("=== Seed")
    sunflower_seed = Seed("Sunflower", 80, 45, "Yellow")
    sunflower_seed.show()
    sunflower_seed.bloom()
    print(f"[make {sunflower_seed.get_name()} grow, age and bloom]")
    sunflower_seed.grow(30)
    sunflower_seed.set_age(20)
    sunflower_seed.show()
    sunflower_seed.bloom()
    sunflower_seed.get_stats()
    print()


def ft_show_anonymous_plant() -> None:
    print("=== Anonymous")
    anonymous_plant = Plant.create_anonymous()
    anonymous_plant.show()
    anonymous_plant.get_stats()
    print()


def ft_show_plant_analytics(plant: Plant) -> None:
    plant.show()
    plant.get_stats()
    print()


def ft_show_analytics() -> None:
    print("=== Statistics ===")
    rose_flower = Flower("Rose", 15, 10, "Red")
    ft_show_plant_analytics(rose_flower)
    oak_tree = Tree("Oak", 200, 365, 5)
    ft_show_plant_analytics(oak_tree)
    sunflower_seed = Seed("Sunflower", 80, 45, "Yellow")
    ft_show_plant_analytics(sunflower_seed)


def ft_show_garden_analytics() -> None:
    ft_show_flowers()
    ft_show_trees()
    ft_show_seeds()
    ft_show_anonymous_plant()
    ft_show_analytics()


def ft_garden_analytics() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_old(Plant, 30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_old(Plant, 400)}")
    print()
    ft_show_garden_analytics()


if __name__ == "__main__":
    ft_garden_analytics()
