numbers = ["0","1","2","3","4","5","6","7","8","9"]
specialChars = ['*', '%', '@', '#', '+', '$', '-', '=', '/', '&']

def checkAround(x, y, grid):
    maxX = len(grid[0]) - 1
    maxY = len(grid) - 1

    bottom1 = False
    bottom2 = False

    top1 = False
    top2 = False
    # x-1, y
    if x != 0 and grid[y][x-1] in numbers:
        yield getNumber(x-1, y, grid, maxX)
    # x-1, y-1
    if x != 0 and y != 0 and grid[y-1][x-1] in numbers:
        bottom1 = True
        yield getNumber(x-1, y-1, grid, maxX)
    # x, y-1
    if y != 0 and bottom1 != True and grid[y-1][x] in numbers:
        bottom2 = True
        yield getNumber(x, y-1, grid, maxX)
    # x+1, y-1
    if x != maxX and bottom2 != True and grid[y-1][x] not in numbers and y != 0 and grid[y-1][x+1] in numbers:
        yield getNumber(x+1, y-1, grid, maxX)
    # x+1, y
    if x != maxX and grid[y][x+1] in numbers:
        yield getNumber(x+1, y, grid, maxX)
    # x-1, y+1
    if x != 0 and y != maxY and grid[y+1][x-1] in numbers:
        top1 = True
        yield getNumber(x-1, y+1, grid, maxX)
    # x, y+1
    if y != maxY and top1 != True and grid[y+1][x] in numbers:
        top2 = True
        yield getNumber(x, y+1, grid, maxX)
    # x+1, y+1
    if x != maxX and top2 != True and grid[y+1][x] not in numbers and y != maxY and grid[y+1][x+1] in numbers:
        yield getNumber(x+1, y+1, grid, maxX)

def getNumber(x, y, grid, maxX):
    gridLine = grid[y]

    currX = x

    # find the start of the number
    while gridLine[currX-1] in numbers and currX > 0:
        currX -= 1

    if gridLine[currX] == "" or currX == -1:
        currX += 1

    # go back up the number, adding it to the string, then return the number as an int
    numberString = ""
    while gridLine[currX] in numbers and currX < maxX:
        numberString += gridLine[currX]
        currX += 1

    # annoying stuff with hitting the end of the line dealt with here
    if currX == maxX and gridLine[currX] in numbers:
        numberString += gridLine[currX]

    return int(numberString)

with open("input.txt", "r") as f:
    grid = []
    for line in f.readlines():
        grid.append([*line.strip()])

    total = 0

    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char in specialChars:
                numbersAround = checkAround(x, y, grid)
                total += sum(numbersAround)
    print(total)
