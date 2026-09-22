#!/usr/bin/env python3
import sys


class InventoryError(Exception):
    pass


class RedundantItem(InventoryError):
    def __init__(self, item: str = "unknow") -> None:
        message = f"Redundant item '{item}' - discarding"
        super().__init__(message)


class InvalidParam(InventoryError):
    def __init__(self, item: str = "unknow") -> None:
        message = f"Error - invalid parameter '{item}'"
        super().__init__(message)


class Inventory:
    def __init__(self) -> None:
        self.inventory: dict[str, int] = {}

    def __str__(self) -> str:
        return f"{self.inventory}"

    def add_item(self, key: str, value: str | int) -> None:
        if key in self.inventory:
            raise RedundantItem(key)
        try:
            self.inventory[key] = int(value)
        except ValueError as e:
            print(f"Quantity error for '{key}': {e}")

    def get_items(self) -> list[str]:
        return list(self.inventory.keys())

    def get_qty(self, key: str) -> int:
        if key == "keys":
            return len(self.get_items())
        if key == "values":
            return sum(self.inventory.values())
        raise ValueError("unknow type")

    def show_weight_distribution(self) -> None:
        for item in self.inventory:

            percent = (self.inventory[item] / self.get_qty("values")) * 100
            print(f"Item {item} represents {round(percent, 1)}%")

    def show_abundant(self, type: str) -> None:
        if not self.inventory:
            return
        compare = (int.__gt__) if type == "most" else (int.__lt__)
        curr_value = None
        key_value = None
        for key, item in self.inventory.items():
            if curr_value is None or compare(item, curr_value):
                curr_value = item
                key_value = key

        print(f"Item {type} abundant: {key_value} with quantity {curr_value}")


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory = Inventory()
    for arg in sys.argv[1:]:
        try:
            if ":" not in arg:
                raise InvalidParam(arg)
            [key, value] = arg.split(":", 1)
            inventory.add_item(key.strip(), value.strip())
        except InventoryError as e:
            print(e)

    print(f"Got inventory: {inventory}")
    print(f"Item list: {inventory.get_items()}")
    print(
        f"Total quantity of the {inventory.get_qty('keys')} items: "
        f"{inventory.get_qty('values')}"
        )
    inventory.show_weight_distribution()
    inventory.show_abundant("most")
    inventory.show_abundant("least")
    inventory.add_item("magic", 1)
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
