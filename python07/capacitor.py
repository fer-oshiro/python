#!/usr/bin/env python3
from ex1 import HealingCreatureFactory, TransformCreatureFactory


def test_healing_creature(factory: HealingCreatureFactory) -> None:
    print("Testing Creature with healing capability")

    print(" base:")
    creature_base = factory.create_base()
    creature_evolved = factory.create_evolved()
    print(creature_base.describe())
    print(creature_base.attack())
    print(creature_base.heal("itself"))
    print(" evolved:")
    print(creature_evolved.describe())
    print(creature_evolved.attack())
    print(creature_evolved.heal("itself and others"))


def test_transform_creature(factory: TransformCreatureFactory) -> None:
    print("Testing Creature with transform capability")

    print(" base:")
    creature_base = factory.create_base()
    creature_evolved = factory.create_evolved()
    print(creature_base.describe())
    print(creature_base.attack())
    print(creature_base.transform("sharper form"))
    print(creature_base.attack())
    print(creature_base.revert("normal"))
    print(" evolved:")
    print(creature_evolved.describe())
    print(creature_evolved.attack())
    print(creature_evolved.transform("dragonic battle form"))
    print(creature_evolved.attack())
    print(creature_evolved.revert("form"))


if __name__ == "__main__":
    test_healing_creature(HealingCreatureFactory())
    test_transform_creature(TransformCreatureFactory())
