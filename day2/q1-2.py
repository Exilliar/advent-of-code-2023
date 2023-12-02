# different way of doing q1, using regex, results are the same as from q1.py

import re

maxCubes = {
    "red": 12,
    "green": 13,
    "blue": 14
}

with open("input.txt", "r") as f:
    total = 0
    for line in f.readlines():
        splitted = re.split(": |, |; ", line.strip())
        gameId = 0
        gamePass = True
        for split in splitted:
            spaces = split.split(" ")
            if spaces[0] == "Game":
                gameId = int(spaces[1])
            else:
                number = int(spaces[0])
                color = spaces[1]
                if maxCubes[color] < number:
                    gamePass = False
        if gamePass == True:
            total += gameId
    print("total: " + str(total))
