#!/usr/bin/env python3
import math


class InvalidSyntax(Exception):
    def __init__(self, message: str = "Invalid syntax") -> None:
        super().__init__(message)


def get_user_coord() -> tuple[float, float, float]:
    while True:
        try:
            coord_raw = input(
                "Enter new coordinates " +
                "as floats in format 'x,y,z': "
                )
            if len(coord_raw.split(",")) != 3:
                raise InvalidSyntax()
            coord_list: list[float] = []
            for item in coord_raw.split(","):
                try:
                    coord_list.append(float(item))
                except ValueError as e:
                    print(f"Error on parameter '{item}': {e}")

            if len(coord_list) != 3:
                raise ValueError()
            [x, y, z] = coord_list
            coordination = (x, y, z)
            return coordination
        except InvalidSyntax as e:
            print(e)
        except ValueError:
            pass


def get_distance(
        coord: tuple[float, float, float],
        coord_2: tuple[float, float, float] = (0, 0, 0)) -> float:

    distance = .0
    for axis in [0, 1, 2]:
        distance += (coord[axis] - coord_2[axis]) ** 2

    return round(math.sqrt(distance), 4)


def get_player_pos() -> None:
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    coord_1 = get_user_coord()
    print(f"Got a first tuple: {coord_1}")
    print(f"It includes: X={coord_1[0]}, Y={coord_1[1]}, Z={coord_1[2]}")
    print(f"Distance to center: {get_distance(coord_1)}")
    coord_2 = get_user_coord()
    print(
        "Distance between the 2 sets of coordinates: " +
        f"{get_distance(coord_1, coord_2)}"
        )


if __name__ == "__main__":
    get_player_pos()
