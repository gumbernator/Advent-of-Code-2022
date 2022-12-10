
from typing import Dict, List


def part1(lines: List[str]):
    temporal_x = []
    x = 1
    for line in lines:
        if line == 'noop':
            temporal_x.append(x)
            continue
        y = int(line.split(' ')[1])
        temporal_x.append(x)
        temporal_x.append(x)
        x += y

    strength_sum = 0
    for cycle in [20, 60, 100, 140, 180, 220]:
        strength = temporal_x[cycle - 1] * cycle
        strength_sum += strength

    print('part1:', strength_sum)


def part2(lines: List[str]):
    temporal_x = []
    x = 1
    for line in lines:
        if line == 'noop':
            temporal_x.append(x)
            continue
        y = int(line.split(' ')[1])
        temporal_x.append(x)
        temporal_x.append(x)
        x += y

    rows, cols = 6, 40
    crt = ''
    for i in range(rows):
        for j in range(cols):
            cycle = i * cols + j
            sprite_middle = temporal_x[cycle]
            if j in {sprite_middle - 1, sprite_middle, sprite_middle + 1}:
                crt += '#'
            else:
                crt += '.'
        crt += '\n'
    print('part2:', )
    print(crt)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
    # with open('test.txt', 'r') as f:
        lines = f.readlines()
        lines = [line.replace('\n', '') for line in lines]
        part1(lines)
        part2(lines)
