#!/usr/bin/env python3
import sys


def print_error(message: str) -> None:
    sys.stdout.flush()
    sys.stderr.write(f"[STDERR] {message}\n")
    sys.stderr.flush()


def get_content(filename: str) -> list[str] | None:
    print(f"Accessing file '{filename}'")
    file = None
    data = ""
    try:
        file = open(filename, 'r')
        print("---", end="\n\n")
        data = file.read()
        print(data, end="")
        print("\n---")
    except (OSError, UnicodeDecodeError) as e:
        print_error(f"Error opening file '{filename}': {e}")
        return None
    finally:
        if file is not None:
            file.close()
            print(f"File '{filename}' closed.")
    return data.splitlines(keepends=True)


def transform_data(content: list[str]) -> list[str]:
    def update_line(line: str) -> str:
        if line[-1:] == "\n":
            return f"{line[:-1]}#\n"
        return f"{line}#"

    transform_content = []
    print("---", end="\n\n")
    for line in content:
        new_line = update_line(line)
        print(new_line, end="")
        transform_content.append(new_line)
    print("\n---")
    return transform_content


def write_content(filename: str, content: list[str]) -> None:
    print(f"Saving data to '{filename}'")
    file = None
    try:
        file = open(filename, 'w')
        for line in content:
            file.write(line)
    except OSError as e:
        print_error(f"Error opening file '{filename}': {e}")
        print("Data not saved.")
        return
    finally:
        if file is not None:
            file.close()
    print(f"Data saved in file '{filename}'.")


def read_input(label: str) -> str:
    print(label, end="", flush=True)
    return sys.stdin.readline().rstrip("\n")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
        return
    print("=== Cyber Archives Recovery & Preservation ===")
    content = get_content(sys.argv[1])
    if content is None:
        return
    print("\nTransform data:")
    content = transform_data(content)
    filename = read_input("Enter new file name (or empty): ")
    if not filename:
        print("Not saving data.")
        return
    write_content(filename, content)


if __name__ == "__main__":
    main()
