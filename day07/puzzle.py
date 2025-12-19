from functools import cache
from itertools import chain

with open("input") as file:
    input = file.read().splitlines()

# Puzzle 1
beams = [input[0].find("S")]
count = 0
for i in range(1, len(input)):
    new = []
    for beam in beams:
        if input[i][beam] == "^":
            new.append([beam - 1, beam + 1])
            count += 1
        else:
            new.append([beam])

    beams = set(chain.from_iterable(new))

print(count)


# Puzzle 2
def puzzle2(beam, rows):
    @cache
    def recurse(beam, i=1):
        for i in range(i, len(rows)):
            if rows[i][beam] != "^":
                continue

            left = recurse(beam - 1, i + 1)
            right = recurse(beam + 1, i + 1)

            return left + right

        return 1

    return recurse(beam)


beam = input[0].find("S")
puzzle2(beam, input)
