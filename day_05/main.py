
from copy import deepcopy
from typing import List


test_stacks = [
    [
        'N',
        'Z'
    ],
    [
        'D',
        'C',
        'M'
    ],
    [
        'P'
    ]
]

input_stacks = [
    [
        'R',
        'Q',
        'G',
        'P',
        'C',
        'F'
    ],
    [
        'P',
        'C',
        'T',
        'W'
    ],
    [
        'C',
        'M',
        'P',
        'H',
        'B'
    ],
    [
        'R',
        'P',
        'M',
        'S',
        'Q',
        'T',
        'L'
    ],
    [
        'N',
        'G',
        'V',
        'Z',
        'J',
        'H',
        'P'
    ],
    [
        'J',
        'P',
        'D'
    ],
    [
        'R',
        'T',
        'J',
        'F',
        'Z',
        'P',
        'G',
        'L'
    ],
    [
        'J',
        'T',
        'P',
        'F',
        'C',
        'H',
        'L',
        'N'
    ],
    [
        'W',
        'C',
        'T',
        'H',
        'Q',
        'Z',
        'V',
        'G'
    ]
]


def part1(lines: List[str], stacks: List[List[str]]):
    for line in lines:
        splits = line.split(' ')
        quantity = int(splits[1])
        from_idx = int(splits[3]) - 1
        to_idx = int(splits[5]) - 1
        # print(quantity, from_idx, to_idx)
        # print(stacks)
        for _ in range(quantity):
            stacks[to_idx].insert(0, stacks[from_idx][0])
            del stacks[from_idx][0]
        # print(stacks)
    res = ''.join([stack[0] for stack in stacks])
    print('part1:', res)


def part2(lines: List[str], stacks: List[List[str]]):
    for line in lines:
        splits = line.split(' ')
        quantity = int(splits[1])
        from_idx = int(splits[3]) - 1
        to_idx = int(splits[5]) - 1
        # print(quantity, from_idx, to_idx)
        # print(stacks)
        stacks[to_idx][:0] = stacks[from_idx][:quantity]
        del stacks[from_idx][:quantity]
        # print(stacks)
    res = ''.join([stack[0] for stack in stacks])
    print('part2:', res)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        lines = [line.replace('\n', '') for line in lines]
        part1(lines, deepcopy(input_stacks))
        part2(lines, deepcopy(input_stacks))
