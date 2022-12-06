
from typing import List


def part1(lines: List[str]):
    line = lines[0]
    if len(set(line[:4])) == 4:
        print('part1:', 4)
        return
    i = 5
    while i < len(line):
        if len(set(line[i-4:i])) == 4:
            print('part1:', i)
            return
        i += 1


def part2(lines: List[str]):
    line = lines[0]
    if len(set(line[:14])) == 14:
        print('part2:', 14)
        return
    i = 15
    while i < len(line):
        if len(set(line[i-14:i])) == 14:
            print('part2:', i)
            return
        i += 1


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
    # with open('test.txt', 'r') as f:
        lines = f.readlines()
        lines = [line.replace('\n', '') for line in lines]
        part1(lines)
        part2(lines)
