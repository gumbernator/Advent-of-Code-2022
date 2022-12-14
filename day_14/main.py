from typing import List, Tuple


def drop(grid: List[List[str]]):
    x, y = 500, 0
    rested_drops = 0
    while True:
        if grid[y][x] == 'o': break
        if (y + 1) >= len(grid): break
        if grid[y+1][x] == '.':
            y += 1
        else:
            if grid[y+1][x-1] == '.':
                y += 1
                x -= 1
            elif grid[y+1][x+1] == '.':
                y += 1
                x += 1
            else:
                grid[y][x] = 'o'
                x, y = 500, 0
                rested_drops += 1
    return rested_drops


def part1(lines: List[str]):
    grid = []
    for _ in range(200):
        row = []
        for _ in range(1000):
            row.append('.')
        grid.append(row)

    min_x, max_x = float('inf'), float('-inf')

    for line in lines:
        coords = line.split(' -> ')
        old_x, old_y = None, None
        for coord in coords:
            dims = coord.split(',')
            x, y = int(dims[0]), int(dims[1])
            min_x, max_x = min(min_x, x), max(max_x, x)
            if old_x is None:
                old_x, old_y = x, y
                continue
            if old_x == x:
                for i in range(min(y, old_y), max(y, old_y) + 1):
                    grid[i][x] = '#'
                old_x, old_y = x, y
            elif old_y == y:
                for i in range(min(x, old_x), max(x, old_x) + 1):
                    grid[y][i] = '#'
                old_x, old_y = x, y

    drops = drop(grid)

    print('part1:', drops)


def part2(lines: List[str]):
    grid = []
    for _ in range(200):
        row = []
        for _ in range(1000):
            row.append('.')
        grid.append(row)

    max_y = float('-inf')
    for line in lines:
        coords = line.split(' -> ')
        old_x, old_y = None, None
        for coord in coords:
            dims = coord.split(',')
            x, y = int(dims[0]), int(dims[1])
            max_y = max(max_y, y)
            if old_x is None:
                old_x, old_y = x, y
                continue
            if old_x == x:
                for i in range(min(y, old_y), max(y, old_y) + 1):
                    grid[i][x] = '#'
                old_x, old_y = x, y
            elif old_y == y:
                for i in range(min(x, old_x), max(x, old_x) + 1):
                    grid[y][i] = '#'
                old_x, old_y = x, y

    floor_y = max_y + 2
    for i in range(len(grid[0])):
        grid[floor_y][i] = '#'

    drops = drop(grid)

    print('part2:', drops)


if __name__ == '__main__':
    # for fname in {'test.txt'}:
    for fname in {'test.txt', 'input.txt'}:
        print(fname)
        with open(fname, 'r') as f:
            lines = f.readlines()
            lines = [line.replace('\n', '') for line in lines]
            part1(lines)
            part2(lines)
