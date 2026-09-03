import sys
import typing


def ft_ancient_text() -> None:
    if len(sys.argv) != 2:
        return print("Usage: ft_ancient_text.py <file>")
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{sys.argv[1]}'")
    try:
        file: typing.IO[str] = open(sys.argv[1], "r")
        text = file.read()
        file.close()
        print("---")
        print(text)
        print("---")
        print(f"File '{sys.argv[1]}' closed.")
    except Exception as excpt:
        return print(f"Error opening file '{sys.argv[1]}': {excpt}")


if __name__ == "__main__":
    try:
        ft_ancient_text()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
    except BaseException as base_err:
        print(f"\nAn unexpected error occurred: {base_err}")
