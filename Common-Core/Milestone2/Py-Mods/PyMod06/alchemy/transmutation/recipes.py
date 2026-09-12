from alchemy.elements import create_air
from elements import create_fire
from ..potions import strength_potion


def lead_to_gold() -> str:
    air = create_air()
    fire = create_fire()
    potion = strength_potion()
    return (
        f"Recipe transmuting Lead to Gold: brew '{air}' and '{potion}' "
        f"mixed with '{fire}' "
    )
