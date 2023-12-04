with open("input.txt", "r") as f:
    cards = {
        "1": 1
    }
    shouldContinue = True
    total = 0
    for line in f.readlines():
        line = line.strip()
        cardNumber = int(line.split(": ")[0].replace("Card", "").strip())
        if str(cardNumber) not in cards:
            cards[str(cardNumber)] = 1
        if shouldContinue == True:
            gameTotal = 0
            numbers = line.split(": ")[1]
            winningNumbers = numbers.split(" | ")[0].split(" ")
            userNumbers = numbers.split(" | ")[1].split(" ")

            for userNumber in userNumbers:
                for winningNumber in winningNumbers:
                    if userNumber != "" and userNumber == winningNumber:
                        gameTotal += 1
            copiesOfCard = cards[str(cardNumber)]
            if gameTotal != 0:
                for i in range(gameTotal):
                    card = str(cardNumber + i + 1)
                    if card not in cards:
                        cards[card] = 1
                    cards[card] += copiesOfCard
            else:
                if copiesOfCard == 1:
                    shouldContinue = False
        else:
            if str(cardNumber) not in cards:
                cards[str(cardNumber)] = 1

    totalList = []
    for c in cards:
        totalList.append(cards[c])
    total = sum(totalList)
    print("total: " + str(total))
