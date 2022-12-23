import re

INPUT_FILE = "input.txt"


def main():
    file = open(INPUT_FILE, "r")
    lines = file.readlines()

    not_contain = 0
    for line in lines:
        expression = re.search(r"(\d+)-(\d+),(\d+)-(\d+)", line)
        intervals = expression.groups()
        subtraction = (
            int(intervals[0])-int(intervals[2]),
            int(intervals[1])-int(intervals[3]),
            int(intervals[1])-int(intervals[2]),
            int(intervals[0])-int(intervals[3])
        )
        positive = sum(n > 0 for n in subtraction)
        negative = sum(n < 0 for n in subtraction)

        if (positive == 4) or (negative == 4):
            not_contain += 1

    print(f"At least partial contained pairs: {len(lines)-not_contain}")


if __name__ == "__main__":
    main()
