
from typing import List


def part1(lines: List[str]):
    full_contained = 0
    for line in lines:
        lists = line.split(',')
        list1start, list1end = int(lists[0].split('-')[0]), int(lists[0].split('-')[1])
        list2start, list2end = int(lists[1].split('-')[0]), int(lists[1].split('-')[1])
        if list1start <= list2start and list1end >= list2end or list2start <= list1start and list2end >= list1end:
            full_contained += 1
    print('part1:', full_contained)


def part2(lines: List[str]):
    overlapped = 0
    for line in lines:
        lists = line.split(',')
        list1start, list1end = int(lists[0].split('-')[0]), int(lists[0].split('-')[1])
        list2start, list2end = int(lists[1].split('-')[0]), int(lists[1].split('-')[1])
        if list1start <= list2end and list1start >= list2start or list1end >= list2start and list1end <= list2end or list2start >= list1start and list2start <= list1end or list2end >= list1start and list2end <= list1end:
            overlapped += 1
    print('part2:', overlapped)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        lines = [line.replace('\n', '') for line in lines]
        part1(lines)
        part2(lines)
