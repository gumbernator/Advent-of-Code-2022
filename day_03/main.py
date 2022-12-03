
from typing import List


def chart2priority(c: str):
    if c.islower():
        return ord(c) - 96
    return ord(c) - 38


def part1(lines: List[str]):
    priority_sum = 0
    for line in lines:
        compartment_size = len(line) / 2
        first_half_set, second_half_set = set(), set()
        for i, c in enumerate(line):
            if i <compartment_size:
                first_half_set.add(c)
            else:
                second_half_set.add(c)
        common_char = first_half_set.intersection(second_half_set)
        common_char = list(common_char)[0]
        priority_sum += chart2priority(common_char)
    print('part1:', priority_sum)


def part2(lines: List[str]):
    i = 0
    priority_sum = 0
    while i < len(lines):
        first_set = {c for c in lines[i]}
        second_set = {c for c in lines[i+1]}
        third_set = {c for c in lines[i+2]}
        common_char = set.intersection(first_set, second_set, third_set)
        common_char = list(common_char)[0]
        priority_sum += chart2priority(common_char)
        i += 3
    print('part2:', priority_sum)

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        lines = [line.replace('\n', '') for line in lines]
        part1(lines)
        part2(lines)
