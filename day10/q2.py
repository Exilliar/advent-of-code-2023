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

    print(f"up: {ccUp}, down: {ccDown}, left: {ccLeft}, right: {ccRight}")

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
        print("append start pipe: " + str(startPos))
        points.append(startPos)

    for coord in coordsInLoop:
        if grid[coord[1]][coord[0]] != "|" and grid[coord[1]][coord[0]] != "-" and grid[coord[1]][coord[0]] != "S":
            points.append(coord)
    print(points)

    grid[startPos[1]][startPos[0]] = startPipeType

    # firstSum = 0
    # secondSum = 0
    # for index, coord in enumerate(points[:-1]):
    #     # print(coord)
    #     # if index != len(coordsInLoop) - 1:
    #     print(coord[0] * points[index+1][1])
    #     print(coord[1] * points[index+1][0])
    #     firstSum += coord[0] * points[index+1][1]
    #     secondSum += coord[1] * points[index+1][0]
    # print()
    # # print(firstSum)
    # # print()
    # # print(secondSum)
    # print(f"area: {secondSum - firstSum}")
    # print()
    # print(coordsInLoop)
    # print(len(coordsInLoop))
    # print(abs(firstSum - secondSum) - len(coordsInLoop))

    newGrid = []
    for i, r in enumerate(grid):
        newGrid.append([])
        for c in r:
            newGrid[i].append(c)
    # print("new Grid: " + str(newGrid))
    # for g in grid:
    #     print(g)

    for y, row in enumerate(grid):
        print(y)
        for x, square in enumerate(row):
            # print(x)
            # if square != "." and (x,y) not in coordsInLoop:
            #     newGrid[y][x] = "X"
            if (x, y) not in coordsInLoop:
                xCheck = x - 1
                numHitLeft = 0
                while xCheck >= 0:
                    # print(f"{xCheck}, {y}")
                    # if x == 10 and y == 5:
                    #     print(xCheck)
                    if (xCheck, y) in coordsInLoop:
                        # inLoopIndex = coordsInLoop.index((xCheck, y))
                        checkSquare = grid[y][xCheck]
                        # if checkSquare != "|":
                        if (xCheck, y) in points:
                            # print("in points")
                            # if x == 10 and y == 5:
                            #         print("eh?")
                            pointIndex = points.index((xCheck, y))
                            point = points[pointIndex]
                            pointLow = pointIndex - 1
                            # if pointLow < 0:
                            #     pointLow = len(points) - 1
                            pointHigh = pointIndex + 1
                            if pointHigh >= len(points):
                                pointHigh = 0
                            # if x == 10 and y == 5:
                            #     print(f"pointLow: {pointLow}, pointHigh: {pointHigh}")
                            #     print(f"fullPointLow: {points[pointLow]}")
                            #     print(f"fullPointHigh: {points[pointHigh]}")

                            pointCheck = None
                            oldXCheck = xCheck
                            if points[pointLow][1] == y:
                                # print("go low")
                                xCheck = points[pointLow][0] - 1
                                pointCheck = points[pointLow]
                            elif points[pointHigh][1] == y:
                                # print("go high")
                                # if x == 10 and y == 5:
                                #     print("got it correct?")
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
                                # print(f"{pointCheckType}-{oldCheckXType}")
                            # else:
                            #     print("neither?")
                        else:
                            # print("hit left")
                            # if x == 10 and y == 5:
                            #     print("whack off one")
                            numHitLeft += 1
                            # if x == 10 and y == 5:
                            #     print("inc hit left")
                            xCheck -= 1
                    else:
                        xCheck -= 1
                # print(numHit)
                # xCheck = x + 1
                # numHitRight = 0
                # while xCheck < len(row):
                #     if (xCheck, y) in coordsInLoop:
                #         numHitRight += 1
                #         checkSquare = grid[y][xCheck]
                #         while checkSquare != "." and checkSquare != "|" and xCheck < len(row):
                #             # print("moving")
                #             xCheck += 1
                #             checkSquare = grid[y][xCheck]
                #     xCheck += 1
                if (numHitLeft % 2 != 0 and numHitLeft != 0):
                    # print(f"\n({x}, {y})")
                    # print(f"numHitLeft: {numHitLeft}")
                    if newGrid[y][x] != "1":
                        total += 1
                    newGrid[y][x] = "1, " + str(numHitLeft)
                else:
                    newGrid[y][x] = "0, " + str(numHitLeft)

    # total = 0
    # print(coordsInLoop)
    # for index, coord in enumerate(coordsInLoop):
    #     x = coord[0]
    #     y = coord[1]
    #     print()
    #     print(f"({x}, {y})")
    #     # move to the right/left
    #     leftStop = False
    #     leftStopBad = False # bad = hit outside of loop or end of grid
    #     rightStop = False
    #     rightStopBad = False # bad = hit outside of loop or end of grid
    #     i = 1
    #     rightSum = 0
    #     rightCoords = []
    #     leftSum = 0
    #     leftCoords = []
    #     while not leftStop or not rightStop:
    #         # print(i)
    #         # if (i > 4):
    #         #     print(f"oh no!\nrightStop: {rightStop}\nleftStop: {leftStop}\nloopCheck: {(not leftStop and not rightStop)}")
    #         #     break
    #         rightX = x + i
    #         if rightX == len(grid[0]) or rightStop == True:
    #             print(f"right hit end of grid: ({rightX}, {y})")
    #             rightStop = True
    #             rightStopBad = True
    #         else:
    #             print("move to right")
    #             # move to the right
    #             if grid[y][rightX] == ".":
    #                 rightSum += 1
    #                 rightCoords.append((rightX, y))
    #             if (rightX, y) in coordsInLoop:
    #                 print("right hit coord in loop")
    #                 rightStop = True
    #                 if coordsInLoop.index((rightX, y)) > index:
    #                     print("right stop bad coord in loop")
    #                     rightStopBad = True
    #         leftX = x - i
    #         if leftX < 0 or leftStop == True:
    #             print(f"left hit end of grid: ({leftX}, {y})")
    #             leftStop = True
    #             leftStopBad = True
    #         else:
    #             # move to the left
    #             print("move to left")
    #             if grid[y][leftX] == ".":
    #                 leftSum += 1
    #                 leftCoords.append((leftX, y))
    #             if (leftX, y) in coordsInLoop:
    #                 print("left hit coord in loop")
    #                 leftStop = True
    #                 if coordsInLoop.index((leftX, y)) < index:
    #                     print("left stop bad coord in loop")
    #                     leftStopBad = True
    #         i += 1
    #     if leftStopBad and not rightStopBad:
    #         # if left stopped bad then count the right hand coords
    #         for c in rightCoords:
    #             grid[c[1]][c[0]] = "1"
    #         for c in leftCoords:
    #             grid[c[1]][c[0]] = "0"
    #         total += rightSum
    #     elif not leftStopBad and rightStopBad:
    #         for c in leftCoords:
    #             grid[c[1]][c[0]] = "1"
    #         for c in rightCoords:
    #             grid[c[1]][c[0]] = "0"
    #         total += leftSum
    #     # move up/down
    # print(total)

    for g in newGrid:
        print("\t".join(g))
    print("total: " + str(total))

    # print(steps // 2)
    # coordsInLoop = [(-3, -2), (-1, 4), (6, 1), (3, 10), (-4, 9), (-3, -2)]
    # coordsInLoop.append(coordsInLoop[0])
    # one = abs
    # # firstSum = 0
    # # secondSum = 0
    # # for index, coord in enumerate(coordsInLoop[:-1]):
    # #     # print(coord)
    # #     # if index != len(coordsInLoop) - 1:
    # #     print(coord[0] * coordsInLoop[index+1][1])
    # #     firstSum += coord[0] * coordsInLoop[index+1][1]
    # #     secondSum += coord[1] * coordsInLoop[index+1][0]
    # print()
    # print(firstSum)
    # # print()
    # print(secondSum)
    # print(firstSum - secondSum)
    # print()
    # print(coordsInLoop)
    # print(len(coordsInLoop))
    # print(abs(firstSum - secondSum) - len(coordsInLoop))
