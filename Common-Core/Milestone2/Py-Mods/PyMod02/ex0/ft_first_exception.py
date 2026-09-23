
def input_temperature(temp_str: str) -> int:
    print(f"Input data is: {temp_str}")
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    print()
    try:
        valid_temperature: int = input_temperature("25")
        print(f"Temperature now is {valid_temperature}°C")
    except Exception as excpt:
        print(f"Caught input_temperature error: {excpt}")
    print()
    try:
        input_temperature("abc")
    except Exception as excpt:
        print(f"Caught input_temperature error: {excpt}")
    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
