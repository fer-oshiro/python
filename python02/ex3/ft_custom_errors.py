#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error"):
        super().__init__(message)


def check_plant(plant: str, is_wilting: bool) -> None:
    if is_wilting:
        raise PlantError(f"The {plant} plant is wilting!")


def check_water(amount: float) -> None:
    if amount < 10:
        raise WaterError("Not enough water in the tank!")


def test_all_catch() -> None:
    print("=== Custom Garden Errors Demo ===")

    print("\nTesting PlantError...")
    try:
        check_plant("tomato", True)
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError...")
    try:
        check_water(0)
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")
    try:
        check_plant("tomato", True)
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    try:
        check_water(0)
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_all_catch()
