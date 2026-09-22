#!/usr/bin/env python3

def secure_archive(
        filename: str, mode: str = "r", content: str = ""
        ) -> tuple[bool, str]:
    if mode not in ("r", "w"):
        return (False, f"Invalid mode '{mode}': use 'r' or 'w'")
    try:
        with open(filename, mode, encoding="utf-8") as file:
            if mode == "r":
                content = file.read()
                return (True, content)
            else:
                file.write(content)
                return (True, "Content successfully written to file")
    except (OSError, UnicodeDecodeError) as e:
        return (False, str(e))


def main() -> None:
    print("=== Cyber Archives Security ===")

    print()
    print("Using 'secure_archive' to read from a nonexistent file:")
    content = secure_archive("/not/existing/file", "r")
    print(content)

    print()
    print("Using 'secure_archive' to read from an inaccessible file:")
    content = secure_archive("/etc/shadow", "r")
    print(content)

    print()
    print("Using 'secure_archive' to write content to a new file:")
    content = secure_archive(
        "vault_backup.txt", "w", "recovered fragment data\n"
        )
    print(content)

    print()
    print("Using 'secure_archive' to read from a regular file:")
    content = secure_archive("vault_backup.txt", "r")
    print(content)


if __name__ == "__main__":
    main()
