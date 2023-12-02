import re

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
numberNames = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "zero": "0",
}

with open("input.txt", "r") as f:
    sum = 0
    for line in f.readlines():
        first = ""
        last = ""
        for index, char in enumerate(line):
            search = re.search("^(one|two|three|four|five|six|seven|eight|nine|zero)", line[index:])
            if char in numbers:
                if first == "":
                    first = char
                last = char
            elif search != None and search.group() in numberNames:
                if first == "":
                    first = numberNames[search.group()]
                last = numberNames[search.group()]
        sum += int(first+last)
    print("sum: " + str(sum))
