#!/usr/bin/env python

from itertools import accumulate

def parse(instruction):
    direction = -1 if instruction[0] == 'L' else 1
    return int(instruction[1:]) * direction

with open("input", "r") as file:
    data = [parse(line.strip()) for line in file]

    # Puzzle 1
    iter = accumulate(data, lambda x, y: (x + y) % 100, initial=50)
    print(sum(item == 0 for item in iter))

    # puzzle 2
    aux = 50
    cycles = 0
    for i in data:
        update = i + aux
        if i >= 0:
            cycles += update // 100
        else:
            cycles += (aux - 1) // 100 - (update - 1) // 100

        aux = update % 100

    print(cycles)
