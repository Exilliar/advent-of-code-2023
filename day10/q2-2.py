# faster implementation of q2

pipes = {
    "|": ((0, -1), (0, 1)),
    "-": ((-1, 0), (1, 0)),
    "L": ((0, -1), (1, 0)),
    "J": ((0, -1), (-1, 0)),
    "7": ((-1, 0), (0, 1)),
    "F": ((0, 1), (1, 0)),
}

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

    points = []
    if startPipeType != "|" and startPipeType != "-":
        points.append(startPos)

    for coord in coordsInLoop:
        if grid[coord[1]][coord[0]] != "|" and grid[coord[1]][coord[0]] != "-" and grid[coord[1]][coord[0]] != "S":
            points.append(coord)

    grid[startPos[1]][startPos[0]] = startPipeType

    total = 0

    # find if each point is contained in the polygon of the pipe network through ray casting https://en.wikipedia.org/wiki/Point_in_polygon (but faster than in q2.py)
    for y, row in enumerate(grid):
        x = 0
        hitCount = 0
        while x < len(row):
            currVal = grid[y][x]
            if (x, y) not in coordsInLoop:
                if hitCount != 0 and hitCount % 2 != 0:
                    total += 1
                x += 1
            else:
                if currVal == "|":
                    hitCount += 1
                    x += 1
                elif (x, y) in points:
                    pointIndex = points.index((x, y))
                    point = points[pointIndex]
                    pointLow = pointIndex - 1
                    pointHigh = pointIndex + 1
                    if pointHigh >= len(points):
                        pointHigh = 0

                    pointCheck = None
                    oldX = x
                    if points[pointLow][1] == y:
                        x = points[pointLow][0] + 1
                        pointCheck = points[pointLow]
                    elif points[pointHigh][1] == y:
                        x = points[pointHigh][0] + 1
                        pointCheck = points[pointHigh]
                    if pointCheck:
                        pointCheckType = grid[pointCheck[1]][pointCheck[0]]
                        oldCheckXType = grid[y][oldX]
                        if pointCheckType == "F" and oldCheckXType == "J":
                            hitCount += 1
                        elif pointCheckType == "J" and oldCheckXType == "F":
                            hitCount += 1
                        elif pointCheckType == "L" and oldCheckXType == "7":
                            hitCount += 1
                        elif pointCheckType == "7" and oldCheckXType == "L":
                            hitCount += 1

    print("total: " + str(total))
