from typing import List, Dict, Tuple
import re

INPUT_FILE = "input.txt"


class Monkey:
    _counter = 0

    def __init__(self,
                 items: List[int],
                 operation_expr: str,
                 test_val: int,
                 target_true: int,
                 target_false: int
                 ) -> None:

        self.id = Monkey._counter
        Monkey._counter += 1
        self.items = items
        self.operation_expr = operation_expr
        self.test_val = test_val
        self.target_true = target_true
        self.target_false = target_false
        self.insp_items_count = 0

    def __str__(self) -> str:
        return f"Monkey {self.id}:\n items: {self.items}\n operation: new = "\
               f"{self.operation_expr}\n test_val: {self.test_val}\n  "\
               f"If true: target {self.target_true}\n  If false: target "\
               f"{self.target_false}\n inspected items: "\
               f"{self.insp_items_count}"

    def inspect_item(self, item: int) -> Tuple[int]:
        self.insp_items_count += 1
        old = item  # var old is in the expr
        new = eval(self.operation_expr)
        # Least common multiplier of all test_val from all monkeys
        new = new % 9699690
        if (new % self.test_val) == 0:
            return new, self.target_true
        return new, self.target_false

    def throw_item(self, item: int, monkey: 'Monkey') -> None:
        monkey.items.append(item)

    def inspect_items(self, other_monkeys: Dict[int, 'Monkey']) -> None:
        for item in self.items:
            new_item, idx_target = self.inspect_item(item)
            self.throw_item(new_item, other_monkeys[idx_target])
        # Empty the items after turn
        self.items = []


def main():
    file = open(INPUT_FILE, "r")
    file_str = file.read()

    groups = re.findall(
        "Monkey (\d):\n  Starting items: (.+)\n  Operation: new = (.+)\n  "
        "Test: divisible by (\d+)\n    If true: throw to monkey (\d+)\n    "
        "If false: throw to monkey (\d+)",
        file_str
    )
    print(groups)

    monkeys = {}
    for group in groups:
        items_parsed = group[1].split(", ")
        items_parsed = [int(i) for i in items_parsed]
        monkeys[int(group[0])] = Monkey(
            items=items_parsed,
            operation_expr=group[2],
            test_val=int(group[3]),
            target_true=int(group[4]),
            target_false=int(group[5])
        )

    for key, val in monkeys.items():
        print(val)

    # Play
    rounds = []
    for idx_round in range(1, 10001):
        for idx, monkey in monkeys.items():
            monkey.inspect_items(other_monkeys=monkeys)
        print(idx_round)
        current_state = {key: val.items for key, val in monkeys.items()}
        rounds.append((idx_round, current_state))

    print(rounds)

    # See inspected items and monkey business
    inspected_items = []
    for key, val in monkeys.items():
        print(val)
        inspected_items.append(val.insp_items_count)
    inspected_items.sort()
    print(f"Monkey business: {inspected_items[-1]*inspected_items[-2]}")


if __name__ == "__main__":
    main()
