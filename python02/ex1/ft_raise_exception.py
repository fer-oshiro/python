#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    temperature = int(temp_str)
    if temperature < 0:
        raise ValueError(f"{temperature}°C is too cold for plants (min 0°C)")
    if temperature > 40:
        raise ValueError(f"{temperature}°C is too hot for plants (max 40°C)")
    return temperature


def test_temperature() -> None:
    print("=== Garden Temperature ===")

    try:
        print("\nInput data is '25'")
        print(f"Temperature is now {input_temperature('25')}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    try:
        print("\nInput data is 'abc'")
        input_temperature(f"Temperature is now {input_temperature('abc')}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    try:
        print("\nInput data is '100'")
        input_temperature(f"Temperature is now {input_temperature('100')}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    try:
        print("\nIInput data is '-50'")
        input_temperature(f"Temperature is now {input_temperature('-50')}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
