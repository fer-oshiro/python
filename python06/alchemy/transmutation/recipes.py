from ..potions import strength_potion
from ..elements import create_air
from elements import create_fire


def lead_to_gold() -> str:
    return (
        "Recipe transmuting Lead to Gold: "
        f"brew '{create_air()}' "
        f"and '{strength_potion()}' "
        f"mixed with '{create_fire()}'"
    )
