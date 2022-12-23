import string

INPUT_FILE = "input.txt"


def main():
    file = open(INPUT_FILE, "r")
    lines = file.readlines()

    letters = string.ascii_lowercase + string.ascii_uppercase
    priorities = {
        key: val for key, val in zip(letters, list(range(1, len(letters) + 1)))
    }

    priorities_sum = 0
    group = []
    for line in lines:
        group.append(line)
        if len(group) == 3:
            intersection = set(group[0]) & set(group[1]) & set(group[2])
            intersection.remove("\n")
            if len(intersection) > 1:
                raise ValueError(
                    f"Intersection has more than 1 value: {intersection}"
                )
            priorities_sum += priorities[list(intersection)[0]]
            group = []

    print(f"Sum of intersection priorities: {priorities_sum}")


if __name__ == "__main__":
    main()
