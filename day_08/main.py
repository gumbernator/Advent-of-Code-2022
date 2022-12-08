
from typing import Dict, List


def part1(lines: List[str]):
    grid = []
    for line in lines:
        row = [int(c) for c in line]
        grid.append(row)

    visibles = set()
    # Look from top
    top_max_heights = [-1 for _ in range(len(grid[0]))]
    for i, row in enumerate(grid):
        for j, h in enumerate(row):
            if top_max_heights[j] < h:
                visibles.add((i, j))
                top_max_heights[j] = h
    # Look from bottom
    bottom_max_heights = [-1 for _ in range(len(grid[0]))]
    for i in range(len(grid) - 1, -1, -1):
        row = grid[i]
        for j, h in enumerate(row):
            if bottom_max_heights[j] < h:
                visibles.add((i, j))
                bottom_max_heights[j] = h
    # Look from left
    left_max_heights = [-1 for _ in range(len(grid))]
    for j in range(len(grid[0])):
        for i in range(len(grid)):
            if left_max_heights[i] < grid[i][j]:
                visibles.add((i, j))
                left_max_heights[i] = grid[i][j]
    # Look from right
    right_max_heights = [-1 for _ in range(len(grid))]
    for j in range(len(grid[0]) - 1, -1, -1):
        for i in range(len(grid)):
            if right_max_heights[i] < grid[i][j]:
                visibles.add((i, j))
                right_max_heights[i] = grid[i][j]

    interior_visibles_count = 0
    edge_visibles_count = 0
    for visible in visibles:
        if visible[0] != 0 and visible[0] != len(grid) - 1 and visible[1] != 0 and visible[1] != len(grid[0]) - 1:
            interior_visibles_count += 1
        else:
            edge_visibles_count += 1
    print(f'part1: {interior_visibles_count} + {edge_visibles_count} = {len(visibles)}')


def part2(lines: List[str]):
    grid = []
    for line in lines:
        row = [int(c) for c in line]
        grid.append(row)

    def score(posx: int, posy: int, grid: List[List[int]]) -> int:
        top, right, bottom, left = 0, 0, 0, 0
        height = grid[posx][posy]
        topx = posx - 1
        while topx >= 0:
            top += 1
            if grid[topx][posy] >= height:
                break
            topx -= 1
        bottomx = posx + 1
        while bottomx < len(grid):
            bottom += 1
            if grid[bottomx][posy] >= height:
                break
            bottomx += 1
        righty = posy + 1
        while righty < len(grid[0]):
            right += 1
            if grid[posx][righty] >= height:
                break
            righty += 1
        lefty = posy - 1
        while lefty >= 0:
            left += 1
            if grid[posx][lefty] >= height:
                break
            lefty -= 1
        return top * right * bottom * left

    max_score = -1
    for i in range(1, len(grid)):
        for j in range(1, len(grid[0])):
            max_score = max(max_score, score(i, j, grid))
    print('part2:', max_score)

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
    # with open('test.txt', 'r') as f:
        lines = f.readlines()
        lines = [line.replace('\n', '') for line in lines]
        part1(lines)
        part2(lines)
