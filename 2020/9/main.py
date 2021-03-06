from typing import List, NamedTuple
from enum import Enum
from collections import defaultdict

PREAMBLE_SIZE = 25

def ass(want, f, *args, **kwargs):
    got = f(*args, **kwargs)
    if got != want:
        print(f"{f.__qualname__} returned {got}, expected {want}")

def find_first_nonsum_number(numbers, preamble_size=PREAMBLE_SIZE):
    sums = defaultdict(int)
    for i in range(preamble_size):
        for j in range(i + 1, preamble_size):
            sums[numbers[i] + numbers[j]] += 1

    for new_idx in range(preamble_size, len(numbers)):
        new_num = numbers[new_idx]
        if new_num not in sums:
            return new_num
        old_idx = new_idx - preamble_size
        old_num = numbers[old_idx]

        for i in range(old_idx + 1, new_idx):
            sums[new_num + numbers[i]] += 1
            sums[old_num + numbers[i]] -= 1
            if sums[old_num + numbers[i]] == 0:
                del sums[old_num + numbers[i]]
    return None

TEST_NUMBERS = [int(line) for line in """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576""".split()]

ass(127, find_first_nonsum_number, TEST_NUMBERS, preamble_size=5)

def find_sum_subrange(numbers, target):
    i = 0
    j = 0
    current_sum = numbers[i]
    while current_sum != target:
        if current_sum < target:
            j += 1
            current_sum += numbers[j]
        else:
            if i != j:
                current_sum -= numbers[i]
                i += 1
            else:
                i += 1
                j += 1
                current_sum = numbers[i]

    return i, j

ass((2, 5), find_sum_subrange, TEST_NUMBERS, 127)

def find_solution_from_subrange(numbers, left, right):
    return min(numbers[left:right]) + max(numbers[left:right])


def main():
    with open('in.txt') as infile:
        lines = [line.strip() for line in infile.readlines()]
        numbers = list(map(int, lines))
        nonsum_number = find_first_nonsum_number(numbers)
        print(nonsum_number)
        print(find_solution_from_subrange(numbers, *find_sum_subrange(numbers, nonsum_number)))


if __name__ == "__main__":
    main()
