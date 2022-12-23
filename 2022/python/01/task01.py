
INPUT_FILE = "input.txt"


def main():
    file = open(INPUT_FILE, "rb")
    lines = file.readlines()

    elfs = []
    count = 0
    for line in lines:
        if line != b"\n":
            count += int(line)
        else:
            elfs.append(count)
            count = 0

    print(f"max: {max(elfs)}")

    # Find top three elves
    elfs.sort()
    print(elfs)
    print(f"Top three sum {elfs[-1] + elfs[-2] + elfs[-3]}")


if __name__ == "__main__":
    main()
