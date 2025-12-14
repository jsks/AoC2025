class Grid:
    def __init__(self, grid):
        self.nrow = len(grid)
        self.ncol = len(grid[0])
        self.grid = grid

    def __setitem__(self, pair, value):
        row, col = pair
        self.grid[row][col] = value

    def __iter__(self):
        return ((i, j) for i in range(self.nrow) for j in range(self.ncol))

    def neighbours(self, row, col):
        for i in range(max(row - 1, 0), min(row + 2, self.nrow)):
            for j in range(max(col - 1, 0), min(col + 2, self.ncol)):
                if i == row and j == col:
                    continue

                yield i, j

    def adjacent(self, row, col):
        return sum(self.grid[i][j] == '@' for i, j in self.neighbours(row, col))

    def accessible(self):
        for i, j in self:
            if self.grid[i][j] == '@' and self.adjacent(i, j) < 4:
                yield i, j

with open("input") as f:
    grid = Grid([list(line) for line in f.read().splitlines()])

    # Puzzle 1
    print(sum(1 for _ in grid.accessible()))

    # Puzzle 2
    count = 0
    while True:
        aux = 0
        for i, j in grid.accessible():
            aux += 1
            grid[i, j] = '.'

        if aux == 0:
            break

        count += aux

    print(count)
