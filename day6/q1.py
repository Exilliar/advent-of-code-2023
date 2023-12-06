def extractValues(line):
    returnArr = []
    tmp = line.split(":")[1].strip().split(" ")
    for t in tmp:
        if t != "":
            returnArr.append(int(t.strip()))
    return returnArr

def readInput(lines):
    timeDistance = []
    times = extractValues(lines[0])
    distance = extractValues(lines[1])
    for index, t in enumerate(times):
        timeDistance.append((t, distance[index]))
    return timeDistance

with open("input.txt", "r") as f:
    lines = list(f.readlines())
    timeDistance = readInput(lines)

    total = 1
    for td in timeDistance:
        winningTimes = 0
        for buildUpTime in range(1, td[0]):
            travelSpeed = buildUpTime
            travelDistance = travelSpeed * (td[0] - buildUpTime)
            if travelDistance > td[1]:
                winningTimes += 1
        if winningTimes != 0:
            total *= winningTimes
    print(total)
