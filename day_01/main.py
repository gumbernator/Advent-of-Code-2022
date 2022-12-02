
from typing import List


def part1(lines: List[str]):
    max_calories = float('-inf')
    current_sum = 0
    for line in lines:
        if line != '\n':
            current_sum += int(line)
        else:
            max_calories = max(max_calories, current_sum)
            current_sum = 0
    print('part1:', max_calories)

def part2(lines: List[str]):
    elf_calories = []
    current_sum = 0
    for line in lines:
        if line != '\n':
            current_sum += int(line)
        else:
            elf_calories.append(current_sum)
            current_sum = 0
    top3sum = sum(sorted(elf_calories, reverse=True)[:3])
    print('part2:', top3sum)

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        input_lines = f.readlines()
        part1(input_lines)
        part2(input_lines)
