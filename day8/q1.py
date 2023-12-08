class Node:
    def __init__(self, name: str) -> None:
        self.name = name
        self.left = None
        self.right = None

    def __str__(self):
        return f"{self.name} - ({self.left.name}, {self.right.name})"

with open("input.txt", "r") as f:
    lines = list(f.readlines())
    instructions = [*lines[0].strip()]
    nodes = {}

    currLine = 2

    while currLine < len(lines):
        name = lines[currLine].strip().split(" = ")[0]
        nodes[name] = Node(name)
        currLine += 1

    currLine = 2
    while currLine < len(lines):
        name = lines[currLine].split(" = ")[0]
        leftRight = lines[currLine].strip().split(" = ")[1].replace("(", "").replace(")", "").split(", ")
        leftName = leftRight[0]
        rightName = leftRight[1]
        leftNode = nodes[leftName]
        rightNode = nodes[rightName]
        nodes[name].left = leftNode
        nodes[name].right = rightNode
        currLine += 1

    currentNode = nodes["AAA"]
    instructionNum = 0
    steps = 0

    while currentNode.name != "ZZZ":
        steps += 1
        currInstruction = instructions[instructionNum]

        if currInstruction == "L":
            currentNode = currentNode.left
        elif currInstruction == "R":
            currentNode = currentNode.right

        if instructionNum == len(instructions) - 1:
            instructionNum = 0
        else:
            instructionNum += 1
    print("steps: " + str(steps))
