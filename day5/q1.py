def handleTransition(seeds, currLine):
    skip = []
    while currLine < len(lines) and lines[currLine].strip() != "":
        line = lines[currLine].strip()
        if line[0].isdigit():
            numbers = line.split(" ")
            destinationRange = int(numbers[0])
            sourceRange = int(numbers[1])
            rangeLength = int(numbers[2])
            for index, seed in enumerate(seeds):
                seedCheck = seed
                possibleRangeMax = sourceRange + rangeLength
                if seedCheck >= sourceRange and seedCheck < possibleRangeMax:
                    diff = destinationRange - sourceRange
                    destinationNum = seedCheck + diff
                    if index not in skip:
                        seeds[index] = destinationNum
                        skip.append(index)
        currLine += 1

    return currLine

with open("input.txt", "r") as f:
    lines = list(f.readlines())
    seedsLine = lines[0]
    seedsList = seedsLine.split(": ")[1].split(" ")
    seeds = []
    i = 0
    for seed in seedsList:
        seeds.append(int(seed.strip()))

    currLine = 2

    seedsLength = 2
    while seedsLength != 9:
        currLine = handleTransition(seeds, currLine)
        currLine += 1
        seedsLength += 1

    minSeed = -1
    for seed in seeds:
        finalVal = seed
        if minSeed == -1:
            minSeed = finalVal
        elif minSeed > finalVal:
            minSeed = finalVal
    print("minSeed: " + str(minSeed))
