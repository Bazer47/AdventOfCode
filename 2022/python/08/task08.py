from typing import List, Tuple
import re

INPUT_FILE = "input.txt"


def check_column(grid: List[List[str]], idx: Tuple[int]) -> Tuple[bool]:
    column = [row[idx[1]] for row in grid]
    visible_down = True
    visible_up = True
    # Check column down
    if [val for val in column[idx[0]+1:] if val >= column[idx[0]]]:
        visible_down = False
    # Check column up
    if [val for val in column[:idx[0]] if val >= column[idx[0]]]:
        visible_up = False
    return visible_up, visible_down


def check_row(grid: List[List[str]], idx: Tuple[int]):
    row = grid[idx[0]]
    visible_right = True
    visible_left = True
    # Check row right
    if [val for val in row[idx[1]+1:] if val >= row[idx[1]]]:
        visible_right = False
    # Check row left
    if [val for val in row[:idx[1]] if val >= row[idx[1]]]:
        visible_left = False
    return visible_right, visible_left


def check_visibility(grid: List[List[str]], idx: Tuple[int]):
    visibility = []
    visibility.extend(check_column(grid, idx))
    visibility.extend(check_row(grid, idx))
    if any(visibility):
        print(f"Idx: {idx} visible, {visibility}")
        return 1
    print(f"Idx: {idx} not visible, {visibility}")
    return 0


def main():
    file = open(INPUT_FILE, "r")
    lines = file.readlines()

    grid = []
    visible_count = 0
    for line in lines:
        parsed_line = re.findall(r"\d", line)
        parsed_line = [int(s) for s in parsed_line]
        grid.append(parsed_line)

    # Add edges
    visible_count += 2*len(grid[0])
    visible_count += 2*len(grid) - 4  # Subtract corners

    for row_idx in range(1, len(grid)-1):
        for col_idx in range(1, len(grid[0])-1):
            visible_count += check_visibility(grid, (row_idx, col_idx))

    # print(grid)
    print(visible_count)


if __name__ == "__main__":
    main()
