from alchemy.elements import create_earth, create_air
import elements as root_elements


def healing_potion() -> str:
    return (
        f"Healing potion brewed with "
        f"'{create_earth()}' and '{create_air()}'"
    )


def strength_potion() -> str:
    return (
        f"Strength potion brewed with "
        f"'{root_elements.create_fire()}' and '{root_elements.create_water()}'"
    )
