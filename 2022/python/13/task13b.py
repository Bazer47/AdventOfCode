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


def sort(packets: List) -> List:
    """Sort packets so that all are in the right order."""
    n = len(packets)
    order = [0]*(n-1)
    while True:
        for idx in range(n-1):
            result = compare_items(packets[idx], packets[idx+1])
            if not result:
                packets[idx+1], packets[idx] = packets[idx], packets[idx+1]
            order[idx] = result
        if all(order):
            return packets


def main():
    file = open(INPUT_FILE, "r")
    lines = file.read()

    all_packets = re.findall(r"\[.*\]", lines)
    all_packets = [eval(item) for item in all_packets]

    # Add dividers
    divider_1 = [[2]]
    divider_2 = [[6]]
    all_packets.append(divider_1)
    all_packets.append(divider_2)

    sorted_packets = sort(all_packets)
    # print(sorted_packets)

    idx_divider_1 = sorted_packets.index(divider_1)+1
    idx_divider_2 = sorted_packets.index(divider_2)+1
    print(f"Decoder key: {idx_divider_1*idx_divider_2}")


if __name__ == "__main__":
    main()
