import os
import sys
import site


def show_venv_info() -> None:
    print("MATRIX STATUS: Welcome to the construct\n")
    print("Current Python:", sys.executable)
    env_path = sys.prefix
    env_name = os.path.basename(env_path)
    print(f"Virtual Environment: {env_name}")
    print(f"Environment Path: {env_path}\n")
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting the global system.\n")
    print("Package installation path:")
    print(f"{site.getsitepackages()[0]}\n")


def show_normal_info() -> None:
    print("MATRIX STATUS: You're still plugged in\n")
    print("Current Python:", sys.executable)
    print("Virtual Environment: None detected\n")
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.\n")
    print("To enter the construct, run:")
    print("python3 -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env\\Scripts\\activate # On Windows\n")
    print("Then run this program again.\n")


def main() -> None:
    if sys.prefix == sys.base_prefix:
        show_normal_info()
    else:
        show_venv_info()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
    except BaseException as base_err:
        print(f"\nAn unexpected error occurred: {base_err}")
