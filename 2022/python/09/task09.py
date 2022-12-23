from typing import List, Tuple

INPUT_FILE = "input.txt"


class Head:
    def __init__(self, pos: List[int]) -> None:
        self.pos = pos
        self.pos_history = []
        self.pos_history.append(tuple(self.pos.copy()))

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
    def __init__(self, pos: List[int]) -> None:
        self.pos = pos
        self.pos_history = []
        self.pos_history.append(tuple(self.pos.copy()))

    def check_difference(self, head: Head) -> Tuple[int]:
        diff_x = head.pos[0] - self.pos[0]
        diff_y = head.pos[1] - self.pos[1]
        return diff_x, diff_y

    def must_move(self, head: Head) -> bool:
        diff_x, diff_y = self.check_difference(head)
        if max((abs(diff_x), abs(diff_y))) <= 1:
            return False
        return True

    def move_one(self, head: Head) -> Tuple[int]:
        must_move = self.must_move(head)
        if not must_move:
            raise AssertionError("Cant move!")
        diff_x, diff_y = self.check_difference(head)
        if abs(diff_x) == 2:
            if diff_x < 0:
                diff_x += 1
            elif diff_x > 0:
                diff_x -= 1
        elif abs(diff_y) == 2:
            if diff_y < 0:
                diff_y += 1
            elif diff_y > 0:
                diff_y -= 1
        self.pos[0] += diff_x
        self.pos[1] += diff_y
        self.pos_history.append(tuple(self.pos.copy()))
        return self.pos


def main():
    file = open(INPUT_FILE, "r")
    lines = file.readlines()

    head = Head([0, 0])
    tail = Tail([0, 0])

    for line in lines:
        instruction = line.split(" ")
        for i in range(int(instruction[1])):
            head.move_one(instruction[0])
            if tail.must_move(head):
                tail.move_one(head)
    print(head.pos_history)
    print(tail.pos_history)

    print(f"Visited positions: {len(set(tail.pos_history))}")


if __name__ == "__main__":
    main()
