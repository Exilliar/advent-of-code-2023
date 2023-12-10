pipes = {
    "|": ((0, -1), (0, 1)),
    "-": ((-1, 0), (1, 0)),
    "L": ((0, -1), (1, 0)),
    "J": ((0, -1), (-1, 0)),
    "7": ((-1, 0), (0, 1)),
    "F": ((0, 1), (1, 0)),
}

def GetUpLeft(coordinates, grid): # coordinates: (x: int, y: int)
    if coordinates[1] != 0 and coordinates[0] != 0:
        return ((coordinates[0] - 1, coordinates[1] - 1), grid[coordinates[1] - 1][coordinates[0] - 1])
    return False

def GetUp(coordinates, grid): # coordinates: (x: int, y: int)
    if coordinates[1] != 0:
        return ((coordinates[0] , coordinates[1] - 1), grid[coordinates[1] - 1][coordinates[0]])
    return False

def GetUpRight(coordinates, grid): # coordinates: (x: int, y: int)
    if coordinates[1] != 0 and coordinates[0] != len(grid[0]) - 1:
        return ((coordinates[0] + 1, coordinates[1] - 1), grid[coordinates[1] - 1][coordinates[0] + 1])
    return False

def GetLeft(coordinates, grid):
    if coordinates[0] != 0:
        return ((coordinates[0] - 1, coordinates[1]), grid[coordinates[1]][coordinates[0] - 1])
    return False

def GetRight(coordinates, grid):
    if coordinates[0] != len(grid[0]) - 1:
        return ((coordinates[0] + 1, coordinates[1]), grid[coordinates[1]][coordinates[0] + 1])
    return False

def GetDownLeft(coordinates, grid):
    if coordinates[1] != len(grid) - 1 and coordinates[0] != 0:
        return ((coordinates[0] - 1, coordinates[1] + 1), grid[coordinates[1] + 1][coordinates[0] - 1])
    return False

def GetDown(coordinates, grid):
    if coordinates[1] != len(grid) - 1:
        return ((coordinates[0], coordinates[1] + 1), grid[coordinates[1] + 1][coordinates[0]])
    return False

def GetDownRight(coordinates, grid):
    if coordinates[1] != len(grid) - 1 and coordinates[0] != len(grid[0]) - 1:
        return ((coordinates[0] + 1, coordinates[1] + 1), grid[coordinates[1] + 1][coordinates[0] + 1])
    return False

def PipeCanConnect(pipePos, currPos, grid):
    pipe = grid[pipePos[1]][pipePos[0]]
    if pipe not in pipes:
        return False
    pipeConnections = pipes[pipe]
    if (pipePos[0] + pipeConnections[0][0] == currPos[0] and pipePos[1] + pipeConnections[0][1] == currPos[1])\
        or (pipePos[0] + pipeConnections[1][0] == currPos[0] and pipePos[1] + pipeConnections[1][1] == currPos[1]):
        return True
    return False

def coordinatesLinked(oldCoords, newCoords, allCoords: list):
    oldCoordsIndex = allCoords.index(oldCoords)
    newCoordsIndex = allCoords.index(newCoords)

    if oldCoordsIndex == newCoordsIndex - 1 or oldCoordsIndex == newCoordsIndex + 1:
        return True
    else:
        return False

with open("input.txt", "r") as f:
    # convert input to more easy to work with grid
    grid = []
    for line in f.readlines():
        line = line.strip()
        grid.append([*line])

    # find the starting coordinate
    startPos = None
    startX = -1
    startY = -1
    for index, line in enumerate(grid):
        try:
            startX = line.index("S")
            startY = index
        except ValueError:
            pass

    startPos = (startX, startY)

    # figure out what type of pipe the start coordinate is
    ccLeft = PipeCanConnect((startPos[0] - 1, startPos[1]), startPos, grid)
    ccRight = PipeCanConnect((startPos[0] + 1, startPos[1]), startPos, grid)
    ccUp = PipeCanConnect((startPos[0], startPos[1] - 1), startPos, grid)
    ccDown = PipeCanConnect((startPos[0], startPos[1] + 1), startPos, grid)

    startPipeType = ""

    if ccUp and ccDown:
        startPipeType = "|"
    elif ccLeft and ccRight:
        startPipeType = "-"
    elif ccUp and ccRight:
        startPipeType = "L"
    elif ccUp and ccLeft:
        startPipeType = "J"
    elif ccLeft and ccDown:
        startPipeType = "7"
    elif ccDown and ccRight:
        startPipeType = "F"

    startPipe = pipes[startPipeType]

    # traverse the pipe till we get back to the start
    steps = 1
    oldX = startPos[0]
    oldY = startPos[1]
    coordsInLoop = [(oldX, oldY)]
    currentX = startPos[0] + startPipe[0][0]
    currentY = startPos[1] + startPipe[0][1]
    currentPipe = grid[currentY][currentX]

    while currentPipe != "S":
        steps += 1
        pipe = pipes[currentPipe]
        if currentX + pipe[0][0] == oldX and currentY + pipe[0][1] == oldY:
            oldX = currentX
            oldY = currentY
            currentX = currentX + pipe[1][0]
            currentY = currentY + pipe[1][1]
        else:
            oldX = currentX
            oldY = currentY
            currentX = currentX + pipe[0][0]
            currentY = currentY + pipe[0][1]
        currentPipe = grid[currentY][currentX]
        coordsInLoop.append((oldX, oldY))

    total = 0
    points = []
    if startPipeType != "|" and startPipeType != "-":
        points.append(startPos)

    for coord in coordsInLoop:
        if grid[coord[1]][coord[0]] != "|" and grid[coord[1]][coord[0]] != "-" and grid[coord[1]][coord[0]] != "S":
            points.append(coord)

    grid[startPos[1]][startPos[0]] = startPipeType

    newGrid = []
    for i, r in enumerate(grid):
        newGrid.append([])
        for c in r:
            newGrid[i].append(c)

    for y, row in enumerate(grid):
        print(y)
        for x, square in enumerate(row):
            if (x, y) not in coordsInLoop:
                xCheck = x - 1
                numHitLeft = 0
                while xCheck >= 0:
                    if (xCheck, y) in coordsInLoop:
                        checkSquare = grid[y][xCheck]
                        if (xCheck, y) in points:
                            pointIndex = points.index((xCheck, y))
                            point = points[pointIndex]
                            pointLow = pointIndex - 1
                            pointHigh = pointIndex + 1
                            if pointHigh >= len(points):
                                pointHigh = 0

                            pointCheck = None
                            oldXCheck = xCheck
                            if points[pointLow][1] == y:
                                xCheck = points[pointLow][0] - 1
                                pointCheck = points[pointLow]
                            elif points[pointHigh][1] == y:
                                xCheck = points[pointHigh][0] - 1
                                pointCheck = points[pointHigh]
                            if pointCheck:
                                pointCheckType = grid[pointCheck[1]][pointCheck[0]]
                                oldCheckXType = grid[y][oldXCheck]
                                if pointCheckType == "F" and oldCheckXType == "J":
                                    numHitLeft += 1
                                elif pointCheckType == "J" and oldCheckXType == "F":
                                    numHitLeft += 1
                                elif pointCheckType == "L" and oldCheckXType == "7":
                                    numHitLeft += 1
                                elif pointCheckType == "7" and oldCheckXType == "L":
                                    numHitLeft += 1
                        else:
                            numHitLeft += 1
                            xCheck -= 1
                    else:
                        xCheck -= 1
                if (numHitLeft % 2 != 0 and numHitLeft != 0):
                    if newGrid[y][x] != "1":
                        total += 1
                    newGrid[y][x] = "1, " + str(numHitLeft)
                else:
                    newGrid[y][x] = "0, " + str(numHitLeft)

    print("total: " + str(total))
