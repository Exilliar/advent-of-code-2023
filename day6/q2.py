with open("input.txt", "r") as f:
    lines = list(f.readlines())
    time = int(lines[0].split(":")[1].replace(" ", ""))
    distance = int(lines[1].split(":")[1].replace(" ", ""))

    winningTimes = 0
    for buildUpTime in range(1, time):
        travelSpeed = buildUpTime
        travelDistance = travelSpeed * (time - buildUpTime)
        if travelDistance > distance:
            winningTimes += 1
    print(winningTimes)
