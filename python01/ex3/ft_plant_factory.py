#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, p_age: int = 0):
        self.name = name
        self.height = height
        self.p_age = p_age

    def __str__(self) -> str:
        return f"{self.name}: {self.height:.1f}cm, {self.p_age} days old"

    def show(self) -> None:
        print(self)

    def grow(self, rate: float) -> None:
        self.height = round(self.height + rate, 1)

    def age(self) -> None:
        self.p_age += 1


def main() -> None:
    plants = [
        Plant("Rose", 25.0, 30),
        Plant("Oak", 200.0, 365),
        Plant("Cactus", 5.0, 90),
        Plant("Sunflower", 80.0, 45),
        Plant("Fern", 15.0, 120)
    ]
    print("=== Plant Factory Output ===")
    for plant in plants:
        print(f"Created: {plant}")


if __name__ == "__main__":
    main()
