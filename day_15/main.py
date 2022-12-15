from typing import List, Set, Tuple


class Sensor:
    def __init__(self, x: int, y: int, dist: int):
        self.x = x
        self.y = y
        self.dist = dist


def part1(lines: List[str], y: int):
    sensors: Set[Sensor] = set()
    beacons: Set[Tuple[int, int]] = set()

    for line in lines:
        line = line.replace('Sensor at ', '').replace(' closest beacon is at ', '').replace(' ', '').replace('x=', '').replace('y=', '')
        splits = line.split(':')
        sensor_coords = (int(splits[0].split(',')[0]), int(splits[0].split(',')[1]))
        beacon_coords = (int(splits[1].split(',')[0]), int(splits[1].split(',')[1]))
        beacons.add(beacon_coords)

        manhattan_distance = abs(sensor_coords[0] - beacon_coords[0]) + abs(sensor_coords[1] - beacon_coords[1])
        sensor = Sensor(sensor_coords[0], sensor_coords[1], manhattan_distance)
        sensors.add(sensor)

    y_ranges = []
    for sensor in sensors:
        if abs(y - sensor.y) > sensor.dist: continue
        dist_diff = sensor.dist - abs(y - sensor.y)
        y_ranges.append((sensor.x - dist_diff, sensor.x + dist_diff))

    # merging the overlaps
    while True:
        try:
            for i in range(len(y_ranges)):
                for j in range(i+1, len(y_ranges)):
                    if y_ranges[j][0] <= y_ranges[i][0] and y_ranges[i][1] <= y_ranges[j][1]:
                        del y_ranges[i]
                        raise AssertionError
                    if y_ranges[i][0] <= y_ranges[j][0] and y_ranges[j][1] <= y_ranges[i][1]:
                        del y_ranges[j]
                        raise AssertionError
                    if y_ranges[j][0] <= y_ranges[i][0] and y_ranges[i][0] <= y_ranges[j][1]:
                        y_ranges[j] = (y_ranges[j][0], y_ranges[i][1])
                        del y_ranges[i]
                        raise AssertionError
                    if y_ranges[i][0] <= y_ranges[j][0] and y_ranges[j][0] <= y_ranges[i][1]:
                        y_ranges[i] = (y_ranges[i][0], y_ranges[j][1])
                        del y_ranges[j]
                        raise AssertionError
        except AssertionError: continue
        break

    no_beacon_positions = 0
    for y_range in y_ranges:
        no_beacon_positions += y_range[1] - y_range[0] + 1
        for beacon in beacons:
            if beacon[1] == y and y_range[0] <= beacon[0] and beacon[0] <= y_range[1]:
                no_beacon_positions -= 1

    print('part1:', no_beacon_positions)


def part2(lines: List[str], limit: int):
    sensors: Set[Sensor] = set()
    beacons: Set[Tuple[int, int]] = set()

    for line in lines:
        line = line.replace('Sensor at ', '').replace(' closest beacon is at ', '').replace(' ', '').replace('x=', '').replace('y=', '')
        splits = line.split(':')
        sensor_coords = (int(splits[0].split(',')[0]), int(splits[0].split(',')[1]))
        beacon_coords = (int(splits[1].split(',')[0]), int(splits[1].split(',')[1]))
        beacons.add(beacon_coords)

        manhattan_distance = abs(sensor_coords[0] - beacon_coords[0]) + abs(sensor_coords[1] - beacon_coords[1])
        sensor = Sensor(sensor_coords[0], sensor_coords[1], manhattan_distance)
        sensors.add(sensor)

    for y in range(0, limit + 1):
        y_ranges = []
        for sensor in sensors:
            if abs(y - sensor.y) > sensor.dist: continue
            dist_diff = sensor.dist - abs(y - sensor.y)
            y_ranges.append((sensor.x - dist_diff, sensor.x + dist_diff))

        right_most = 0
        prev_right = right_most
        while True:
            for y_range in y_ranges:
                if y_range[0] <= right_most and right_most <= y_range[1]:
                    right_most = y_range[1]
            if right_most >= limit: break
            if right_most == prev_right:
                print('part2:', (right_most + 1) * 4000000 + y)
                return
            prev_right = right_most

    print('part2:', None)


if __name__ == '__main__':
    # for fname in {'test.txt', 'input.txt'}:
    print('test.txt')
    with open('test.txt', 'r') as f:
        lines = f.readlines()
        lines = [line.replace('\n', '') for line in lines]
        part1(lines, 10)
        part2(lines, 20)

    print('input.txt')
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        lines = [line.replace('\n', '') for line in lines]
        part1(lines, 2000000)
        part2(lines, 4000000)
