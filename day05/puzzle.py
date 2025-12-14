def parse_range(s):
    return [int(x) for x in s.split("-")]

def within(x, ranges):
    return any(lower <= x <= upper for lower, upper in ranges)

def compact(ranges):
    lst = sorted(ranges, key=lambda x: x[0])

    compacted = []
    start, end = lst[0]

    for lower, upper in lst[1:]:
        if lower <= end:
            end = max(end, upper)
        else:
            compacted.append((start, end))
            start, end = lower, upper

    compacted.append((start, end))
    return compacted

with open("input") as f:
    header, block = f.read().split("\n\n")

ranges = [parse_range(line) for line in header.splitlines()]
numbers = [int(line) for line in block.splitlines()]

# Puzzle 1
found = [x for x in numbers if within(x, ranges)]
print(len(found))

# Puzzle 2
aux = sum(end - start + 1 for start, end in compact(ranges))
print(aux)
