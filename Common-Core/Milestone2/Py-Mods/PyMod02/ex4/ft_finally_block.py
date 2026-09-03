
class PlantError(Exception):
    def __str__(self) -> str:
        if not self.args:
            return f"Caught {self.__class__.__name__} Unknown plant error"
        return f"Caught {self.__class__.__name__}: {self.args[0]}"


def water_plant(plant_name: str) -> None:
    if plant_name == plant_name.capitalize():
        return print(f"Watering {plant_name}: [OK]")
    raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")
    print()
    print("Testing valid plants...")
    print("Opening watering system")
    try:
        water_plant("Tomato")
        water_plant("Lettuce")
        water_plant("Carrots")
    except PlantError as garden_excpt:
        print(f"{garden_excpt}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")
        print()
    print("Testing invalid plants...")
    print("Opening watering system")
    try:
        water_plant("Tomato")
        water_plant("lettuce")
    except PlantError as garden_excpt:
        print(f"{garden_excpt}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")
        print()
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
