import sys
import typing


def ft_print_data(data: str) -> None:
    print("---")
    print(data)
    print("---")


def ft_get_data(filename: str) -> str | None:
    print(f"Accessing file '{filename}'")
    try:
        file: typing.IO[str] = open(filename, "r")
        data: str = file.read()
        file.close()
        ft_print_data(data)
        print(f"File '{filename}' closed.")
        return data
    except OSError as error:
        return print(f"Error opening file '{filename}': {error}")


def ft_transform_data(data: str) -> str:
    index: int = 0
    transformed: str = ""
    while index < len(data):
        if data[index] == "\n":
            transformed += "#\n"
        else:
            transformed += data[index]
        index += 1
    if len(data) > 0 and data[len(data) - 1] != "\n":
        transformed += "#"
    return transformed


def ft_save_data(data: str) -> None:
    """Ask for a filename and save the transformed data."""
    filename: str = input("Enter new file name (or empty): ")
    if filename == "":
        print("Not saving data.")
        return
    print(f"Saving data to '{filename}'")
    try:
        file: typing.IO[str] = open(filename, "w")
        file.write(data)
        file.close()
        print(f"Data saved in file '{filename}'.")
    except OSError as error:
        return print(f"Error saving file '{filename}': {error}")


def ft_archive_creation() -> None:
    """Main archive creation procedure."""
    print("=== Cyber Archives Recovery & Preservation ===")
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    data: str | None = ft_get_data(sys.argv[1])
    if data is None:
        return
    transformed_data: str = ft_transform_data(data)
    print("Transform data:")
    ft_print_data(transformed_data)
    ft_save_data(transformed_data)


if __name__ == "__main__":
    try:
        ft_archive_creation()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
    except BaseException as base_err:
        print(f"\nAn unexpected error occurred: {base_err}")
