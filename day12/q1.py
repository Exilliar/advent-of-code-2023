import time

def draw(number: int, remainingNumbers: list, newLines: list, newLinesPos: int, startPos: int, maxLength: int):
    newLine = newLines[newLinesPos]
    saveCurr = newLine.copy()
    if startPos > len(newLine):
        while startPos > len(newLines[newLinesPos]):
            newLine.append(".")
    for i in range(0, number):
        newLine.append("#")
    if len(newLine) < maxLength:
        newLine.append(".")
    else:
        return newLine
    if len(remainingNumbers) == 0:
        if len(newLine) <= maxLength:
            newLines.append(saveCurr)
            return draw(number, remainingNumbers, newLines, newLinesPos + 1, startPos + 1, maxLength)
        else:
            return newLines
    else:
        draw(remainingNumbers[0], remainingNumbers[1:], newLines, newLinesPos, len(newLine), maxLength)
        if len(saveCurr) + sum(remainingNumbers) + len(remainingNumbers) + number <= maxLength:
            newLines.append(saveCurr)
            draw(number, remainingNumbers, newLines, len(newLines) - 1, startPos + 1, maxLength)
        return newLines

def validCheck(toCheck: list, line: list, numbersSum: int):
    if len(toCheck) != len(line):
        return False
    else:
        toCheckNumHashes = 0
        for i, l in enumerate(toCheck):
            if l == "#":
                toCheckNumHashes += 1
            lineL = line[i]
            if lineL == "#" and l != "#":
                return False
            if lineL == "." and l != ".":
                return False
        if toCheckNumHashes == numbersSum:
            return True
        else:
            return False

with open("input.txt", "r") as f:
    startTime = time.perf_counter()
    totaltotal = 0
    for line in f.readlines():
        line = line.strip()
        field = [*line.split(" ")[0]]
        numbers = [int(l) for l in line.split(" ")[1].split(",")]

        newLines = [[]]

        draw(numbers[0], numbers[1:], newLines, 0, 0, len(field))

        # print()
        # print(line)
        for newLine in newLines:
            if len(newLine) < len(field):
                while len(newLine) < len(field):
                    newLine.append(".")
            # print(newLine)
        total = 0
        valids = []
        for line in newLines:
            if validCheck(line, field, sum(numbers)):
                valids.append(line)
                total += 1
        # print(f"total: {total}")
        totaltotal += total
    print(totaltotal)
    endTime = time.perf_counter()
    print(f"time: {endTime - startTime}")
