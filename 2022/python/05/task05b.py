from typing import List
import re

INPUT_FILE = "input.txt"


def get_crates(lines: List[str]) -> List[List[str]]:
    # Get number of columns
    for line in lines:
        parsed_line = re.findall(r"\d+", line)
        if parsed_line:
            n_columns = len(parsed_line)
        if line == "\n":
            break
    print(f"N. of columns: {n_columns}")

    # Find the crates
    crates_rows = []
    for line in lines:
        parsed_line = re.findall(r" ?(\[[A-Z]\]| {3})", line)
        if len(parsed_line) == 9:
            crates_rows.append(parsed_line)
        if line == "\n":
            break
    crates_columns = list(zip(*crates_rows))
    # print(crates_columns)

    # Process crates columns
    for idx, col in enumerate(crates_columns):
        new_col_1 = [val for val in col if val.startswith("[")]
        new_col_2 = [val[1] for val in new_col_1]
        crates_columns[idx] = new_col_2
    # print(crates_columns)
    return crates_columns


def parse_instructions(lines: List[str]) -> List[List[int]]:
    # Move X from Y to Z
    instructions = []
    newline_trigger = False
    for line in lines:
        if newline_trigger:
            parsed_line = re.findall(r"\d+", line)
            instructions.append([int(s) for s in parsed_line])
        if line == "\n":
            newline_trigger = True
    return instructions


def main():
    file = open(INPUT_FILE, "r")
    lines = file.readlines()

    crates_columns = get_crates(lines)
    instructions = parse_instructions(lines)
    # print(instructions)

    # Execute instructions on crates
    for instr in instructions:
        print(crates_columns[instr[1]-1])
        print(crates_columns[instr[2]-1])
        # Copy crates into target
        crates_columns[instr[2]-1][:0] = (
            crates_columns[instr[1]-1][0:instr[0]]
        )
        # Delete crates in the origin
        crates_columns[instr[1]-1] = crates_columns[instr[1]-1][instr[0]:]
        print(crates_columns[instr[1]-1])
        print(crates_columns[instr[2]-1])
        print("\n")
    print(crates_columns)
    print([val[0] for val in crates_columns])


if __name__ == "__main__":
    main()
