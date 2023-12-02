with open("input.txt", "r") as f:
    total = 0
    for line in f.readlines():
        cubeColors = {
            "red": 1,
            "green": 1,
            "blue": 1
        }

        colonSplitted = line.split(":")
        gameNum = int(colonSplitted[0].split(" ")[1])

        rounds = colonSplitted[1].strip().split("; ")
        for round in rounds:
            cubes = round.split(", ")
            for cube in cubes:
                splitted = cube.split(" ")
                number = int(splitted[0])
                color = splitted[1]
                if cubeColors[color] < number:
                    cubeColors[color] = number

        power = cubeColors["red"] * cubeColors["blue"] * cubeColors["green"]
        total += power
    print("total: " + str(total))
