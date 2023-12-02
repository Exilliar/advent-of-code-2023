maxCubes = {
    "red": 12,
    "green": 13,
    "blue": 14
}

with open("input.txt", "r") as f:
    total = 0
    for line in f.readlines():
        gamePass = True
        colonSplitted = line.split(":")
        gameNum = int(colonSplitted[0].split(" ")[1])

        rounds = colonSplitted[1].strip().split("; ")
        for round in rounds:
            cubes = round.split(", ")
            for cube in cubes:
                splitted = cube.split(" ")
                number = int(splitted[0])
                color = splitted[1]
                if maxCubes[color] < number:
                    gamePass = False

        if gamePass == True:
            total += gameNum
    print("total: " + str(total))