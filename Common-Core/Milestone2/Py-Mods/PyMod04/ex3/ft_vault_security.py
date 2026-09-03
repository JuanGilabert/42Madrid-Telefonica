

def secure_archive(
        file_name: str, action: str, content: str
) -> tuple[bool, str]:
    if action == "read":
        try:
            with open(file_name, "r") as file:
                return (True, file.read())
        except Exception as excpt:
            return (False, f"Error opening file '{file_name}': {excpt}")
    if action == "write":
        try:
            with open(file_name, "w") as file:
                file.write(content)
                return (True, "Content successfully written to file")
        except Exception as excpt:
            return (False, f"Error writing to file '{file_name}': {excpt}")
    return (False, f"Invalid action '{action}'. Please use 'read' or 'write'.")


def ft_show_vault_security(
        msg: str, file_name: str, action: str, content: str
) -> None:
    print(f"{msg}")
    print(f"{secure_archive(file_name, action, content)}")
    print()


def ft_vault_security() -> None:
    print("=== Cyber Archives Security ===")
    print()
    read_msg: str = "Using 'secure_archive' to read from "
    nonexistent_file_name = "nonexistent_file.txt"
    nonexistent_file_msg: str = f"{read_msg} a nonexistent file:"
    ft_show_vault_security(
        nonexistent_file_msg, nonexistent_file_name, "read", ""
    )
    inaccessible_file_name = "test.txt"
    inaccessible_file_msg: str = f"{read_msg} an inaccessible file:"
    ft_show_vault_security(
        inaccessible_file_msg, inaccessible_file_name, "read", ""
    )
    regular_file_name = "test.txt"
    regular_file_msg: str = f"{read_msg} a regular file:"
    ft_show_vault_security(regular_file_msg, regular_file_name, "read", "")
    write_msg: str = "Using 'secure_archive' to write "
    content = "This is a test content."
    write_content_msg: str = f"{write_msg} previous content to a new file:"
    ft_show_vault_security(
        write_content_msg, regular_file_name, "write", content
    )


if __name__ == "__main__":
    try:
        ft_vault_security()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
    except BaseException as base_err:
        print(f"\nAn unexpected error occurred: {base_err}")
