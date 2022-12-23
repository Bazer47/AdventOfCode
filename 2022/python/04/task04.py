import re

INPUT_FILE = "input.txt"


def main():
    file = open(INPUT_FILE, "r")
    lines = file.readlines()

    fully_contain = 0
    for line in lines:
        expression = re.search(r"(\d+)-(\d+),(\d+)-(\d+)", line)
        intervals = expression.groups()
        subtraction = (
            int(intervals[0])-int(intervals[2]),
            int(intervals[1])-int(intervals[3]),
            int(intervals[1])-int(intervals[2]),
            int(intervals[0])-int(intervals[3])
        )
        nonnegative = sum(n >= 0 for n in subtraction)
        zeros = sum(n == 0 for n in subtraction)

        if nonnegative == 2:
            fully_contain += 1
        elif (nonnegative == 3) and (0 in subtraction):
            fully_contain += 1
        elif (nonnegative == 4) and (zeros == 2):
            fully_contain += 1

    print(f"Fully contained pairs: {fully_contain}")


if __name__ == "__main__":
    main()
