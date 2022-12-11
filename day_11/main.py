from copy import deepcopy
from typing import List, Tuple


class Item:
    def __init__(self, worry: int, divisors: List[int]):
        self.worry = worry
        self.mods = {
            divisor: worry % divisor
            for divisor in divisors
        }

    def divide_by_3(self):
        self.worry = int(self.worry / 3)
        self.mods = {
            divisor: self.worry % divisor
            for divisor in self.mods
        }

    def add(self, num: int, modify_worry: bool):
        if modify_worry: self.worry += num
        self.mods = {
            divisor: (mod + num % divisor) % divisor
            for divisor, mod in self.mods.items()
        }

    def multiply(self, num: int, modify_worry: bool):
        if modify_worry: self.worry *= num
        self.mods = {
            divisor: (mod * (num % divisor)) % divisor
            for divisor, mod in self.mods.items()
        }

    def square(self, modify_worry: bool):
        if modify_worry: self.worry = self.worry ** 2
        self.mods = {
            divisor: (mod * mod) % divisor
            for divisor, mod in self.mods.items()
        }


class Monkey:
    def __init__(self, items: List[Item], operation: Tuple[str, int], divisor: int, divided_idx: int, non_divided_idx: int):
        self.items = items
        self.op, self.op_num = operation
        self.divisor = divisor
        self.divided_idx = divided_idx
        self.non_divided_idx = non_divided_idx
        self.total_inspected_items = 0

    def inspect(self, all_monkeys: List["Monkey"], divide_by_3: bool):
        for item in self.items:
            if self.op == 'add':
                item.add(self.op_num, modify_worry=divide_by_3)
            elif self.op == 'multiply':
                item.multiply(self.op_num, modify_worry=divide_by_3)
            elif self.op == 'square':
                item.square(modify_worry=divide_by_3)

            if divide_by_3: item.divide_by_3()

            if item.mods[self.divisor] == 0:
                all_monkeys[self.divided_idx].items.append(item)
            else:
                all_monkeys[self.non_divided_idx].items.append(item)

            self.total_inspected_items += 1
        self.items = []


def part1(monkeys: List[Monkey]):
    for _ in range(20):
        for monkey in monkeys:
            monkey.inspect(monkeys, divide_by_3=True)

    total_inspected_items = [monkey.total_inspected_items for monkey in monkeys]
    total_inspected_items.sort(reverse=True)
    monkey_business = total_inspected_items[0] * total_inspected_items[1]
    print('part1:', monkey_business)


def part2(monkeys: List[Monkey]):
    for _ in range(10_000):
        for monkey in monkeys:
            monkey.inspect(monkeys, divide_by_3=False)

    total_inspected_items = [monkey.total_inspected_items for monkey in monkeys]
    print(total_inspected_items)
    total_inspected_items.sort(reverse=True)
    monkey_business = total_inspected_items[0] * total_inspected_items[1]
    print('part2:', monkey_business)


if __name__ == '__main__':
    test_divisors = [23, 19, 13, 17]
    test_monkeys = [
        Monkey([Item(num, test_divisors) for num in [79, 98]], ('multiply', 19), 23, 2, 3),
        Monkey([Item(num, test_divisors) for num in [54, 65, 75, 74]], ('add', 6), 19, 2, 0),
        Monkey([Item(num, test_divisors) for num in [79, 60, 97]], ('square', ...), 13, 1, 3),
        Monkey([Item(num, test_divisors) for num in [74]], ('add', 3), 17, 0, 1)
    ]

    input_divisors = [2, 17, 7, 11, 19, 5, 13, 3]
    input_monkeys = [
        Monkey([Item(num, input_divisors) for num in [99, 63, 76, 93, 54, 73]], ('multiply', 11), 2, 7, 1),
        Monkey([Item(num, input_divisors) for num in [91, 60, 97, 54]], ('add', 1), 17, 3, 2),
        Monkey([Item(num, input_divisors) for num in [65]], ('add', 7), 7, 6, 5),
        Monkey([Item(num, input_divisors) for num in [84, 55]], ('add', 3), 11, 2, 6),
        Monkey([Item(num, input_divisors) for num in [86, 63, 79, 54, 83]], ('square', ...), 19, 7, 0),
        Monkey([Item(num, input_divisors) for num in [96, 67, 56, 95, 64, 69, 96]], ('add', 4), 5, 4, 0),
        Monkey([Item(num, input_divisors) for num in [66, 94, 70, 93, 72, 67, 88, 51]], ('multiply', 5), 13, 4, 5),
        Monkey([Item(num, input_divisors) for num in [59, 59, 74]], ('add', 8), 3, 1, 3),
    ]

    # with open('input.txt', 'r') as f:
    # with open('test.txt', 'r') as f:
        # lines = f.readlines()
        # lines = [line.replace('\n', '') for line in lines]
    part1(deepcopy(input_monkeys))
    part2(deepcopy(input_monkeys))
