#!/usr/bin/env python3
import random


def gen_player_achievements() -> set[str]:
    achievements = {
        'Crafting Genius', 'Strategist', 'World Savior',
        'Speed Runner', 'Survivor', 'Master Explorer',
        'Treasure Hunter', 'Unstoppable', 'First Steps',
        'Collector Supreme', 'Untouchable', 'Sharp Mind', 'Boss Slayer'
    }
    num_items = random.randint(0, len(achievements))
    subset_list = random.sample(list(achievements), k=num_items)
    return set(subset_list)


def main() -> None:
    print("=== Achievement Tracker System ===")

    print()
    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()
    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")

    print()
    distinc_achievement = set.union(alice, bob, charlie, dylan)
    print(f"All distinct achievements: {distinc_achievement}")

    print()
    common_achievements = set.intersection(alice, bob, charlie, dylan)
    print(f"Common achievements: {common_achievements}")

    print()
    all_less_alice = set.union(bob, charlie, dylan)
    print(f"Only Alice has: {set.difference(alice, all_less_alice)}")
    all_less_bob = set.union(alice, charlie, dylan)
    print(f"Only Bob has: {set.difference(bob, all_less_bob)}")
    all_less_charlie = set.union(alice, bob, dylan)
    print(f"Only Charlie has: {set.difference(charlie, all_less_charlie)}")
    all_less_dylan = set.union(alice, bob, charlie)
    print(f"Only Dylan has: {set.difference(dylan, all_less_dylan)}")

    print()
    print(f"Alice is missing: {set.difference(all_less_alice, alice)}")
    print(f"Bob is missing: {set.difference(all_less_bob, bob)}")
    print(f"Charlie is missing: {set.difference(all_less_charlie, charlie)}")
    print(f"Dylan is missing: {set.difference(all_less_dylan, dylan)}")


if __name__ == "__main__":
    main()
