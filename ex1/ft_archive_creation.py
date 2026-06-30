#!/usr/bin/env python3

import sys
import typing


def get_err_msg(path: str, err: Exception) -> str:
    return f"Error opening file '{path}': {err}"


def print_content(text: str) -> None:
    print("---\n")
    print(text, end="")
    print("\n---")


def main() -> None:
    script_name = sys.argv[0]
    args = sys.argv[1:]

    if not args or len(args) > 1:
        print(f"Usage: {script_name} <file>")
        return

    path = args[0]

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{path}'")
    text = ""

    f: typing.IO | None = None
    try:
        f = open(path)
        text = f.read()
        print_content(text)

    except (FileNotFoundError, PermissionError) as e:
        print(get_err_msg(path, e))
        return
    finally:
        if f is not None:
            print(f"File '{path}' closed.")
            f.close()

    print("\nTransform data:")

    if text:
        lines = text.splitlines()
        text = "\n".join([line + "#" for line in lines]) + "\n"

    print_content(text)

    new_path = input("Enter new file name (or empty): ")

    if not new_path:
        print("Not saving data.")
        return

    print(f"Saving data to '{new_path}'")

    f = None
    try:
        f = open(new_path, 'w')
        f.write(text)
        print(f"Data saved in file '{new_path}'.")

    except (FileNotFoundError, PermissionError) as e:
        print(get_err_msg(new_path, e))
    finally:
        if f is not None:
            f.close()


if __name__ == "__main__":
    main()
