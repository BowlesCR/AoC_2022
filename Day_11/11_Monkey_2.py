import fileinput
import re
from collections import deque
from math import prod


class Monkey:
    def __init__(
        self, items: deque[int], operation: tuple[str, str | int], test: int, target_true: int, target_false: int
    ):
        self.items: deque[items] = items
        self.operation: tuple[str, str | int] = operation
        self.test: int = test
        self.target_true: int = target_true
        self.target_false: int = target_false
        self.inspections: int = 0


class Sim:
    def __init__(self, lines: list[str]):
        self.monkeys: list[Monkey] = []
        self.parse(lines)
        self.divisor = prod([monkey.test for monkey in self.monkeys])

    def parse(self, lines: list[str]):
        r_monkey = re.compile(r"^Monkey (\d+):$")
        r_starting = re.compile(r"^ {2}Starting items: ((?:\d+(?:, )?)*)$")
        r_operation = re.compile(r"^ {2}Operation: new = old ([+-/*]) (\d+|old)$")
        r_test = re.compile(r"^ {2}Test: divisible by (\d+)$")
        r_target = re.compile(r"^ {4}If (true|false): throw to monkey (\d+)$")

        while lines:
            line = lines.pop(0).rstrip()

            m = r_monkey.match(line)
            assert m

            line = lines.pop(0).rstrip()
            m = r_starting.match(line)
            assert m
            starting = deque(int(i) for i in m.group(1).split(", "))

            line = lines.pop(0).rstrip()
            m = r_operation.match(line)
            assert m
            if m.group(2).isnumeric():
                operation = (m.group(1), int(m.group(2)))
            else:
                operation = (m.group(1), m.group(2))

            line = lines.pop(0).rstrip()
            m = r_test.match(line)
            assert m
            test = int(m.group(1))

            line = lines.pop(0).rstrip()
            m = r_target.match(line)
            assert m
            assert m.group(1) == "true"
            target_true = int(m.group(2))

            line = lines.pop(0).rstrip()
            m = r_target.match(line)
            assert m
            assert m.group(1) == "false"
            target_false = int(m.group(2))

            self.monkeys.append(Monkey(starting, operation, test, target_true, target_false))

            if lines:  # eat a blank line if we're not on the last monkey
                line = lines.pop(0).rstrip()
                assert not line

    def run_round(self):
        for i, monkey in enumerate(self.monkeys):
            while monkey.items:
                monkey.inspections += 1
                item = monkey.items.popleft()
                if monkey.operation[1] == "old":
                    val = item
                else:
                    val = monkey.operation[1]

                match monkey.operation[0]:
                    case "+":
                        item += val
                    case "-":
                        item -= val
                    case "*":
                        item *= val
                    case "/":
                        item /= val
                    case _:
                        assert False

                item %= self.divisor

                if item % monkey.test == 0:
                    self.monkeys[monkey.target_true].items.append(item)
                else:
                    self.monkeys[monkey.target_false].items.append(item)


def main():
    sim = Sim(list(fileinput.input()))
    for _ in range(10000):
        sim.run_round()

    print(prod(sorted([monkey.inspections for monkey in sim.monkeys], reverse=True)[:2]))


if __name__ == "__main__":
    main()
