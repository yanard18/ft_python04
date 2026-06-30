#!/usr/bin/env python3

import sys
import typing


def get_err_msg(path: str, err: Exception) -> str:
    return f"error opening file '{path}': {err}"


def main() -> None:
    script_name = sys.argv[0]
    args = sys.argv[1:]

    if not args or len(args) > 1:
        print(f"usage: {script_name} <file>")
        return

    path = args[0]

    print("=== cyber archives recovery ===")
    print(f"accessing file '{path}'")

    f: typing.IO | None = None
    try:
        f = open(path)
        print("---\n")
        print(f.read(), end="")
        print("\n---")

    except OSError as e:
        print(get_err_msg(path, e))
    finally:
        if f is not None:
            print(f"file '{path}' closed.")
            f.close()


if __name__ == "__main__":
    main()
