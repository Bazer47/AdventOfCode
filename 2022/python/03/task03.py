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
    for line in lines:
        first_comp = line[0:(len(line)//2)]
        second_comp = line[(len(line)//2):]
        both_comp_item = [
            item for item in first_comp if item in second_comp
        ][0]
        priority = priorities[both_comp_item]
        priorities_sum += priority

    print(f"Sum of both compartment priorities: {priorities_sum}")


if __name__ == "__main__":
    main()
