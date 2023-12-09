def calcLineDifferences(line: list, calcedLines: list, iteration: int):
    allZeroes = True
    i = 0
    while i < len(line) - 1:
        diff = int(line[i+1]) - int(line[i])
        calcedLines[iteration].append(diff)
        if diff != 0:
            allZeroes = False
        i += 1
    if not allZeroes:
        calcedLines.append([])
        return calcLineDifferences(calcedLines[iteration], calcedLines, iteration + 1)
    else:
        return calcedLines


with open("input.txt", "r") as f:
    total = 0
    for line in f.readlines():
        line = line.strip()
        line = [int(l) for l in line.split(" ")]
        rows = calcLineDifferences(line, [line, []], 1)

        oldVal = 0
        i = len(rows) - 2
        while i >= 0:
            oldVal = rows[i][0] - oldVal
            i -= 1
        total += oldVal
    print("total: " + str(total))
