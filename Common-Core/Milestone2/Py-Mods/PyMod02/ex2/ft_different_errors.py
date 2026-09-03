
def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        10 / 0
    elif operation_number == 2:
        open("/non/existent/file", "r")
    elif operation_number == 3:
        "plant" + 42
    else:
        return


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    print("Testing operation 0...")
    try:
        garden_operations(0)
    except ValueError as error:
        print(f"Caught ValueError: {error}")
    print("Testing operation 1...")
    try:
        garden_operations(1)
    except ZeroDivisionError as error:
        print(f"Caught ZeroDivisionError: {error}")
    print("Testing operation 2...")
    try:
        garden_operations(2)
    except FileNotFoundError as error:
        print(f"Caught FileNotFoundError: {error}")
    print("Testing operation 3...")
    try:
        garden_operations(3)
    except TypeError as error:
        print(f"Caught TypeError: {error}")
    print("Testing operation 4...")
    try:
        garden_operations(4)
        print("Operation completed successfully")
    except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError):
        pass
    print()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
