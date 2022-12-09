
from typing import Dict, List


class Knot:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def move(self, direction: str):
        if direction == 'U':
            self.y += 1
        elif direction == 'D':
            self.y -= 1
        elif direction == 'R':
            self.x += 1
        elif direction == 'L':
            self.x -= 1

    def follow(self, point: "Knot"):
        xdiff = point.x - self.x
        ydiff = point.y - self.y
        if abs(xdiff) < 2 and abs(ydiff) < 2:
            return
        if abs(xdiff) == 2 and abs(ydiff) == 2:
            self.x += xdiff / 2
            self.y += ydiff / 2
            return
        if abs(xdiff) == 2:
            self.x += xdiff / 2
            if ydiff == 0:
                return
            self.y += ydiff
        if abs(ydiff) == 2:
            self.y += ydiff / 2
            if xdiff == 0:
                return
            self.x += xdiff


def part1(lines: List[str]):
    H, T = Knot(0, 0), Knot(0, 0)
    T_visits = set()
    for line in lines:
        splits = line.split(' ')
        direction, count = splits[0], int(splits[1])
        for _ in range(count):
            H.move(direction)
            T.follow(H)
            T_visits.add((T.x, T.y))
    print('part1:', len(T_visits))


def part2(lines: List[str]):
    knots = [Knot(0, 0) for _ in range(10)]
    knot_9_visits = set()
    for line in lines:
        splits = line.split(' ')
        direction, count = splits[0], int(splits[1])
        for _ in range(count):
            knots[0].move(direction)
            for i in range(1, 10):
                knots[i].follow(knots[i-1])
            knot_9_visits.add((knots[9].x, knots[9].y))
    print(f'part2:', len(knot_9_visits))


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
    # with open('part1_test.txt', 'r') as f:
    # with open('part2_test.txt', 'r') as f:
        lines = f.readlines()
        lines = [line.replace('\n', '') for line in lines]
        part1(lines)
        part2(lines)
