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
    label_one_heading: str,
    label_two_heading: str,
    open_valves: List[str],
    closed_valves: List[str],
    total_pressure: int,
    valves: Dict[str, Valve],
    max_pressure: List[int],
    path_nodes: Dict[Tuple[str, str], List[str]]
    ):
    print(total_pressure)
    if minute >= 26:
        max_pressure[0] = max(max_pressure[0], total_pressure)
        return

    total_pressure + sum([valves[label].flow_rate for label in open_valves])

    if label_one_heading is None and label_two_heading is None:
        for i in range(len(closed_valves)):
            for j in range(i+1, len(closed_valves)):
                # new_closed_valves = [val for k, val in enumerate(closed_valves) if k not in {i, j}]
                # tunnels2next = min(len(path_nodes[(label_one, closed_valves[i])]), len(path_nodes[(label_two, closed_valves[j])])) - 1

                traverse_with_elephant(
                    path_nodes[(label_one, closed_valves[i])][1],
                    path_nodes[(label_two, closed_valves[j])][1],
                    # minute + tunnels2next,
                    minute,
                    closed_valves[i],
                    closed_valves[j],
                    open_valves,
                    closed_valves,
                    total_pressure,
                    valves,
                    max_pressure,
                    path_nodes
                )
        return

    if label_one == label_one_heading and label_two == label_two_heading:
        if label_one != label_two:
            new_open_valves = open_valves + [label_one, label_two]
            new_closed_valves = [val for val in closed_valves if val not in {label_one, label_two}]
        else:
            new_open_valves = open_valves + [label_one]
            new_closed_valves = [val for val in closed_valves if val not in {label_one}]

        if len(new_closed_valves) >= 2:
            for i in range(len(new_closed_valves)):
                for j in range(i+1, len(new_closed_valves)):
                    # tunnels2next = min(len(path_nodes[(label_one, new_closed_valves[i])]), len(path_nodes[(label_two, new_closed_valves[j])])) - 1
                    traverse_with_elephant(
                        label_one,
                        label_two,
                        minute + 1,
                        new_closed_valves[i],
                        new_closed_valves[j],
                        new_open_valves,
                        new_closed_valves,
                        total_pressure,
                        valves,
                        max_pressure,
                        path_nodes
                    )
        elif len(new_closed_valves) == 1:
            traverse_with_elephant(
                label_one,
                label_two,
                minute + 1,
                new_closed_valves[0],
                new_closed_valves[0],
                new_open_valves,
                new_closed_valves,
                total_pressure,
                valves,
                max_pressure,
                path_nodes
            )
        else:
            max_pressure[0] = max(max_pressure[0], total_pressure)
        return

    if label_one == label_one_heading:
        new_open_valves = open_valves + [label_one]
        new_closed_valves = [val for val in closed_valves if val not in {label_one}]
        if label_two_heading is not None:
            label_two = path_nodes[(label_two, label_two_heading)][1]
        for valve in new_closed_valves:
            if valve == label_two_heading: continue
            traverse_with_elephant(
                label_one,
                label_two,
                minute + 1,
                valve,
                label_two_heading,
                new_open_valves,
                new_closed_valves,
                total_pressure,
                valves,
                max_pressure,
                path_nodes
            )
        if new_closed_valves == [label_two_heading]:
            traverse_with_elephant(
                label_one,
                label_two,
                minute + 1,
                None,
                label_two_heading,
                new_open_valves,
                new_closed_valves,
                total_pressure,
                valves,
                max_pressure,
                path_nodes
            )
        return

    if label_two == label_two_heading:
        new_open_valves = open_valves + [label_two]
        new_closed_valves = [val for val in closed_valves if val not in {label_two}]
        if label_one_heading is not None:
            label_one = path_nodes[(label_one, label_one_heading)][1]
        for valve in new_closed_valves:
            if valve == label_one_heading: continue
            traverse_with_elephant(
                label_one,
                label_two,
                minute + 1,
                label_one_heading,
                valve,
                new_open_valves,
                new_closed_valves,
                total_pressure,
                valves,
                max_pressure,
                path_nodes
            )
        if new_closed_valves == [label_one_heading]:
            traverse_with_elephant(
                label_one,
                label_two,
                minute + 1,
                label_one_heading,
                None,
                new_open_valves,
                new_closed_valves,
                total_pressure,
                valves,
                max_pressure,
                path_nodes
            )
        return

    label_one = path_nodes[(label_one, label_one_heading)][1] if label_one_heading is not None else label_one
    label_two = path_nodes[(label_two, label_two_heading)][1] if label_two_heading is not None else label_two
    traverse_with_elephant(
        label_one,
        label_two,
        minute + 1,
        label_one_heading,
        label_two_heading,
        open_valves,
        closed_valves,
        total_pressure,
        valves,
        max_pressure,
        path_nodes
    )

    # if label_one == label_one_heading and label_two == label_two_heading and label_one != label_two:
    #     # released_pressure_one = (25 - minute) * valves[label_one].flow_rate
    #     # released_pressure_two = (25 - minute) * valves[label_two].flow_rate
    #     # total_pressure += released_pressure_one + released_pressure_two
    #     # minute += 1
    #     new_closed_valves = [val for val in closed_valves if val not in {label_one, label_two}]

    #     if len(new_closed_valves) >= 2:
    #         for i in range(len(new_closed_valves)):
    #             for j in range(i+1, len(new_closed_valves)):
    #                 tunnels2next = min(len(path_nodes[(label_one, new_closed_valves[i])]), len(path_nodes[(label_two, new_closed_valves[j])])) - 1
    #                 traverse_with_elephant(
    #                     path_nodes[(label_one, new_closed_valves[i])][tunnels2next],
    #                     path_nodes[(label_two, new_closed_valves[j])][tunnels2next],
    #                     minute + tunnels2next,
    #                     new_closed_valves[i],
    #                     new_closed_valves[j],
    #                     new_closed_valves,
    #                     total_pressure,
    #                     valves,
    #                     max_pressure,
    #                     path_nodes
    #                 )
    #     elif len(new_closed_valves) == 1:
    #         tunnels2next = min(len(path_nodes[(label_one, new_closed_valves[0])]), len(path_nodes[(label_two, new_closed_valves[0])])) - 1
    #         traverse_with_elephant(
    #             path_nodes[(label_one, new_closed_valves[0])][tunnels2next],
    #             path_nodes[(label_two, new_closed_valves[0])][tunnels2next],
    #             minute + tunnels2next,
    #             new_closed_valves[0],
    #             new_closed_valves[0],
    #             new_closed_valves,
    #             total_pressure,
    #             valves,
    #             max_pressure,
    #             path_nodes
    #         )
    #     else:
    #         max_pressure[0] = max(max_pressure[0], total_pressure)
    #     return

    # # print(label_one, label_one_heading)
    # # print(label_two, label_two_heading)
    # # print(len(closed_valves))
    # if label_one == label_one_heading:
    #     released_pressure_one = (25 - minute) * valves[label_one].flow_rate
    #     total_pressure += released_pressure_one
    #     minute += 1
    #     label_two = path_nodes[(label_two, label_two_heading)][1]
    #     new_closed_valves = [val for val in closed_valves if val != label_one]
    #     for valve in new_closed_valves:
    #         if valve == label_two_heading: continue
    #         tunnels2next = min(len(path_nodes[(label_one, valve)]), len(path_nodes[(label_two, label_two_heading)])) - 1
    #         traverse_with_elephant(
    #             path_nodes[(label_one, valve)][tunnels2next],
    #             path_nodes[(label_two, label_two_heading)][tunnels2next],
    #             minute + tunnels2next,
    #             valve,
    #             label_two_heading,
    #             new_closed_valves,
    #             total_pressure,
    #             valves,
    #             max_pressure,
    #             path_nodes
    #         )
    #     if len(new_closed_valves) == 0:
    #         tunnels2next = min(len(path_nodes[(label_one, label_two_heading)]), len(path_nodes[(label_two, label_two_heading)])) - 1
    #         left_minute = 25 - minute - tunnels2next - 1
    #         released_pressure = max(left_minute * valves[label_one].flow_rate, left_minute * valves[label_two].flow_rate)
    #         if left_minute <= 0:
    #             max_pressure[0] = max(max_pressure[0], total_pressure)
    #         else:
    #             max_pressure[0] = max(max_pressure[0], total_pressure + released_pressure)
    #     return

    # if label_two == label_two_heading:
    #     released_pressure_two = (25 - minute) * valves[label_two].flow_rate
    #     total_pressure += released_pressure_two
    #     minute += 1
    #     label_one = path_nodes[(label_one, label_one_heading)][1]
    #     new_closed_valves = [val for val in closed_valves if val != label_two]
    #     for valve in new_closed_valves:
    #         if valve == label_one_heading: continue
    #         tunnels2next = min(len(path_nodes[(label_one, label_one_heading)]), len(path_nodes[(label_two, valve)])) - 1
    #         traverse_with_elephant(
    #             path_nodes[(label_one, label_one_heading)][tunnels2next],
    #             path_nodes[(label_two, valve)][tunnels2next],
    #             minute + tunnels2next,
    #             label_one_heading,
    #             valve,
    #             new_closed_valves,
    #             total_pressure,
    #             valves,
    #             max_pressure,
    #             path_nodes
    #         )
    #     if len(new_closed_valves) == 0:
    #         tunnels2next = min(len(path_nodes[(label_one, label_one_heading)]), len(path_nodes[(label_two, label_one_heading)])) - 1
    #         left_minute = 25 - minute - tunnels2next - 1
    #         released_pressure = max(left_minute * valves[label_one].flow_rate, left_minute * valves[label_two].flow_rate)
    #         if left_minute <= 0:
    #             max_pressure[0] = max(max_pressure[0], total_pressure)
    #         else:
    #             max_pressure[0] = max(max_pressure[0], total_pressure + released_pressure)
    #     return

    # if label_one == label_one_heading and label_two == label_two_heading:
    #     new_closed_valves = [val for val in closed_valves if val not in {label_one, label_two}]
    #     released_pressure_one = (25 - minute) * valves[label_one].flow_rate
    #     released_pressure_two = (25 - minute) * valves[label_two].flow_rate


    # for i in range(len(closed_valves)):
    #     for j in range(i+1, len(closed_valves)):
    #         new_closed_valves = [val for k, val in enumerate(closed_valves) if k not in {i, j}]

    #         passed_minutes = path_nodes[(label, closed_valve)]
    #         released_pressure = (30 - minute - passed_minutes) * valves[closed_valve].flow_rate

    # for closed_valve in closed_valves:
    #     new_closed_valves = closed_valves.copy()
    #     new_closed_valves.remove(closed_valve)
    #     pass


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

    traverse_with_elephant('AA', 'AA', 0, None, None, open_valves, closed_valves, 0, valves, max_pressure, path_nodes)

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
