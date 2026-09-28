from ex0.creature import Creature
from .capability import HealCapability, TransformCapability


class Sproutling(Creature, HealCapability):
    def attack(self) -> str:
        return f"{self.name} uses Vine Whip!"

    def heal(self, target: str) -> str:
        return f"{self.name} heals {target} for a small amount"


class Bloomelle(Creature, HealCapability):
    def attack(self) -> str:
        return f"{self.name} uses Petal Dance!"

    def heal(self, target: str) -> str:
        return f"{self.name} heals {target} for a large amount"


class Shiftling(TransformCapability, Creature):
    def attack(self) -> str:
        if self.is_transformed:
            return f"{self.name} performs a boosted strike!"
        return f"{self.name} attacks normally."

    def transform(self, target: str) -> str:
        self.is_transformed = True
        return f"{self.name} shifts into a {target}!"

    def revert(self, target: str) -> str:
        self.is_transformed = False
        return f"{self.name} returns to {target}."


class Morphagon(TransformCapability, Creature):
    def attack(self) -> str:
        if self.is_transformed:
            return f"{self.name} unleashes a devastating morph strike!"
        return f"{self.name} attacks normally."

    def transform(self, target: str) -> str:
        self.is_transformed = True
        return f"{self.name} morphs into a {target}!"

    def revert(self, target: str) -> str:
        self.is_transformed = False
        return f"{self.name} stabilizes its {target}."
