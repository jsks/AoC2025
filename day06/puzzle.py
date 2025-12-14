from functools import reduce
from itertools import zip_longest
from operator import add, mul


def split_at(s, positions):
    extended = positions + [len(s)]
    return [s[i:j].rstrip() for i, j in zip(extended[:-1], extended[1:])]


def parse_problems(input):
    lines = input.splitlines()
    ops = lines[-1]
    split_points = [i for i, ch in enumerate(ops) if not ch.isspace()]

    rows = [split_at(s, split_points) for s in lines[:-1]] + [ops.split()]
    return [lst[::-1] for lst in zip(*rows)]


def eval_problem(p, vertical_digits=False):
    op, *args = p
    if vertical_digits:
        args = ["".join(digits[::-1]) for digits in zip_longest(*args, fillvalue="")]

    return reduce(add if op == "+" else mul, map(lambda x: int(x.strip()), args))


with open("input") as f:
    input = f.read()
    problems = parse_problems(input)

    # Puzzle 1
    aux = sum(eval_problem(p) for p in problems)
    print(aux)

    # Puzzle 2
    aux = sum(eval_problem(p, vertical_digits=True) for p in problems)
    print(aux)
