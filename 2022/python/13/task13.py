from typing import List, Union
import re

INPUT_FILE = "input.txt"


def compare_items(left: Union[List, int], right: Union[List, int]) -> int:
    """Compare two items and return if two items are in a right order.

       1 means right order, 0 wrong order, and -1 can't say.
    """
    if (isinstance(left, int) and isinstance(right, int)):
        if left < right:
            return 1
        elif left > right:
            return 0
        return -1

    elif (isinstance(left, list) and isinstance(right, list)):
        result = -1
        for idx in range(min(len(left), len(right))):
            result = compare_items(left[idx], right[idx])
            if result != -1:
                return result
        if len(left) < len(right):
            return 1
        elif len(left) > len(right):
            return 0
        return -1
    else:
        if isinstance(left, int):
            result = compare_items([left], right)
        else:
            result = compare_items(left, [right])
        return result


def main():
    file = open(INPUT_FILE, "r")
    lines = file.read()

    all_packets = re.findall(r"\[.*\]", lines)
    all_packets = [eval(item) for item in all_packets]

    order = []
    for idx in range(0, len(all_packets)-1, 2):
        left = all_packets[idx]
        right = all_packets[idx+1]
        # print(f"Left packet: {left}")
        # print(f"Right packet: {right}")
        order_pair = compare_items(left, right)
        # print(f"Right order: {right_order_packet}")
        order.append(order_pair)

    sum = 0
    for idx, order_pair in enumerate(order):
        sum += (idx+1) * order_pair
    print(sum)


if __name__ == "__main__":
    main()
