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

    def age(self, age: int) -> bool:
        return self.set_age(self.get_age() + age)

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


class Flower(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            p_age: int = 0,
            color: str = "Red",
            has_bloomed: bool = False
            ) -> None:
        self._color = color
        self.has_bloomed = has_bloomed
        super().__init__(name, height, p_age)

    def show(self) -> None:
        super().show()
        print(f" Color: {self.get_color()}")
        print(f" {self.bloom()}")

    def get_color(self) -> str:
        return self._color

    def set_bloom(self, value: bool) -> None:
        self.has_bloomed = value

    def bloom(self) -> str:
        if not self.has_bloomed:
            return f"{self.name} has not bloomed yet"
        return f"{self.name} is blooming beautifully!"


class Tree(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            p_age: int = 0,
            trunk_diameter: float = 0
            ) -> None:
        self.trunk_diameter = trunk_diameter
        super().__init__(name, height, p_age)

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self.get_height():.1f}cm long and "
            f"{self.trunk_diameter:.1f}cm wide.")


class Vegetable(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            p_age: int,
            harvest_season: str,
            ) -> None:
        self.harvest_season = harvest_season
        self.nutritional_value = 0
        super().__init__(name, height, p_age)

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")

    def age(self, age: int) -> bool:
        if not super().age(age):
            return False
        self.nutritional_value += age
        return True

    def produce_shade(self) -> None:
        print(f"{self.name} is blooming with {self.harvest_season} flowers!")


def main() -> None:
    rose = Flower("Rose", 15, 10, "red")
    oak_tree = Tree("Oak", 200, 365, 5)
    tomato = Vegetable("Tomato", 5, 10, "April")

    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose.show()
    print("[asking the rose to bloom]")
    rose.set_bloom(True)
    rose.show()

    print("\n=== Tree")
    oak_tree.show()
    print("[asking the oak to produce shade]")
    oak_tree.produce_shade()

    print("\n=== Vegetable")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    tomato.age(20)
    tomato.grow(42.0)
    tomato.show()


if __name__ == "__main__":
    main()
