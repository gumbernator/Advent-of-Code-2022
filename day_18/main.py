from typing import List, Set, Tuple
from itertools import cycle


def part1(lines: List[str]):
    cubes: Set[Tuple[int, int, int]] = set()
    for line in lines:
        splits = line.split(',')
        x, y, z = int(splits[0]), int(splits[1]), int(splits[2])
        cubes.add((x, y, z))

    surface_sides = 0
    for x, y, z in cubes:
        for i in [-1, 1]:
            if (x+i, y, z) not in cubes: surface_sides += 1
            if (x, y+i, z) not in cubes: surface_sides += 1
            if (x, y, z+i) not in cubes: surface_sides += 1

    print('part1:', surface_sides)


def part2(lines: List[str]):
    cubes: Set[Tuple[int, int, int]] = set()
    min_x, min_y, min_z = float('inf'), float('inf'), float('inf')
    max_x, max_y, max_z = float('-inf'), float('-inf'), float('-inf')
    for line in lines:
        splits = line.split(',')
        x, y, z = int(splits[0]), int(splits[1]), int(splits[2])
        cubes.add((x, y, z))
        min_x, min_y, min_z = min(min_x, x), min(min_y, y), min(min_z, z)
        max_x, max_y, max_z = max(max_x, x), max(max_y, y), max(max_z, z)

    min_x, min_y, min_z = min_x - 1, min_y - 1, min_z - 1
    max_x, max_y, max_z = max_x + 1, max_y + 1, max_z + 1

    visitables = [(min_x, min_y, min_z)]
    visited: Set[Tuple[int, int, int]] = set()
    while len(visitables) > 0:
        visited = {*visited, *visitables}
        new_visitables = set()
        for x, y, z in visitables:
            for dx, dy, dz in [(-1, 0, 0), (0, -1, 0), (0, 0, -1), (1, 0, 0), (0, 1, 0), (0, 0, 1)]:
                check_pos = (x+dx, y+dy, z+dz)
                if check_pos[0] < min_x or check_pos[1] < min_y or check_pos[2] < min_z or check_pos[0] > max_x or check_pos[1] > max_y or check_pos[2] > max_z:
                    continue
                if check_pos in cubes:
                    continue
                if check_pos not in visited:
                    new_visitables.add(check_pos)
        visitables = new_visitables

    surface_sides = 0
    for x, y, z in cubes:
        for dx, dy, dz in [(-1, 0, 0), (0, -1, 0), (0, 0, -1), (1, 0, 0), (0, 1, 0), (0, 0, 1)]:
            check_pos = (x+dx, y+dy, z+dz)
            if check_pos in visited: surface_sides += 1

    print('part2:', surface_sides)


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
