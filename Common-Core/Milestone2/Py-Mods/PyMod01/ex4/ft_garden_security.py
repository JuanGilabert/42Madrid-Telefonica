#!/usr/bin/env python

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name: str = ""
        self.set_name(name)
        self._height_in_cm: float = 0
        self.set_height(height, False)
        self._age_in_days = 0
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

    def set_height(self, height: float, show_updated_msg: bool = True) -> None:
        if type(height) not in (int, float):
            return print("height must be a number")
        if height < 0:
            print(f"{self.get_name()}: Error, height can't be negative")
            return print("Height update rejected")
        self._height_in_cm = +height
        if show_updated_msg:
            print(f"Height updated: {self._height_in_cm}cm")

    def get_age(self) -> int:
        return self._age_in_days

    def set_age(self, age: int, show_updated_msg: bool = True) -> None:
        if type(age) is not int:
            return print("age must be an integer")
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            return print("Age update rejected")
        self._age_in_days += age
        if show_updated_msg:
            print(f"Age updated: {self._age_in_days} days")

    def grow(self, grow: float) -> None:
        self._height_in_cm += grow

    def show(self) -> None:
        height_str_msg = f"{self._height_in_cm:.2f}cm"
        age_str_msg = f"{self._age_in_days} days old"
        print(f"Plant created: {self._name}: {height_str_msg}, {age_str_msg}")


def ft_garden_security() -> None:
    print("=== Garden Security System ===")
    rose = Plant("Rose", 25, 30)
    rose.show()
    print()
    rose.set_height(10)
    rose.set_age(20)
    print()
    rose.set_height(-50)
    rose.set_age(-50)
    print()
    height_str_msg = f"{rose.get_height():.2f}cm"
    age_str_msg = f"{rose.get_age()} days old"
    print(f"Current state: {rose.get_name()}: {height_str_msg}, {age_str_msg}")


if __name__ == "__main__":
    ft_garden_security()
