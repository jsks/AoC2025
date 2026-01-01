from collections import defaultdict, Counter
from itertools import combinations
from functools import reduce
from math import prod, sqrt
from operator import sub


class Node:
    def __init__(self, line):
        x, y, z = [int(n) for n in line.split(",")]
        self.point = (x, y, z)
        self.circuit = None

    def reset(self):
        self.circuit = None


def euclidean(a, b):
    expr = reduce(lambda aux, pair: aux + sub(*pair) ** 2, zip(a.point, b.point), 0)
    return sqrt(expr)


def connect(circuits, a, b):
    if not (circuit := a.circuit or b.circuit):
        # Please don't actually do this in production
        circuit = hash((a, b))

    a.circuit = b.circuit = circuit
    circuits[circuit].add(a)
    circuits[circuit].add(b)


def merge(circuits, a, b):
    if a.circuit == b.circuit:
        return

    original = b.circuit
    for n in circuits[original]:
        n.circuit = a.circuit
        circuits[a.circuit].add(n)

    del circuits[original]


def run(circuits, nodes, start=0, end=None):
    distances = {(a, b): euclidean(a, b) for a, b in combinations(nodes, 2)}
    pairs = sorted(distances.items(), key=lambda item: item[1])

    end = end or len(pairs)
    for (a, b), _ in pairs[start:end]:
        if a.circuit and b.circuit:
            merge(circuits, a, b)
        else:
            connect(circuits, a, b)

        if len(circuits) == 1 and all(n.circuit is not None for n in nodes):
            return a.point[0], b.point[0]


with open("input") as f:
    input = f.readlines()
    nodes = [Node(line) for line in input]

circuits = defaultdict(set)

# Puzzle 1
run(circuits, nodes, end=1000)

counts = Counter(n.circuit for n in nodes if n.circuit)
product = prod(sorted(counts.values(), reverse=True)[:3])
print(product)

# Puzzle 2
x1, x2 = run(circuits, nodes, start=1001)
print(x1 * x2)
