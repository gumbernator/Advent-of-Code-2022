from typing import List, Set, Tuple
from itertools import cycle


def part1(lines: List[str]):
    nums = [int(line) for line in lines]
    new_nums = list(range(len(nums)))
    for i, num in enumerate(nums):
        # print([nums[i] for i in new_nums])
        moves = abs(num) % (len(nums) - 1)
        moves = moves if num > 0 else -moves
        if moves == 0: continue
        idx = new_nums.index(i)
        insert_idx = idx + moves

        if moves > 0:
            if insert_idx >= len(nums):
                insert_idx = insert_idx % len(nums)
            new_nums.insert(insert_idx + 1, i)
            insert_idx += 1
        else:
            if insert_idx < 0:
                insert_idx = len(nums) + insert_idx
            new_nums.insert(insert_idx, i)
        if insert_idx > idx:
            del new_nums[idx]
        else:
            del new_nums[idx+1]

    new_nums = [nums[i] for i in new_nums]
    zero_idx = new_nums.index(0)
    _1000th = (zero_idx + 1000) % len(nums)
    _2000th = (zero_idx + 2000) % len(nums)
    _3000th = (zero_idx + 3000) % len(nums)

    print('part1:', new_nums[_1000th] + new_nums[_2000th] + new_nums[_3000th])


def part2(lines: List[str]):
    nums = [int(line) * 811589153 for line in lines]
    new_nums = list(range(len(nums)))

    for _ in range(10):
        # print(_, [nums[i] for i in new_nums])
        for i, num in enumerate(nums):
            # print([nums[i] for i in new_nums])
            moves = abs(num) % (len(nums) - 1)
            moves = moves if num > 0 else -moves
            if moves == 0: continue
            idx = new_nums.index(i)
            insert_idx = idx + moves

            if moves > 0:
                if insert_idx >= len(nums):
                    insert_idx = insert_idx % len(nums)
                new_nums.insert(insert_idx + 1, i)
                insert_idx += 1
            else:
                if insert_idx < 0:
                    insert_idx = len(nums) + insert_idx
                new_nums.insert(insert_idx, i)
            if insert_idx > idx:
                del new_nums[idx]
            else:
                del new_nums[idx+1]
    # print(10, [nums[i] for i in new_nums])

    new_nums = [nums[i] for i in new_nums]
    zero_idx = new_nums.index(0)
    _1000th = (zero_idx + 1000) % len(nums)
    _2000th = (zero_idx + 2000) % len(nums)
    _3000th = (zero_idx + 3000) % len(nums)

    print('part2:', new_nums[_1000th] + new_nums[_2000th] + new_nums[_3000th])


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
