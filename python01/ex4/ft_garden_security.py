#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, p_age: int = 0):
        self.name = name
        self._height = .0
        self._p_age = 0
        self.set_height(height)
        self.set_age(p_age)

    def __str__(self) -> str:
        return f"{self.name}: {self._height:.1f}cm, {self._p_age} days old"

    def show(self) -> None:
        print(self)

    def grow(self, rate: float) -> None:
        self.set_height(round(self._height + rate, 1))

    def age(self) -> None:
        self.set_age(self.get_age() + 1)

    def set_height(self, height: float) -> bool:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            return False
        self._height = height
        return True

    def set_age(self, age: int) -> bool:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            return False
        self._p_age = age
        return True

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._p_age


def main() -> None:
    rose = Plant("Rose", 15.0, 10)
    print("=== Garden Security System ===")
    print(f"Plant created: {rose}")

    if rose.set_height(25):
        print(f"\nHeight updated: {rose.get_height()}cm")
    if rose.set_age(30):
        print(f"Age updated: {rose.get_age()} days\n")
    if not rose.set_height(-10.0):
        print("Height update rejected")
    if not rose.set_age(-5):
        print("Age update rejected")

    print(f"Current state: {rose}")


if __name__ == "__main__":
    main()
