from typing import List, Tuple
import re
import copy

INPUT_FILE = "input.txt"


def scenic_score_column(grid: List[List[str]], idx: Tuple[int]) -> Tuple[int]:
    column = [row[idx[1]] for row in grid]
    idx_val = column[idx[0]]
    score_down = 0
    score_up = 0
    # Check column down
    column_down = column[idx[0]+1:]
    for val in column_down:
        if val < idx_val:
            score_down += 1
        else:
            score_down += 1
            break
    # Check column up
    column_up = column[:idx[0]]
    column_up.reverse()
    for val in column_up:
        if val < idx_val:
            score_up += 1
        else:
            score_up += 1
            break
    return score_down, score_up


def scenic_score_row(grid: List[List[str]], idx: Tuple[int]) -> Tuple[int]:
    row = grid[idx[0]]
    idx_val = row[idx[1]]
    score_right = 0
    score_left = 0
    # Check row right
    row_right = row[idx[1]+1:]
    for val in row_right:
        if val < idx_val:
            score_right += 1
        else:
            score_right += 1
            break
    # Check row left
    row_left = row[:idx[1]]
    row_left.reverse()
    for val in row_left:
        if val < idx_val:
            score_left += 1
        else:
            score_left += 1
            break
    return score_right, score_left


def get_scenic_score(grid: List[List[str]], idx: Tuple[int]):
    score_down, score_up = scenic_score_column(grid, idx)
    score_right, score_left = scenic_score_row(grid, idx)
    return score_down*score_up*score_right*score_left


def main():
    file = open(INPUT_FILE, "r")
    lines = file.readlines()

    grid = []
    for line in lines:
        parsed_line = re.findall(r"\d", line)
        parsed_line = [int(s) for s in parsed_line]
        grid.append(parsed_line)

    score_grid = copy.deepcopy(grid)
    max_score = 0
    for row_idx in range(0, len(grid)):
        # print(grid[row_idx])
        for col_idx in range(0, len(grid[0])):
            if ((row_idx == 0) or (row_idx == len(grid)-1)
                    or (col_idx == 0) or (col_idx == len(grid[0])-1)):
                # Tree on the edge has zero scenic view
                score_grid[row_idx][col_idx] = 0
            else:
                score_grid[row_idx][col_idx] = get_scenic_score(
                    grid, (row_idx, col_idx)
                )
            # Update max
            if score_grid[row_idx][col_idx] > max_score:
                max_score = score_grid[row_idx][col_idx]

    print(score_grid)
    print(max_score)


if __name__ == "__main__":
    main()
