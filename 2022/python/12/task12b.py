from typing import List
import string

INPUT_FILE = "input.txt"
ALPHABET = list(string.ascii_lowercase)


class Cell:
    def __init__(self, row_idx: int, col_idx: int, dist: int) -> None:
        self.row_idx = row_idx
        self.col_idx = col_idx
        self.dist = dist

    def __repr__(self) -> str:
        return f"Cell({self.row_idx}, {self.col_idx}, {self.dist})"


def find_min_distance(grid: List[List[str]], start: Cell) -> int:
    """Find minimal distance between start and end in the grid."""

    # Maintain location visit status
    visited = [[False for _ in range(len(grid[0]))]
               for _ in range(len(grid))]

    # Broadth First Search on the grid
    # Init with start cell
    queue = []
    queue.append(start)
    visited[start.row_idx][start.col_idx] = True

    while queue:
        current_cell = queue.pop(0)

        # Destination found
        if (grid[current_cell.row_idx][current_cell.col_idx] == 'E'):
            return current_cell.dist

        # moving up
        if is_valid(
                current_cell.row_idx,
                current_cell.col_idx,
                current_cell.row_idx - 1,
                current_cell.col_idx,
                grid,
                visited):
            queue.append(
                Cell(
                    current_cell.row_idx - 1,
                    current_cell.col_idx,
                    current_cell.dist + 1)
                )
            visited[current_cell.row_idx - 1][current_cell.col_idx] = True

        # moving down
        if is_valid(
                current_cell.row_idx,
                current_cell.col_idx,
                current_cell.row_idx + 1,
                current_cell.col_idx,
                grid,
                visited):
            queue.append(
                Cell(
                    current_cell.row_idx + 1,
                    current_cell.col_idx,
                    current_cell.dist + 1)
                )
            visited[current_cell.row_idx + 1][current_cell.col_idx] = True

        # moving left
        if is_valid(
                current_cell.row_idx,
                current_cell.col_idx,
                current_cell.row_idx,
                current_cell.col_idx - 1,
                grid,
                visited):
            queue.append(
                Cell(
                    current_cell.row_idx,
                    current_cell.col_idx - 1,
                    current_cell.dist + 1)
                )
            visited[current_cell.row_idx][current_cell.col_idx - 1] = True

        # moving right
        if is_valid(
                current_cell.row_idx,
                current_cell.col_idx,
                current_cell.row_idx,
                current_cell.col_idx + 1,
                grid,
                visited):
            queue.append(
                Cell(
                    current_cell.row_idx,
                    current_cell.col_idx + 1,
                    current_cell.dist + 1)
                )
            visited[current_cell.row_idx][current_cell.col_idx + 1] = True

    return -1


def is_valid(old_x: int,
             old_y: int,
             new_x: int,
             new_y: int,
             grid: List[List[str]],
             visited: List[List[bool]]
             ) -> bool:
    """Checking move validity"""
    if ((new_x < 0 or new_y < 0)
            or (new_x >= len(grid) or new_y >= len(grid[0]))):
        # The idxs are outside of the grid
        return False
    if visited[new_x][new_y]:
        # Already visited
        return False

    if grid[new_x][new_y] == "E":
        # Interchange the exit sign and its height
        new_height = "z"
    else:
        new_height = grid[new_x][new_y]

    if (ALPHABET.index(new_height)
            - ALPHABET.index(grid[old_x][old_y]) > 1):
        # Too big jump up
        return False
    return True


def find_all_paths_min(grid: List[List[str]]) -> int:
    """Find all paths minimum distance starting with a."""
    min_dists: List[int] = []
    for row_idx in range(len(grid)):
        for col_idx in range(len(grid[row_idx])):
            if grid[row_idx][col_idx] == 'a':
                start = Cell(row_idx, col_idx, 0)
                min_dist = find_min_distance(grid, start)
                if min_dist >= 0:
                    min_dists.append(min_dist)
    return min(min_dists)


def main():
    file = open(INPUT_FILE, "r")
    lines = file.readlines()

    grid = []
    for idx, line in enumerate(lines):
        line_lst = [char for char in line]
        if idx < (len(lines) - 1):
            line_lst = line_lst[:-1]
        grid.append(line_lst)
    print(grid)

    # Replace S with a
    for row_idx in range(len(grid)):
        for col_idx in range(len(grid[row_idx])):
            if grid[row_idx][col_idx] == "S":
                grid[row_idx][col_idx] = "a"

    print(find_all_paths_min(grid))


if __name__ == "__main__":
    main()
