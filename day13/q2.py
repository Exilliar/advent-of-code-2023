def horizontalCheck(grid: list):
    for i, g in enumerate(grid):
        if i > 0:
            moveToDown = min(i, len(grid) - i)
            numDiffs = 0
            x = 0
            while x < moveToDown and numDiffs < 2:
                down = grid[i - x - 1]
                up = grid[i + x]
                for a, d in enumerate(down):
                    if d != up[a]:
                        numDiffs += 1
                x += 1
            if numDiffs == 1:
                return i
    return -1

def verticalCheck(grid: list):
    cols = []
    for i in range(len(grid[0])):
        col = [a[i] for a in grid]
        cols.append(col)
    return horizontalCheck(cols)

with open("input.txt", "r") as f:
    grids = [[]]
    gridNum = 0
    for line in f.readlines():
        line = line.strip()
        if line != "":
            grids[gridNum].append([*line])
        else:
            grids.append([])
            gridNum += 1
    total = 0
    for grid in grids:
        horizontal = horizontalCheck(grid)
        vertical = verticalCheck(grid)
        if horizontal != -1:
            total += horizontal * 100
        elif vertical != -1:
            total += vertical
    print(f"total: {total}")