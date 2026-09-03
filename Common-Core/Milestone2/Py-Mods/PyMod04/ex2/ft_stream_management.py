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
        stderr_msg = "[STDERR] Error opening file "
        sys.stderr.write(f"{stderr_msg}'{filename}': {error}\n")
        return None


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
    sys.stdout.write("Enter new file name (or empty): ")
    filename: str = sys.stdin.readline().strip()
    if filename == "":
        return print("Not saving data.")
    print(f"Saving data to '{filename}'")
    try:
        file: typing.IO[str] = open(filename, "w")
        file.write(data)
        file.close()
        print(f"Data saved in file '{filename}'.")
    except OSError as error:
        stderr_msg = "[STDERR] Error opening file "
        sys.stderr.write(f"{stderr_msg}'{filename}': {error}\n")
        sys.stderr.write("Data not saved.\n")
        return None


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
