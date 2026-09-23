from enum import Enum
from datetime import datetime
from pydantic import BaseModel, Field
from pydantic import model_validator, ValidationError


class Rank(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def after_validation(self) -> "SpaceMission":
        if not self.mission_id[0] == "M":
            raise ValueError("Mission ID must start with 'M'")
        for crew_member in self.crew:
            if crew_member.rank in [Rank.COMMANDER, Rank.CAPTAIN]:
                break
        else:
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )
        experienced = sum(
            member.years_experience >= 5
            for member in self.crew
        )
        if self.duration_days > 365:
            if experienced / len(self.crew) < 0.5:
                raise ValueError(
                    "Long missions need 50% experienced crew (5+ years)"
                )
        for crew_member in self.crew:
            if not crew_member.is_active:
                raise ValueError("All crew members must be active")
        member_ids = [member.member_id for member in self.crew]
        if len(member_ids) != len(set(member_ids)):
            raise ValueError("Crew members must have unique member IDs")
        return self


def get_crew_members_list() -> list[CrewMember]:
    crew_member_0 = CrewMember(
        member_id="CM001",
        rank=Rank.COMMANDER,
        name="Sarah Connor",
        age=35,
        specialization="Mission Command",
        years_experience=10
    )
    crew_member_1 = CrewMember(
        member_id="CM002",
        name="John Smith",
        rank=Rank.LIEUTENANT,
        age=28,
        specialization="Navigation",
        years_experience=5
    )
    crew_member_2 = CrewMember(
        member_id="CM003",
        name="Alice Johnson",
        rank=Rank.OFFICER,
        age=42,
        specialization="Engineering",
        years_experience=8
    )
    return [crew_member_0, crew_member_1, crew_member_2]


def show_valid_mission(mission: SpaceMission) -> None:
    print(f"{'=' * 40}")
    print("Valid mission created:")
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: {mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for crew_member in mission.crew:
        print(
            f"- {crew_member.name} "
            f"({crew_member.rank.value}) - "
            f"{crew_member.specialization}"
        )
    print()


def create_valid_mission() -> None:
    mission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date=datetime(2026, 9, 18, 19, 37, 23),
        duration_days=900,
        crew=get_crew_members_list(),
        budget_millions=2500.0
    )
    show_valid_mission(mission)


def create_invalid_mission() -> None:
    print(f"{'=' * 40}")
    crew_members = get_crew_members_list()
    crew_members[0].rank = Rank.CADET
    try:
        SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2026, 9, 18, 19, 37, 23),
            duration_days=900,
            crew=crew_members,
            budget_millions=2500.0
        )
    except ValidationError as error:
        print("Expected validation error:")
        print(str(error.errors()[0]["ctx"]["error"]))
    print()


def main() -> None:
    print("Space Mission Crew Validation")
    create_valid_mission()
    create_invalid_mission()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
    except BaseException as base_err:
        print(f"\nAn unexpected error occurred: {base_err}")
