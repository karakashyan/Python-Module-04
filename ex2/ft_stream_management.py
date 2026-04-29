import sys


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
        return

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{sys.argv[1]}'")
    try:
        f = open(sys.argv[1], "r")
        content = f.read()
        print("---")
        print()
        print(content)
        print()
        print("---")
        f.close()
        print(f"File '{sys.argv[1]}' closed.")
        print()
        print("Transform data:")
        print("---")
        print()
        lines = [line + "#" for line in content.split("\n")]
        for line in lines:
            print(line)
        print()
        print("---")
        sys.stdout.write("Enter new file name (or empty): ")
        sys.stdout.flush()
        file_name = sys.stdin.readline().rstrip("\n")
        if file_name == "":
            print("Not saving data.")
        else:
            print(f"Saving data to '{file_name}'")
            g = open(file_name, "w")
            g.write("\n".join(lines))
            g.close()
            print(f"Data saved in file '{file_name}'.")
    except OSError as e:
        sys.stderr.write(f"[STDERR] Error opening file '{sys.argv[1]}': {e}")


main()
