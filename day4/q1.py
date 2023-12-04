with open("input.txt", "r") as f:
    total = 0
    for line in f.readlines():
        line = line.strip()
        gameTotal = 0
        numbers = line.split(": ")[1]
        winningNumbers = numbers.split(" | ")[0].split(" ")
        userNumbers = numbers.split(" | ")[1].split(" ")

        for userNumber in userNumbers:
            for winningNumber in winningNumbers:
                if userNumber != "" and userNumber == winningNumber:
                    if gameTotal == 0:
                        gameTotal = 1
                    else:
                        gameTotal *= 2
        total += gameTotal
    print("total: " + str(total))
