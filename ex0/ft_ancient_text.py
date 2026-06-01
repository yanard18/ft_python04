#!/usr/bin/env python3

import sys


def get_err_msg(path: str, err: exception) -> str:
    return f"error opening file '{path}': {err}"


def main() -> none:
    script_name = sys.argv[0]
    args = sys.argv[1:]

    if not args or len(args) > 1:
        print(f"usage: {script_name} <file>")
        return

    path = args[0]

    print("=== cyber archives recovery ===")
    print(f"accessing file '{path}'")

    try:
        f = open(path)
        print("---\n")
        print(f.read(), end="")
        print("\n---")
        f.close()
        print(f"file '{path}' closed.")

    except filenotfounderror as e:
        print(get_err_msg(path, e))
    except permissionerror as e:
        print(get_err_msg(path, e))


if __name__ == "__main__":
    main()
