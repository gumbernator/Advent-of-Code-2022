from dijkstar import Graph, find_path
from typing import List, Tuple


def can_go(frm: str, to: str) -> bool:
    return (ord(to) - ord(frm)) <= 1


def part1(lines: List[str]):
    grid = []
    for line in lines:
        grid.append([c for c in line])

    rows = len(grid)
    cols = len(grid[0])
    start_pos, end_pos = None, None

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'E':
                end_pos = (i, j)
                grid[i][j] = 'z'
            elif grid[i][j] == 'S':
                start_pos = (i, j)
                grid[i][j] = 'a'

    graph = Graph()
    for i in range(rows):
        for j in range(cols):
            if i > 0 and can_go(grid[i][j], grid[i-1][j]):
                graph.add_edge((i, j), (i-1, j), 1)
            if i < (rows - 1) and can_go(grid[i][j], grid[i+1][j]):
                graph.add_edge((i, j), (i+1, j), 1)
            if j > 0 and can_go(grid[i][j], grid[i][j-1]):
                graph.add_edge((i, j), (i, j-1), 1)
            if j < (cols - 1) and can_go(grid[i][j], grid[i][j+1]):
                graph.add_edge((i, j), (i, j+1), 1)

    total_cost = find_path(graph, start_pos, end_pos).total_cost

    print('part1:', total_cost)


def part2(lines: List[str]):
    grid = []
    for line in lines:
        grid.append([c for c in line])

    rows = len(grid)
    cols = len(grid[0])
    start_positions, end_pos = [], None

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'E':
                end_pos = (i, j)
                grid[i][j] = 'z'
            elif grid[i][j] in {'S', 'a'}:
                start_positions.append((i, j))
                grid[i][j] = 'a'

    graph = Graph()
    for i in range(rows):
        for j in range(cols):
            if i > 0 and can_go(grid[i][j], grid[i-1][j]):
                graph.add_edge((i, j), (i-1, j), 1)
            if i < (rows - 1) and can_go(grid[i][j], grid[i+1][j]):
                graph.add_edge((i, j), (i+1, j), 1)
            if j > 0 and can_go(grid[i][j], grid[i][j-1]):
                graph.add_edge((i, j), (i, j-1), 1)
            if j < (cols - 1) and can_go(grid[i][j], grid[i][j+1]):
                graph.add_edge((i, j), (i, j+1), 1)

    total_costs = []
    for start_pos in start_positions:
        try:
            total_cost = find_path(graph, start_pos, end_pos).total_cost
            total_costs.append(total_cost)
        except:
            pass

    print('part2:', min(total_costs))


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
    # with open('test.txt', 'r') as f:
        lines = f.readlines()
        lines = [line.replace('\n', '') for line in lines]
        part1(lines)
        part2(lines)
