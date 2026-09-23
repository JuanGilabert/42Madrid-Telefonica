from enum import Enum
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from pydantic import model_validator, ValidationError


class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def after_validation(self) -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")
        if self.contact_type == ContactType.PHYSICAL:
            if not self.is_verified:
                raise ValueError("Physical contact reports must be verified")
        if self.contact_type == ContactType.TELEPATHIC:
            if self.witness_count < 3:
                raise ValueError(
                    "Telepathic contact requires at least 3 witnesses"
                )
        if self.signal_strength > 7.0:
            if not self.message_received:
                raise ValueError(
                    "Strong signals should include received messages"
                )
        return self


def show_valid_alien_contact(alien_contact: AlienContact) -> None:
    print("Valid contact report:")
    print(f"ID: {alien_contact.contact_id}")
    print(f"Type: {alien_contact.contact_type}")
    print(f"Location: {alien_contact.location}")
    print(f"Signal: {alien_contact.signal_strength}/10")
    print(f"Duration: {alien_contact.duration_minutes} minutes")
    print(f"Witnesses: {alien_contact.witness_count}")
    if alien_contact.message_received:
        print(f"Message: '{alien_contact.message_received}'")
    print()


def create_valid_alien_contact() -> None:
    print(f"{'=' * 40}")
    alien_contact = AlienContact(
        contact_id="AC_2024_001",
        timestamp=datetime.now(),
        location="rea 51, Nevada",
        contact_type=ContactType.RADIO,
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli",
        is_verified=True
    )
    show_valid_alien_contact(alien_contact)


def create_invalid_alien_contact() -> None:
    print(f"{'=' * 40}")
    try:
        AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            location="rea 51, Nevada",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=2,
            message_received="Greetings from Zeta Reticuli",
            is_verified=True
        )
    except ValidationError as error:
        print("Expected validation error:")
        print(str(error.errors()[0]["ctx"]["error"]))
    print()


def main() -> None:
    print("Alien Contact Log Validation")
    create_valid_alien_contact()
    create_invalid_alien_contact()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
    except BaseException as base_err:
        print(f"\nAn unexpected error occurred: {base_err}")
