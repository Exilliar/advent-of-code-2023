class Grid:
    def __init__(self, grid: list, separator: str):
        self.grid = []
        for g in grid:
            g = g.strip()
            if separator == "":
                self.grid.append([*g])
            else:
                self.grid.append(g.split(separator))

    def __str__(self):
        lines = []
        for row in self.grid:
            line = ""
            for col in row[:-1]:
                line += f"{col}\t"
            line += f"{row[len(row) - 1]}"
            lines.append(line)
        return "\n".join(lines)

    def expandEmptyRows(self):
        newGrid = []
        for row in self.grid:
            empty = True
            for col in row:
                if col != ".":
                    empty = False
            newGrid.append(row)
            if empty:
                newGrid.append(row)
        self.grid = newGrid

    def expandEmptyCols(self):
        newGrid = [[] for i in range(len(self.grid))]
        height = len(self.grid)
        width = len(self.grid[0])

        for x in range(width):
            empty = True
            for y in range(height):
                if self.grid[y][x] != ".":
                    empty = False
                newGrid[y].append(self.grid[y][x])
            if empty:
                for y in range(height):
                    newGrid[y].append(".")
        self.grid = newGrid

    def findChars(self, charToFind):
        coords = []
        for y, row in enumerate(self.grid):
            for x, col in enumerate(row):
                if col == charToFind:
                    coords.append((x, y))
        return coords

    def findPathSum(self, start, end):
        """Find the number of points crossed to get from one coord to another"""
        a = abs(start[0] - end[0])
        b = abs(start[1] - end[1])
        return a + b




with open("input.txt", "r") as f:
    lines = list(f.readlines())
    grid = Grid(lines, "")
    grid.expandEmptyRows()
    grid.expandEmptyCols()
    charsToFind = grid.findChars("#")

    total = 0
    totalPairs = 0

    for i, baseCoord in enumerate(charsToFind):
        for x, endCoord in enumerate(charsToFind):
            if x > i:
                pathSum = grid.findPathSum(baseCoord, endCoord)
                total += pathSum
                totalPairs += 1
    print(total)
