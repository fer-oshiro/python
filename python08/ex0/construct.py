#!/usr/bin/env python3
import sys
import site
import os


def print_color(text: str, color: str = "", bold: bool = False) -> None:
    if not sys.stdout.isatty():
        return print(text)
    colors: dict[str, str] = {
        "red": "31",
        "green": "32",
        "yellow": "33",
        "blue": "34",
    }
    code = colors.get(color, "39")
    print(f"\033[{'1;' if bold else ''}{code}m{text}\033[0m")


def instruction_venv() -> None:
    print_color("MATRIX STATUS: You're still plugged in\n", "green", True)
    print_color(f"Current Python: {sys.executable}")
    print_color("Virtual Environment: None detected\n")
    print_color("WARNING: You're in the global environment!", "red", bold=True)
    print_color("The machines can see everything you install.\n", "red")
    print_color(
        f"Global package path: {site.getsitepackages()[0]}\n",
        "yellow"
        )
    print_color("To enter the construct, run:", "blue", True)
    print_color("python -m venv matrix_env", "blue")
    print_color("source matrix_env/bin/activate # On Unix", "blue")
    print_color("matrix_env\\Scripts\\activate  # On Windows\n", "blue")
    print_color("Then run this program again.\n")


def details_venv() -> None:
    print_color("MATRIX STATUS: Welcome to the construct\n", "green", True)
    print_color(f"Current Python: {sys.executable}")
    print_color(f"Virtual Environment: {os.path.basename(sys.prefix)}")
    print_color(f"Environment Path: {sys.prefix}\n")
    print_color("SUCCESS: You're in an isolated environment!", "green")
    print_color("Safe to install packages without affecting")
    print_color("the global system.\n")
    print_color("Package installation path:", "", bold=True)
    print_color(f"{site.getsitepackages()[0]}\n")
    print_color("Global Python (outside the construct):", "", bold=True)
    print_color(sys.base_prefix)


def main() -> None:
    in_venv = sys.prefix != sys.base_prefix
    if in_venv:
        return details_venv()
    instruction_venv()


if __name__ == "__main__":
    main()
