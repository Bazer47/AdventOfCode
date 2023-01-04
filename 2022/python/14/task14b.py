from typing import List, Tuple
import re

INPUT_FILE = "input.txt"


class SandUnit:
    """Unit of sand in a grid."""

    def __init__(self, pos: List[int]) -> None:
        self.pos = pos  # [x/col, y/row]

    def fall(self,
             grid: List[List[str]]
             ) -> Tuple[bool, List[int]]:
        """Fall sand unit in the grid from the starting point."""
        while True:
            if (grid[self.pos[1] + 1][self.pos[0]]) == ".":
                # Move down
                self.pos[1] += 1
            elif (grid[self.pos[1] + 1][self.pos[0] - 1]) == ".":
                # Move down left
                self.pos[1] += 1
                self.pos[0] += -1
            elif (grid[self.pos[1] + 1][self.pos[0] + 1]) == ".":
                # Move down right
                self.pos[1] += 1
                self.pos[0] += 1
            else:
                # The unit is at rest
                return True, self.pos


def write_line(first: List[int],
               last: List[int],
               grid: List[List[str]]
               ) -> List[List[str]]:
    diff = [last[0]-first[0], last[1]-first[1]]
    if ((diff[0] != 0) and (diff[1] == 0)):
        # Write horizontal line
        if diff[0] > 0:
            # Right
            for x_idx in range(0, diff[0] + 1):
                grid[first[1]][first[0] + x_idx] = "#"
        elif diff[0] < 0:
            # Left
            for x_idx in range(0, diff[0] - 1, -1):
                grid[first[1]][first[0] + x_idx] = "#"
    elif ((diff[0] == 0) and (diff[1] != 0)):
        # Write vertical line
        if diff[1] > 0:
            # Down
            for y_idx in range(0, diff[1] + 1):
                grid[first[1] + y_idx][first[0]] = "#"
        if diff[1] < 0:
            # Up
            for y_idx in range(0, diff[1] - 1, -1):
                grid[first[1] + y_idx][first[0]] = "#"
    else:
        raise ValueError("Difference between two points is in both x and y.")
    return grid


def write_rock_lines(rock_lines: List[List[List[int]]],
                     grid: List[List[str]]
                     ) -> List[List[str]]:
    for line in rock_lines:
        for idx in range(1, len(line)):
            grid = write_line(line[idx-1], line[idx], grid)
    # Create floor
    max_y = 0
    for line in rock_lines:
        for point in line:
            if point[1] > max_y:
                max_y = point[1]
    grid = write_line([0, max_y+2], [len(grid[0])-1, max_y+2], grid)

    return grid


def get_grid(rock_lines: List[List[List[int]]]) -> List[List[str]]:
    # Get max x and max y
    max_x = 0
    max_y = 0
    for line in rock_lines:
        for point in line:
            if point[0] > max_x:
                max_x = point[0]
            if point[1] > max_y:
                max_y = point[1]
    size_x = max_x + 200
    size_y = max_y + 10

    grid = [["."]*size_x for _ in range(size_y)]
    return grid


def main() -> None:
    file = open(INPUT_FILE, "r")
    lines = file.readlines()

    rock_lines = []
    for line in lines:
        parsed_line = re.findall(r"\d+,\d+", line)
        rock_line = [item.split(",") for item in parsed_line]
        rock_line = [[int(x), int(y)] for x, y in rock_line]
        rock_lines.append(rock_line)
    print(rock_lines)
    grid = get_grid(rock_lines)
    for row_idx in range(len(grid)):
        print(grid[row_idx][490:])

    grid = write_rock_lines(rock_lines, grid)
    # print grid
    for row_idx in range(len(grid)):
        print(grid[row_idx][490:])

    # Sand fall
    start_point = [500, 0]
    sand_counter = 0
    while True:
        unit_tmp = SandUnit(start_point.copy())
        rest, pos = unit_tmp.fall(grid)
        sand_counter += 1
        if pos == [500, 0]:
            break
        print(sand_counter)
        grid[pos[1]][pos[0]] = "o"
    print(f"Sand units: {sand_counter}")


if __name__ == "__main__":
    main()
