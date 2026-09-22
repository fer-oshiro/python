#!/usr/bin/env python3

class Plant:
    class Statistics:
        def __init__(self) -> None:
            self._grow_calls: int = 0
            self._age_calls: int = 0
            self._show_calls: int = 0

        def increment_grow(self) -> None:
            self._grow_calls += 1

        def increment_age(self) -> None:
            self._age_calls += 1

        def increment_show(self) -> None:
            self._show_calls += 1

        def __str__(self) -> str:
            return (
                f"Stats: {self._grow_calls} grow, {self._age_calls} age, "
                f"{self._show_calls} show"
            )

    def __init__(
            self,
            name: str,
            height: float = .0,
            p_age: int = 0
            ):
        self.name = name
        self._height = .0
        self._p_age = 0
        self.set_height(height)
        self.set_age(p_age)
        self._stats = self.Statistics()

    def __str__(self) -> str:
        return f"{self.name}: {self._height:.1f}cm, {self._p_age} days old"

    @staticmethod
    def is_older_than_year(days: int) -> bool:
        return days > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", .0, 0)

    def show(self) -> None:
        self._stats.increment_show()
        print(self)

    def show_stats(self) -> None:
        print(self._stats)

    def grow(self, rate: float) -> None:
        self._stats.increment_grow()
        self.set_height(round(self._height + rate, 1))

    def age(self, age: int) -> bool:
        self._stats.increment_age()
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


class Tree(Plant):
    class Statistics(Plant.Statistics):
        def __init__(self) -> None:
            super().__init__()
            self._shade_calls: int = 0

        def increment_shade(self) -> None:
            self._shade_calls += 1

        def __str__(self) -> str:
            base_stats = super().__str__()
            return f"{base_stats}\n {self._shade_calls} shade"

    def __init__(
            self,
            name: str,
            height: float,
            p_age: int = 0,
            trunk_diameter: float = 0
            ) -> None:
        self.trunk_diameter = trunk_diameter
        super().__init__(name, height, p_age)
        self._stats: Tree.Statistics = self.Statistics()

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        self._stats.increment_shade()
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self.get_height():.1f}cm long and "
            f"{self.trunk_diameter:.1f}cm wide.")


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


class Seed(Flower):
    def __init__(
            self,
            name: str,
            height: float,
            p_age: int = 0,
            color: str = "Red",
            has_bloomed: bool = False,
            qty_seed: int = 0
            ) -> None:
        self.qty_seed = qty_seed
        super().__init__(name, height, p_age, color, has_bloomed)

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self.qty_seed}")


def show_static(plant: Plant) -> None:
    plant.show_stats()


def main() -> None:
    rose = Flower("Rose", 15, 10, "red")
    oak = Tree("Oak", 200, 365, 5)
    sunflower = Seed("Sunflower", 80, 45, "yellow", False, 42)
    anonymous = Plant.create_anonymous()

    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")

    print("\n=== Flower")
    rose.show()
    print("[statistics for Rose]")
    show_static(rose)
    print("[asking the rose to grow and bloom]")
    rose.set_bloom(True)
    rose.show()
    print("[statistics for Rose]")
    show_static(rose)

    print("\n=== Tree")
    oak.show()
    print("[statistics for Oak]")
    show_static(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("[statistics for Oak]")
    show_static(oak)

    print("\n=== Seed")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30)
    sunflower.age(20)
    sunflower.set_bloom(True)
    sunflower.show()
    print("[statistics for Sunflower]")
    show_static(sunflower)

    print("\n=== Anonymous")
    anonymous.show()
    print("[statistics for Unknown plant]")
    show_static(anonymous)


if __name__ == "__main__":
    main()
