#!/usr/bin/env python3

def secure_archive(file: str, mode: str, out: str = "") -> tuple[bool, str]:
    try:
        with open(file, mode) as f:
            if mode == 'r':
                return (True, f.read())
            elif mode == 'w':
                f.write(out)
                return (True, "Content successfully written to file")

    except OSError as e:
        return (False, f"{e}")

    return (True, 't')


def main() -> None:
    print("=== Cyber Archives Security ===\n")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive('/non/existing/file', 'r'), end="\n\n")

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive('/etc/shadow', 'r'), end="\n\n")

    print("Using 'secure_archive' to read from a regular file:")
    content = secure_archive('ancient_fragment.txt', 'r')
    print(content, end="\n\n")

    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive('out.txt', 'w', content[1]))


if __name__ == "__main__":
    main()
