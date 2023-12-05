def handleTransition(seeds, currLine):
    newSeeds = []
    firstLine = True
    seedsToCheckNext = []
    currLine += 1
    while currLine < len(lines) and lines[currLine].strip() != "":
        line = lines[currLine].strip()
        seedsToCheck = []
        if firstLine == True:
            seedsToCheck = seeds
            firstLine = False
        else:
            for seed in seedsToCheckNext:
                seedsToCheck.append(seed)
            seedsToCheckNext = []
        numbers = line.split(" ")
        destinationRange = int(numbers[0])
        sourceRange = int(numbers[1])
        rangeLength = int(numbers[2])
        diff = destinationRange - sourceRange
        for seed in seedsToCheck:
            seedLow = seed[0]
            seedHigh = seed[1]
            possibleRangeMax = sourceRange + rangeLength - 1
            if seedLow >= sourceRange and seedHigh <= possibleRangeMax:
                newSeeds.append((seedLow + diff, seedHigh + diff))
                if seedLow < sourceRange:
                    seedsToCheckNext.append((seedLow, sourceRange - 1))
                if seedHigh > possibleRangeMax:
                    seedsToCheckNext.append((possibleRangeMax + 1, seedHigh))
            elif seedLow < sourceRange and seedHigh > possibleRangeMax:
                newSeeds.append((sourceRange+diff, possibleRangeMax+diff))
                seedsToCheckNext.append((seedLow, sourceRange - 1))
                seedsToCheckNext.append((possibleRangeMax + 1, seedHigh))
            elif seedLow >= sourceRange and seedLow <= possibleRangeMax and seedHigh >= possibleRangeMax:
                newSeeds.append((seedLow + diff, possibleRangeMax + diff))
                seedsToCheckNext.append((possibleRangeMax+1, seedHigh))
            elif seedLow <= sourceRange and seedHigh >= sourceRange and seedHigh <= possibleRangeMax:
                newSeeds.append((sourceRange + diff, seedHigh + diff))
                seedsToCheckNext.append((seedLow, sourceRange - 1))
            else:
                seedsToCheckNext.append(seed)
        currLine += 1

    for seed in seedsToCheckNext:
        newSeeds.append(seed)

    return currLine, newSeeds

with open("input.txt", "r") as f:
    lines = list(f.readlines())
    seedsLine = lines[0]
    seedsList = seedsLine.split(": ")[1].split(" ")
    seeds = [] # (startRange, endRange)[]
    i = 0
    while i < len(seedsList):
        seed = (int(seedsList[i]), int(seedsList[i]) + int(seedsList[i+1]) - 1)
        seeds.append(seed)
        i += 2

    currLine = 2

    seedsLength = 2
    while seedsLength != 9:
        currLine, seeds = handleTransition(seeds, currLine)
        currLine += 1
        seedsLength += 1

    minSeed = -1
    for seed in seeds:
        finalVal = seed[0]
        if minSeed == -1:
            minSeed = finalVal
        elif minSeed > finalVal:
            minSeed = finalVal
    print("minSeed: " + str(minSeed))
