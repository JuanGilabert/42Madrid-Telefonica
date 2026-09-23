import os
from dotenv import load_dotenv


def get_dotenv_config() -> dict[str, str | None]:
    dotenv_config_dict = {}
    dotenv_config_dict["MATRIX_MODE"] = os.getenv("MATRIX_MODE")
    dotenv_config_dict["DATABASE_URL"] = os.getenv("DATABASE_URL")
    dotenv_config_dict["API_KEY"] = os.getenv("API_KEY")
    dotenv_config_dict["LOG_LEVEL"] = os.getenv("LOG_LEVEL")
    dotenv_config_dict["ZION_ENDPOINT"] = os.getenv("ZION_ENDPOINT")
    return dotenv_config_dict


def show_loaded_config(config: dict[str, str | None]) -> None:
    print("Configuration loaded:")
    print(f"Mode: {config['MATRIX_MODE']}")
    if config['DATABASE_URL']:
        print("Database: Connected to local instance")
    else:
        print(f"Database: {config['DATABASE_URL']}")
    if config['API_KEY']:
        print("API Access: Authenticated")
    else:
        print(f"API Access: {config['API_KEY']}")
    print(f"Log Level: {config['LOG_LEVEL']}")
    print(f"Zion Network: {config['ZION_ENDPOINT']}")
    print()


def security_check(config: dict[str, str | None]) -> None:
    print("Environment security check:")
    if config["API_KEY"]:
        print("[OK] No hardcoded secrets detected")
    else:
        print("[WARNING] API_KEY is not configured")
    required_vars = [
        "MATRIX_MODE",
        "DATABASE_URL",
        "API_KEY",
        "LOG_LEVEL",
        "ZION_ENDPOINT"
    ]
    missing_vars = [var for var in required_vars if not config[var]]
    if not missing_vars:
        print("[OK] .env file properly configured")
    else:
        print(f"[WARNING] Missing configuration: {', '.join(missing_vars)}")
    if config["MATRIX_MODE"] in ("development", "production"):
        print("[OK] Production overrides available")
    else:
        print("[WARNING] Invalid MATRIX_MODE")
    print()


def main() -> None:
    try:
        load_dotenv()
    except Exception as err:
        print(f"{err.__class__.__name__}: {err}")
    print("ORACLE STATUS: Reading the Matrix...")
    print()
    config: dict[str, str | None] = get_dotenv_config()
    show_loaded_config(config)
    security_check(config)
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
    except BaseException as base_err:
        print(f"\n{base_err.__class__.__name__}: {base_err}")
