#!/usr/bin/env python3
import sys


def ft_command_quest() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0].split('/')[-1]}")

    if len(sys.argv) <= 1:
        print("No arguments provided!")
        print(f"Total arguments: {len(sys.argv)}")
        return

    print(f"Arguments received: {len(sys.argv) - 1}")
    argv_index = 1
    for argv_name in sys.argv[1:]:
        print(f"Argument {argv_index}: {argv_name}")
        argv_index += 1
    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    ft_command_quest()
