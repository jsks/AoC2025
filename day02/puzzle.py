from itertools import batched
from math import log10, floor

def parse_range(str):
    return [int(x) for x in str.split("-")]

def puzzle1(start, end):
    found = 0
    i = start
    while i <= end:
        ndigits = floor(log10(i)) + 1
        if ndigits % 2 != 0:
            i = 10 ** ndigits
            continue

        candidate = str(i)
        length = len(candidate)
        if candidate[0:(length // 2)] == candidate[(length // 2):]:
            found += i

        i += 1

    return found


def puzzle2(start, end):
    found = 0
    for i in range(start, end + 1):
        candidate = str(i)
        digits = set(candidate)

        if len(candidate) == len(digits):
            continue

        if len(digits) == 1:
            found += i
            continue

        for j in range(2, len(candidate) // 2 + 1):
            iter = batched(candidate, n=j)
            first = next(iter)

            if all(t == first for t in iter):
                found += i
                break

    return found

with open("input") as f:
    input = f.read().strip()
    ranges = [parse_range(range_str) for range_str in input.split(",")]

    # Puzzle 1
    print(sum(puzzle1(lower, upper) for lower, upper in ranges))

    # Puzzle 2
    print(sum(puzzle2(lower, upper) for lower, upper in ranges))
