#!/usr/bin/env python3

def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int('asd')
    elif operation_number == 1:
        42/0
    elif operation_number == 2:
        open("/non/existent/file", 'r')
    elif operation_number == 3:
        "sp"+42
    else:
        return


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")

    test = 0

    while test <= 4:
        try:
            print(f"Testing operation {test}...")
            garden_operations(test)
            print("Operation completed successfully")
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")

        test += 1

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
