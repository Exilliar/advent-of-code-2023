savedResults = {}
numberSaves = {}
startPosSaves = {}
remainingNumbersSave = {}

import time

def draw(number: int, remainingNumbers: list, newLines: list, newLinesPos: int, startPos: int, maxLength: int, field: list, numbersSum: int):
    newLine = newLines[newLinesPos]
    saveCurr = newLine.copy()
    # if not partialValid(newLine, field):
    #     return newLines

    cacheName = str(startPos - len(newLines[newLinesPos]))
    if cacheName not in startPosSaves:
        toSave = []
        if startPos > len(newLine):
            while startPos > len(newLines[newLinesPos]):
                newLine.append(".")
                toSave.append(".")
        startPosSaves[cacheName] = toSave
    else:
        # print(f"hit1 {cacheName}")
        newLine += startPosSaves[cacheName]

    toSave = []
    cacheName = str(number)
    if cacheName not in numberSaves:
        for i in range(0, number):
            newLine.append("#")
            toSave.append("#")
        numberSaves[cacheName] = toSave
    else:
        # print(f"hit2: {cacheName}")
        newLine += numberSaves[cacheName]

    if len(newLine) < maxLength:
        newLine.append(".")
    else:
        return newLine
    if len(remainingNumbers) == 0:
        if len(newLine) <= maxLength:
            newLines.append(saveCurr)
            return draw(number, remainingNumbers, newLines, newLinesPos + 1, startPos + 1, maxLength, field, numbersSum)
        else:
            return newLines
    else:
        cacheName = str(number) + "," + ",".join([str(n) for n in remainingNumbers]) + "-" + str(maxLength - startPos + 1)
        if cacheName not in remainingNumbersSave:
            draw(remainingNumbers[0], remainingNumbers[1:], newLines, newLinesPos, len(newLine), maxLength, field, numbersSum)
            if len(saveCurr) + sum(remainingNumbers) + len(remainingNumbers) + number <= maxLength:
                newLines.append(saveCurr)
                draw(number, remainingNumbers, newLines, len(newLines) - 1, startPos + 1, maxLength, field, numbersSum)

            toSave = []
            tmpNewLines = newLines.copy()
            for i in range(newLinesPos, len(tmpNewLines)):
                toSave.append(tmpNewLines[i][startPos:])
                # toSave.append(newLines[i])
            # print(f"add {cacheName}")
            remainingNumbersSave[cacheName] = toSave
            return newLines
        else:
            # print(f"hit: {cacheName}")
            res = remainingNumbersSave[cacheName]
            # toAdd = []
            # print()
            for r in res:
                # print(len(saveCurr) + len(r))
                # print(r)
                # if len(saveCurr) + len(r) <= maxLength and validCheck(saveCurr + r, field, numbersSum):
                # print(f"add: {saveCurr + r}")
                newLines.append(saveCurr + r)
                # else:
                #     print("don't add")
            # print(newLines)
            return newLines
            

def partialValid(toCheck: list, line: list):
    if len(toCheck) == 0:
        return True
    if len(toCheck) > len(line):
        return False
    for i, l in enumerate(toCheck):
        lineL = line[i]
        if lineL == "#" and l != "#":
            return False
        if lineL == "." and l != ".":
            return False
    return True

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

def expandLine(line: str):
    expandBy = 5
    field = line.split(" ")[0]
    numbers = line.split(" ")[1]
    newNumbers = numbers
    newField = field
    for i in range(0, expandBy - 1):
        newField += "?" + field
        newNumbers += "," + numbers
    return [*newField], [int(l) for l in newNumbers.split(",")]

# print(expandLine("???.### 1,1,3"))

with open("input.txt", "r") as f:
    startTime = time.perf_counter()
    # fieldNumbers = [] # (field, numbers)
    # for line in f.readlines():
    #     field, numbers = expandLine(line)
    #     fieldNumbers.append((field, numbers))
    # print(fieldNumbers)
    # groups = {}
    # for fn in fieldNumbers:
    #     groupName = "".join([str(f) for f in fn[1]])
    #     if groupName in groups:
    #         groups[groupName].append(fn)
    #     else:
    #         groups[groupName] = [fn]
    # print(len(groups))
        
    # for fieldNumbers
    totaltotal = 0
    for i, line in enumerate(f.readlines()):
        line = line.strip()

        field, numbers = expandLine(line)
        field = [*line.split(" ")[0]]
        numbers = [int(l) for l in line.split(" ")[1].split(",")]
        # print(f"{i+1} line: {''.join(field)} {','.join([str(number) for number in numbers])}")

        newLines = [[]]

        draw(numbers[0], numbers[1:], newLines, 0, 0, len(field), field, sum(numbers))

        print()
        print(line)
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
        print(f"total: {total}")
        totaltotal += total
    print(totaltotal)
    endTime = time.perf_counter()
    print(f"time: {endTime - startTime}")
    # print(remainingNumbersSave)
