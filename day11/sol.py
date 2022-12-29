from functools import reduce
import operator
import re
from typing import Callable, Iterable, List


def product(it: Iterable):
    return reduce(operator.mul, it, 1)


class Monkey:
    def __init__(
        self,
        items: Iterable[int],
        operation: Callable[[int], int],
        test: int,
        true_monkey: "Monkey",
        false_monkey: "Monkey",
    ):
        self.items = list(items)
        self.operation = operation
        self.test = test
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey

        self.inspect_count = 0

    def inspect_item(self, item: int, worry_fun: Callable[[int], int]):
        worry = self.operation(item)
        worry = worry_fun(worry)

        if worry % self.test == 0:
            self.true_monkey.throw(worry)
        else:
            self.false_monkey.throw(worry)

        self.inspect_count += 1

    def inspect_all_items(self, worry_fun):
        for item in self.items:
            self.inspect_item(item, worry_fun)
        self.items = []

    def throw(self, item: int):
        self.items.append(item)


def parse_starting(match) -> Iterable[int]:
    return [int(i.strip(",")) for i in match.group(1).split()]


def parse_operation(match) -> Callable[[int], int]:
    op_mapping = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.floordiv,
    }
    var1, op, var2 = match.group(1).split()

    if var1 == "old" and var2 == "old":
        return lambda old: op_mapping[op](old, old)

    if var1 == "old":
        return lambda old: op_mapping[op](old, int(var2))

    if var2 == "old":
        return lambda old: op_mapping[op](int(var1), old)

    return lambda _: op_mapping[op](int(var1), int(var2))


def parse_int(match) -> int:
    return int(match.group(1))


def parse_lines(lines: Iterable[str]) -> List[Monkey]:
    monkey_dicts = {}
    current = None

    matches = (
        ("items", parse_starting, r"Starting items: ((\d+, )*\d+)"),
        ("operation", parse_operation, r"Operation: new = (.*)"),
        ("test", parse_int, r"Test: divisible by (\d+)"),
        ("true_monkey", parse_int, r"If true: throw to monkey (\d+)"),
        ("false_monkey", parse_int, r"If false: throw to monkey (\d+)"),
    )

    for line in lines:
        monkey_match = re.search(r"Monkey (\d+)", line)
        if monkey_match:
            current = int(monkey_match.group(1))
            monkey_dicts[current] = {}
            continue
        for key, func, pattern in matches:
            match = re.search(pattern, line)
            if match:
                monkey_dicts[current][key] = func(match)
                break

    monkeys = {key: Monkey(**params) for key, params in monkey_dicts.items()}
    monkey_list = list(monkeys.values())
    for monkey in monkey_list:
        monkey.true_monkey = monkeys[monkey.true_monkey]
        monkey.false_monkey = monkeys[monkey.false_monkey]

    return monkey_list


def calculate_monkey_business(monkeys: Iterable[Monkey]):
    inspect_counts = [m.inspect_count for m in monkeys]
    inspect_counts.sort(reverse=True)
    return inspect_counts[0] * inspect_counts[1]


def main(input_path="input"):
    with open(input_path) as f:
        lines = f.read().splitlines()

    monkeys = parse_lines(lines)

    for _ in range(20):
        for monkey in monkeys:
            monkey.inspect_all_items(lambda w: w // 3)

    part1 = calculate_monkey_business(monkeys)

    monkeys = parse_lines(lines)

    def worry_fun(w):
        return w % product(m.test for m in monkeys)

    for i in range(10000):
        for monkey in monkeys:
            monkey.inspect_all_items(worry_fun)

    part2 = calculate_monkey_business(monkeys)

    return part1, part2


if __name__ == '__main__':
    print(main())
