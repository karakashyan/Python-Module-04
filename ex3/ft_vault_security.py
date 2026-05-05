def secure_archive(
        file_name: str, action: int = 0,
        content: str = "") -> tuple[bool, str]:
    try:
        if action == 0:
            with open(file_name, "r") as f:
                data = f.read()
            return (True, data)
        else:
            with open(file_name, "w") as f:
                f.write(content)
            return (True, "Content successfully written to file")
    except OSError as e:
        return (False, f"{e}")


def main() -> None:
    print("=== Cyber Archives Security ===")
    print()

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))
    print()

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd"))
    print()

    print("Using 'secure_archive' to read from a regular file:")
    result = secure_archive("file.txt")
    print(result)
    print()

    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_file.txt", 1, result[1]))


main()
