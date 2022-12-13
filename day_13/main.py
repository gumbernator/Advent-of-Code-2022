from typing import List, Tuple


def compare(packet_left, packet_right):
    if isinstance(packet_left, int) and isinstance(packet_right, int):
        if packet_left < packet_right:
            return -1
        elif packet_left > packet_right:
            return 1
        else: # packet_left == packet_right
            return 0
    if isinstance(packet_left, List) and isinstance(packet_right, List):
        for left_val, right_val in zip(packet_left, packet_right):
            compare_res = compare(left_val, right_val)
            if compare_res == 0: continue
            return compare_res
        return compare(len(packet_left), len(packet_right))
    if isinstance(packet_left, List): return compare(packet_left, [packet_right])
    if isinstance(packet_right, List): return compare([packet_left], packet_right)


def part1(lines: List[str]):
    pairs = []
    current_pair = []
    for line in lines:
        if line == '':
            pairs.append(current_pair)
            current_pair = []
            continue
        current_pair.append(eval(line))
    pairs.append(current_pair)

    right_index_sum = 0
    for i, pair in enumerate(pairs):
        if compare(pair[0], pair[1]) == -1:
            right_index_sum += i + 1
    print('part1:', right_index_sum)


def part2(lines: List[str]):
    dividers = [[[2]], [[6]]]
    pairs = []
    for line in lines:
        if line == '': continue
        pairs.append(eval(line))
    pairs.append(dividers[0])
    pairs.append(dividers[1])

    n = len(pairs)
    for i in range(n):
        for j in range(n-i-1):
            if compare(pairs[j+1], pairs[j]) == -1:
                pairs[j], pairs[j+1] = pairs[j+1], pairs[j]

    divider_idx = []
    for i, pair in enumerate(pairs):
        if pair in dividers:
            divider_idx.append(i+1)
    print('part2:', divider_idx[0] * divider_idx[1])


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
    # with open('test.txt', 'r') as f:
        lines = f.readlines()
        lines = [line.replace('\n', '') for line in lines]
        part1(lines)
        part2(lines)

