cardTypes = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}

types = {
    "5ooK": 7, # 5 of a kind
    "4ooK": 6, # 4 of a kind
    "fh": 5, # full house
    "3ooK": 4, # 3 of a kind
    "2p": 3, # 2 pair
    "1p": 2, # 1 pair
    "hk": 1 # high card
}

class Hand:
    def __init__(self, cards: str, bid: int):
        self.cards = [*cards]
        self.bid = bid
        self.score = self.calcScore()
        self.finalScore = 0

    def calcScore(self):
        cardsDic = {} # dictionary containing a count of how many types of each card
        for card in self.cards:
            if card in cardsDic:
                cardsDic[card] += 1
            else:
                cardsDic[card] = 1

        if len(dict((k, v) for k, v in cardsDic.items() if v == 5)) == 1:
            return types["5ooK"]
        elif len(dict((k, v) for k, v in cardsDic.items() if v == 4)) == 1:
            return types["4ooK"]
        elif len(dict((k, v) for k, v in cardsDic.items() if v == 2)) == 1 and len(dict((k, v) for k, v in cardsDic.items() if v == 3)) == 1:
            return types["fh"]
        elif len(dict((k, v) for k, v in cardsDic.items() if v == 3)) == 1:
            return types["3ooK"]
        elif len(dict((k, v) for k, v in cardsDic.items() if v == 2)) == 2:
            return types["2p"]
        elif len(dict((k, v) for k, v in cardsDic.items() if v == 2)) == 1:
            return types["1p"]
        else:
            return types["hk"]
    def __str__(self) -> str:
        return f"{str(self.cards)} - {str(self.bid)} - {str(self.score)} = {str(self.finalScore)}"

    def handWins(self, otherHand: object) -> bool:
        if self.score > otherHand.score:
            return True
        elif self.score < otherHand.score:
            return False
        else:
            for index, card in enumerate(self.cards):
                if cardTypes[card] > cardTypes[otherHand.cards[index]]:
                    return True
                elif cardTypes[card] < cardTypes[otherHand.cards[index]]:
                    return False

with open("input.txt", "r") as f:
    hands = []
    for line in f.readlines():
        cards = line.split(" ")[0]
        bid = int(line.split(" ")[1])
        hands.append(Hand(cards, bid))

    for x in range(len(hands)):
        for y in range(len(hands)):
            if x != y and hands[x].handWins(hands[y]):
                placeholder = hands[y]
                hands[y] = hands[x]
                hands[x] = placeholder

    total = 0
    for index, hand in enumerate(hands):
        hand.finalScore = hand.bid * (len(hands) - index)
        total += hand.bid * (len(hands) - index)
    print(total)

