from ex0.creature import Creature


class InvalidStrategyError(Exception):
    def __init__(self, creature: Creature, strategy: str) -> None:
        super().__init__(
            f"Invalid Creature '{creature.name}' for this {strategy} strategy"
        )
