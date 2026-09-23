import sys


def ft_get_program_name(path: str) -> str:
    i = len(path) - 1
    while i >= 0:
        if path[i] == "/" or path[i] == "\\":
            return path[i + 1:]
        i -= 1
    return path


def ft_command_quest() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {ft_get_program_name(sys.argv[0])}")
    sys_argv_count = len(sys.argv)
    if sys_argv_count < 2:
        return print("No arguments provided!")
    print(f"Arguments recived: {sys_argv_count - 1}")
    i = 1
    for argument in sys.argv[1:]:
        print(f"Argument {i}: {argument}")
        i += 1
    print(f"Total arguments: {sys_argv_count}")


if __name__ == "__main__":
    try:
        ft_command_quest()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
    except BaseException as base_err:
        print(f"\nAn unexpected error occurred: {base_err}")
