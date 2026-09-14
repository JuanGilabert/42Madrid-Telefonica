import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        try:
            coordinates: str = input(
                "Enter new coordinates as floats in format 'x,y,z': ")
            a, b, c = coordinates.split(",")
            x: float = float(a)
            y: float = float(b)
            z: float = float(c)
            return x, y, z
        except ValueError as error:
            if "," not in coordinates:
                print("Invalid syntax")
            else:
                print(f"Error on parameter: {error}")


def ft_coordinate_system() -> None:
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    first = get_player_pos()
    print(f"Got a first tuple: {first}")
    print(f"It includes: X={first[0]}, Y={first[1]}, Z={first[2]}")
    distance = math.sqrt(first[0] ** 2 + first[1] ** 2 + first[2] ** 2)
    print(f"Distance to center: {distance:.4f}")
    print()
    print("Get a second set of coordinates")
    second = get_player_pos()
    x = second[0] - first[0]
    y = second[1] - first[1]
    z = second[2] - first[2]
    distance = math.sqrt(x**2 + y**2 + z**2)
    print(f"Distance between the 2 sets of coordinates: {distance:.4f}")


if __name__ == "__main__":
    try:
        ft_coordinate_system()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
    except BaseException as base_err:
        print(f"\nAn unexpected error occurred: {base_err}")
