
def input_temperature(temperature: str) -> int:
    print(f"Input data is: {temperature}")
    hot_temp_msg = "ºC is too hot for plants (max 40ºC)"
    cold_temp_msg = "ºC is too cold for plants (min 0ºC)"
    temperature_int = int(temperature)
    if temperature_int > 40:
        raise ValueError(f"{temperature_int}{hot_temp_msg}")
    if temperature_int < 0:
        raise ValueError(f"{temperature_int}{cold_temp_msg}")
    return temperature_int


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")
    print()
    try:
        temperature_int = input_temperature("25")
        print(f"Temperature is now {temperature_int}ºC")
    except Exception as excpt:
        print(f"Caught input_temperature error: {excpt}")
    print()
    try:
        input_temperature("abc")
    except Exception as excpt:
        print(f"Caught input_temperature error: {excpt}")
    print()
    try:
        input_temperature("100")
    except Exception as excpt:
        print(f"Caught input_temperature error: {excpt}")
    print()
    try:
        input_temperature("-50")
    except Exception as excpt:
        print(f"Caught input_temperature error: {excpt}")
    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
