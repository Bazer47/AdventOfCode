from typing import List

INPUT_FILE = "input.txt"
WINDOW_SIZE = 14


def check_window(window: List[str]) -> bool:
    if len(set(window)) == len(window):
        return True
    return False


def main():
    file = open(INPUT_FILE, "r")
    lines = file.readlines()
    line = lines[0]

    for idx in range(0, len(line)-WINDOW_SIZE+1):
        start = check_window(line[idx:idx+WINDOW_SIZE])
        if start:
            first_marker = idx+WINDOW_SIZE
            first_marker_window = line[idx:idx+WINDOW_SIZE]
            break

    print(first_marker)
    print(first_marker_window)


if __name__ == "__main__":
    main()
