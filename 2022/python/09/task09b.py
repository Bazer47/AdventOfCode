from typing import List, Tuple, Union

INPUT_FILE = "input.txt"


class Head:
    def __init__(self, pos: List[int]) -> None:
        self.pos = pos
        self.pos_history = []
        self.pos_history.append(tuple(self.pos.copy()))

    def __str__(self) -> str:
        return f"Head {self.pos}"

    def __repr__(self) -> str:
        return f"Head({self.pos})"

    def move_one(self, direction: str) -> Tuple[int]:
        if direction == "L":
            self.pos[1] -= 1
        elif direction == "R":
            self.pos[1] += 1
        elif direction == "U":
            self.pos[0] += 1
        elif direction == "D":
            self.pos[0] -= 1
        else:
            raise ValueError(f"Uknown direction value: {direction}")
        self.pos_history.append(tuple(self.pos.copy()))
        return self.pos


class Tail:
    def __init__(self, pos: List[int], head: Union[Head, "Tail"]) -> None:
        self.pos = pos
        self.pos_history = []
        self.pos_history.append(tuple(self.pos.copy()))
        self.head = head

    def __str__(self) -> str:
        return f"Tail {self.pos} with head on {self.head.pos})"

    def __repr__(self) -> str:
        return f"Tail({self.pos}, head on {self.head.pos})"

    def check_difference(self, head: Head) -> Tuple[int]:
        diff_x = head.pos[0] - self.pos[0]
        diff_y = head.pos[1] - self.pos[1]
        return diff_x, diff_y

    def must_move(self) -> bool:
        diff_x, diff_y = self.check_difference(self.head)
        if max((abs(diff_x), abs(diff_y))) <= 1:
            return False
        return True

    def move_one(self) -> Tuple[int]:
        must_move = self.must_move()
        if not must_move:
            raise AssertionError("Cant move!")
        diff_x, diff_y = self.check_difference(self.head)
        if abs(diff_x) > 1:
            if diff_x < 0:
                diff_x += 1
            elif diff_x > 0:
                diff_x -= 1
        if abs(diff_y) > 1:
            if diff_y < 0:
                diff_y += 1
            elif diff_y > 0:
                diff_y -= 1
        self.pos[0] += diff_x
        self.pos[1] += diff_y
        self.pos_history.append(tuple(self.pos.copy()))
        return self.pos


def visualize_path(path: List[Tuple[int]]) -> None:
    x_y_list = list(zip(*path))
    max_x = max(x_y_list[0])
    max_y = max(x_y_list[1])
    min_x = min(x_y_list[0])
    min_y = min(x_y_list[1])
    size_x = abs(max_x) + abs(min_x) + 6  # Some margin
    size_y = abs(max_y) + abs(min_y) + 6  # Some margin

    # Create grid
    grid = [["."]*size_y for _ in range(size_x)]
    # Visualize with #, start in the middle of grid
    for pos in path:
        grid[pos[0] + abs(min_x)][pos[1] + abs(min_y)] = "#"
    grid[path[0][0] + abs(min_x)][path[0][1] + abs(min_y)] = "s"
    grid.reverse()
    for row in grid:
        print(row)


def main():
    file = open(INPUT_FILE, "r")
    lines = file.readlines()

    head = Head([0, 0])
    tails = []
    TAILS_COUNT = 9
    for i in range(TAILS_COUNT):
        if not tails:
            tails.append(Tail([0, 0], head))
        else:
            tails.append(Tail([0, 0], tails[-1]))

    for line in lines:
        instruction = line.split(" ")
        for i in range(int(instruction[1])):
            head.move_one(instruction[0])
            for tail in tails:
                if tail.must_move():
                    tail.move_one()
                else:
                    tail.pos_history.append(tuple(tail.pos.copy()))

    print(f"Visited positions: {len(set(tails[8].pos_history))}")
    # visualize_path(tails[8].pos_history)


if __name__ == "__main__":
    main()
