#!/usr/bin/env python3

from ex0 import FlameFactory, AquaFactory, CreatureFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    creature_base = factory.create_base()
    creature_evolved = factory.create_evolved()
    print(creature_base.describe())
    print(creature_base.attack())
    print(creature_evolved.describe())
    print(creature_evolved.attack())


def battle(factory_a: CreatureFactory, factory_b: CreatureFactory) -> None:
    print("Testing battle")
    creature_a = factory_a.create_base()
    creature_b = factory_b.create_base()
    print(creature_a.describe())
    print(" vs.")
    print(creature_b.describe())
    print(" fight!")
    print(creature_a.attack())
    print(creature_b.attack())


if __name__ == "__main__":

    flame_factory = FlameFactory()
    test_factory(flame_factory)

    print()
    aqua_factory = AquaFactory()
    test_factory(aqua_factory)

    print()
    battle(flame_factory, aqua_factory)
