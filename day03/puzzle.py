def ljp(bank, n=2, init=''):
    if n == 0:
        return init

    subset = bank[:-(n - 1)] if n > 1 else bank
    max_idx = bank.index(max(subset))

    return ljp(bank[(max_idx + 1):], n - 1, init + bank[max_idx])

def puzzle(banks, n):
    return sum(int(ljp(line, n)) for line in banks)

with open("input") as f:
    input = f.read().splitlines()

    # Puzzle 1
    print(puzzle(input, 2))

    # Puzzle 2
    print(puzzle(input, 12))
