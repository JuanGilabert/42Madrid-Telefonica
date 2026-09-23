try:
    import importlib
    from typing import Any
    from types import ModuleType
except BaseException as err:
    print(f"{err}")


REQUIRED_PACKAGES: dict[str, str] = {
    "numpy": "Numerical computation ready",
    "pandas": "Data manipulation ready",
    "matplotlib": "Visualization ready",
}
MATRIX_ANALYSIS_FILE = "matrix_analysis_distance_to_center.png"


def check_dependencies() -> dict[str, ModuleType]:
    print("Checking dependencies:")
    available_modules: dict[str, ModuleType] = {}
    for package, description in REQUIRED_PACKAGES.items():
        try:
            module: ModuleType = importlib.import_module(package)
            version = getattr(module, "__version__", "unknown_version")
            print(f"[OK] {package} ({version}) - {description}")
            available_modules[package] = module
        except ImportError:
            print(f"[MISSING] {package} - dependency not installed")
    print()
    return available_modules


def show_installation_instructions() -> None:
    print("\nMissing dependencies detected.")
    print("\nUsing pip:")
    print("  pip install -r requirements.txt")
    print("\nUsing Poetry:")
    print("  poetry install\n")


def compare_package_versions(
    available_modules: dict[str, ModuleType]
) -> None:
    print("\nPackage versions:")
    for module_name, package in available_modules.items():
        try:
            version = getattr(package, "__version__", "unknown")
            print(f"  {module_name}: {version}")
        except ImportError:
            print(f"  {module_name}: not installed")
    print()


def generate_matrix_dataset(numpy_mod: ModuleType) -> Any:
    """Generate simulated Matrix data using numpy."""
    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")
    matrix_dataset = numpy_mod.random.normal(
        loc=0,
        scale=1,
        size=(1000, 3)
    )
    return matrix_dataset


def get_analyzed_matrix_dataframe(
    numpy_mod: ModuleType,
    pandas_mod: ModuleType,
    matrix_dataset: Any
) -> Any:
    """Create a pandas DataFrame and calculate statistics."""
    dataframe = pandas_mod.DataFrame(
        matrix_dataset,
        columns=["red_pill", "blue_pill", "system"]
    )
    red_pill = dataframe["red_pill"] ** 2
    blue_pill = dataframe["blue_pill"] ** 2
    system = dataframe["system"] ** 2
    dataframe["power"] = numpy_mod.sqrt(red_pill + blue_pill + system)
    return dataframe


def create_visualization(
    matplotlib_plot_mod: ModuleType,
    dataframe: Any
) -> None:
    print("Generating visualization...")
    matplotlib_plot_mod.figure(figsize=(10, 6))
    matplotlib_plot_mod.plot(
        dataframe.index,
        dataframe["power"],
        linewidth=1
    )
    matplotlib_plot_mod.title("Matrix Data Analysis")
    matplotlib_plot_mod.xlabel("Data point")
    matplotlib_plot_mod.ylabel("System power")
    matplotlib_plot_mod.grid(True)
    matplotlib_plot_mod.tight_layout()
    matplotlib_plot_mod.savefig(MATRIX_ANALYSIS_FILE)
    matplotlib_plot_mod.close()
    print()


def main() -> None:
    print("LOADING STATUS: Loading programs...\n")
    available_modules: dict[str, ModuleType] = check_dependencies()
    for package in REQUIRED_PACKAGES:
        if package not in available_modules:
            return show_installation_instructions()
    compare_package_versions(available_modules)
    numpy_mod: ModuleType = available_modules["numpy"]
    pandas_mod: ModuleType = available_modules["pandas"]
    pyplot_mod: ModuleType = importlib.import_module("matplotlib.pyplot")
    matrix_dataframe: Any = generate_matrix_dataset(numpy_mod)
    dataframe: Any = get_analyzed_matrix_dataframe(
        numpy_mod, pandas_mod, matrix_dataframe
    )
    create_visualization(pyplot_mod, dataframe)
    print("\nAnalysis complete!")
    print(f"Results saved to: {MATRIX_ANALYSIS_FILE}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
    except BaseException as base_err:
        print(f"\nAn unexpected error occurred: {base_err}")
