
class GardenError(Exception):
    def __str__(self) -> str:
        if not self.args:
            return f"Caught {self.__class__.__name__}: Unknown garden error"
        return f"Caught {self.__class__.__name__}: {self.args[0]}"


class PlantError(GardenError):
    def __str__(self) -> str:
        if not self.args:
            return f"Caught {self.__class__.__name__}: Unknown plant error"
        return f"Caught {self.__class__.__name__}: {self.args[0]}"


class WaterError(GardenError):
    def __str__(self) -> str:
        if not self.args:
            return f"Caught {self.__class__.__name__}: Unknown water error"
        return f"Caught {self.__class__.__name__}: {self.args[0]}"


def ft_test_plant_error() -> None:
    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as garden_excpt:
        print(f"{garden_excpt}")
    print()


def ft_test_water_error() -> None:
    print("Testing WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as water_excpt:
        print(f"{water_excpt}")
    print()


def ft_test_garden_error() -> None:
    print("Testing catching all garden errors...")
    try:
        raise GardenError("The tomato plant is wilting!")
    except GardenError as garden_excpt:
        print(f"{garden_excpt}")
    try:
        raise GardenError("Not enough water in the tank!")
    except GardenError as garden_excpt:
        print(f"{garden_excpt}")
    print()


def ft_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")
    print()
    ft_test_plant_error()
    ft_test_water_error()
    ft_test_garden_error()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    ft_custom_errors()
