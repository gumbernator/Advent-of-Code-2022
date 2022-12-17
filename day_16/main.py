from typing import Dict, List, Set, Tuple
from copy import deepcopy
from dijkstar import Graph, find_path


class Valve:
    def __init__(self, label: str, flow_rate: int, tunnels: List[str]):
        self.label = label
        self.flow_rate = flow_rate
        self.tunnels = tunnels

    def __repr__(self):
        return f'{self.label} {self.flow_rate} {self.tunnels}'


def traverse_alone(
    label: str,
    minute: int,
    closed_valves: Set[str],
    total_pressure: int,
    valves: Dict[str, Valve],
    max_pressure: List[int],
    path_nodes: Dict[Tuple[str, str], int]
    ):
    if minute >= 30 or len(closed_valves) == 0:
        max_pressure[0] = max(max_pressure[0], total_pressure)
        return

    for closed_valve in closed_valves:
        new_closed_valves = closed_valves.copy()
        new_closed_valves.remove(closed_valve)
        passed_minutes = path_nodes[(label, closed_valve)]
        released_pressure = (30 - minute - passed_minutes) * valves[closed_valve].flow_rate
        if released_pressure <= 0:
            max_pressure[0] = max(max_pressure[0], total_pressure)
            continue
        traverse_alone(closed_valve, minute + passed_minutes, new_closed_valves, total_pressure + released_pressure, valves, max_pressure, path_nodes)


def traverse_with_elephant(
    label_one: str,
    label_two: str,
    minute: int,
    open_valves: List[str],
    closed_valves: List[str],
    total_pressure: int,
    valves: Dict[str, Valve],
    max_pressure: List[int],
    path_nodes: Dict[Tuple[str, str], List[str]]
    ):
    pass


def part1(lines: List[str]):
    valves: Dict[str, Valve] = {}
    for line in lines:
        splits = line.replace(',', '').split(' ')
        label = splits[1]
        flow_rate = int(splits[4].replace('rate=', '').replace(';', ''))
        tunnels = splits[9:]
        valves[label] = Valve(label, flow_rate, tunnels)

    graph = Graph()
    for label, valve in valves.items():
        for tunnel_label in valve.tunnels:
            graph.add_edge(label, tunnel_label, 1)

    path_nodes: Dict[Tuple[str, str], int] = {}
    for label in valves.keys():
        for _label in valves.keys():
            if label != _label:
                path_nodes[(label, _label)] = len(find_path(graph, label, _label).nodes)

    closed_valves = {label for label, valve in valves.items() if valve.flow_rate != 0}

    max_pressure = [0]
    traverse_alone('AA', 0, closed_valves, 0, valves, max_pressure, path_nodes)

    print('part1:', max_pressure[0])


def part2(lines: List[str]):
    valves: Dict[str, Valve] = {}
    for line in lines:
        splits = line.replace(',', '').split(' ')
        label = splits[1]
        flow_rate = int(splits[4].replace('rate=', '').replace(';', ''))
        tunnels = splits[9:]
        valves[label] = Valve(label, flow_rate, tunnels)

    graph = Graph()
    for label, valve in valves.items():
        for tunnel_label in valve.tunnels:
            graph.add_edge(label, tunnel_label, 1)

    path_nodes: Dict[Tuple[str, str], int] = {}
    for label in valves.keys():
        path_nodes[(label, label)] = [label]
        for _label in valves.keys():
            if label != _label:
                path_nodes[(label, _label)] = find_path(graph, label, _label).nodes

    open_valves = [label for label, valve in valves.items() if valve.flow_rate == 0]
    closed_valves = [label for label, valve in valves.items() if valve.flow_rate != 0]
    max_pressure = [0]

    traverse_with_elephant('AA', 'AA', 0, open_valves, closed_valves, 0, valves, max_pressure, path_nodes)

    print('part2:', max_pressure)


if __name__ == '__main__':
    print('test.txt')
    with open('test.txt', 'r') as f:
        lines = f.readlines()
        lines = [line.replace('\n', '') for line in lines]
        part1(lines)
        part2(lines)

    # print('input.txt')
    # with open('input.txt', 'r') as f:
    #     lines = f.readlines()
    #     lines = [line.replace('\n', '') for line in lines]
    #     part1(lines)
    #     part2(lines)
