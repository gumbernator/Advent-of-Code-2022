from typing import Dict, List, Set, Tuple
from itertools import cycle


class Monkey:
    def __init__(self, name: str, num: int, operand1: "Monkey", operand2: "Monkey", op: str):
        self.name = name
        self._num = num
        self.operand1 = operand1
        self.operand2 = operand2
        self.op = op

    def get_number(self) -> int:
        if self._num is not None:
            return self._num
        num1 = self.operand1.get_number()
        num2 = self.operand2.get_number()
        if self.op == '+':
            self._num = num1 + num2
        elif self.op == '-':
            self._num = num1 - num2
        elif self.op == '*':
            self._num = num1 * num2
        elif self.op == '/':
            self._num = num1 / num2
        return self._num


def part1(lines: List[str]):
    monkeys: Dict[str, Monkey] = {}
    for line in lines:
        splits = line.split(' ')
        name = splits[0].replace(':', '')
        monkeys[name] = Monkey(name, None, None, None, None)

    for line in lines:
        splits = line.split(' ')
        name = splits[0].replace(':', '')
        if len(splits) == 2:
            monkeys[name]._num = int(splits[1])
            continue
        monkeys[name].operand1 = monkeys[splits[1]]
        monkeys[name].operand2 = monkeys[splits[3]]
        monkeys[name].op = splits[2]

    print('part1:', monkeys['root'].get_number())


def part2(lines: List[str]):
    monkeys: Dict[str, Monkey] = {}
    for line in lines:
        splits = line.split(' ')
        name = splits[0].replace(':', '')
        monkeys[name] = Monkey(name, None, None, None, None)

    for line in lines:
        splits = line.split(' ')
        name = splits[0].replace(':', '')
        if len(splits) == 2:
            monkeys[name]._num = int(splits[1])
            continue
        monkeys[name].operand1 = monkeys[splits[1]]
        monkeys[name].operand2 = monkeys[splits[3]]
        monkeys[name].op = splits[2]

    monkeys['root'].op = '-'
    monkeys['humn']._num = 3412650897405
    res = monkeys['root'].get_number()
    print(res)
    # for _ in range(10):
    #     for name in monkeys:
    #         if monkeys[name].op is not None:
    #             monkeys[name]._num = None
    #     monkeys['humn']._num += 0.1
    #     new_res = monkeys['root'].get_number()
    #     print(new_res - res)
    #     res = new_res

    print('part2:', monkeys['root'].get_number())


if __name__ == '__main__':
    print('test.txt')
    with open('test.txt', 'r') as f:
        lines = f.readlines()
        lines = [line.replace('\n', '') for line in lines]
        part1(lines)
        part2(lines)

    print('input.txt')
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        lines = [line.replace('\n', '') for line in lines]
        part1(lines)
        part2(lines)
