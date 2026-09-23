from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)


def show_valid_space_station(station: SpaceStation) -> None:
    print("Valid station created:")
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    status: str = "Non-Operational"
    if station.is_operational:
        status = "Operational"
    print(f"Status: {status}")
    if station.notes:
        print(f"Notes: {station.notes}")
    print()


def create_valid_space_station() -> None:
    print(f"{'=' * 40}")
    station = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance=datetime.now(),
        notes=""
    )
    show_valid_space_station(station)


def create_invalid_space_station() -> None:
    print(f"{'=' * 40}")
    try:
        SpaceStation(
            station_id="ISS002",
            name="Invalid Station",
            crew_size=25,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime(2026, 9, 12, 14, 30, 0)
        )
    except ValidationError as error:
        error_msg = error.errors()[0]["msg"]
        print(f"Expected validation error:\n{error_msg}")
    print()


def main() -> None:
    print("Space Station Data Validation")
    create_valid_space_station()
    create_invalid_space_station()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
    except BaseException as base_err:
        print(f"\nAn unexpected error occurred: {base_err}")
