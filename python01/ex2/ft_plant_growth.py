#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, plant_age: int = 0):
        self.name = name
        self.height = height
        self.plant_age = plant_age

    def __str__(self) -> str:
        return f"{self.name}: {self.height:.1f}cm, {self.plant_age} days old"

    def show(self) -> None:
        print(self)

    def grow(self, rate: float) -> None:
        self.height = round(self.height + rate, 1)

    def age(self) -> None:
        self.plant_age += 1


def main() -> None:
    rose = Plant("Rose", 25.0, 30)

    print("=== Garden Plant Growth ===")
    rose.show()
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.grow(.8)
        rose.age()
        rose.show()
    height_diff = rose.height - 25
    print(f"Growth this week: {height_diff:.1f}cm")


if __name__ == "__main__":
    main()
