# grid stuff

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
