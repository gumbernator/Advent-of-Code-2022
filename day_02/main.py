
from typing import List


def part1(lines: List[str]):
    selected2score = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }
    result2score = {
        'A X': 3,
        'A Y': 6,
        'A Z': 0,
        'B X': 0,
        'B Y': 3,
        'B Z': 6,
        'C X': 6,
        'C Y': 0,
        'C Z': 3,
    }

    score_sum = sum([result2score[line.replace('\n', '')] + selected2score[line.replace('\n', '').split(' ')[1]] for line in lines])
    print('part1:', score_sum)


def part2(lines: List[str]):
    selected2score = {
        'X': 0,
        'Y': 3,
        'Z': 6
    }
    counter2score = {
        'A X': 3,
        'A Y': 1,
        'A Z': 2,
        'B X': 1,
        'B Y': 2,
        'B Z': 3,
        'C X': 2,
        'C Y': 3,
        'C Z': 1,
    }

    score_sum = sum([counter2score[line.replace('\n', '')] + selected2score[line.replace('\n', '').split(' ')[1]] for line in lines])
    print('part2:', score_sum)

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        input_lines = f.readlines()
        part1(input_lines)
        part2(input_lines)
