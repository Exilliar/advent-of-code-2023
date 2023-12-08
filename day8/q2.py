import math

class Node:
    def __init__(self, name: str) -> None:
        self.name = name
        self.left = None
        self.right = None

    def __str__(self):
        return f"{self.name} - ({self.left.name}, {self.right.name})"

def checkNodes(nodes):
    for node in nodes:
        if "Z" not in node.name:
            return False
    return True

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

def calcAnswer(answers: list):
    if len(answers) > 2:
        return lcm(answers[0], calcAnswer(answers[1:]))
    else:
        return lcm(answers[0], answers[1])

with open("input.txt", "r") as f:
    lines = list(f.readlines())
    instructions = [*lines[0].strip()]
    nodes = {}
    startingNodes = []

    currLine = 2

    while currLine < len(lines):
        name = lines[currLine].strip().split(" = ")[0]
        node = Node(name)
        nodes[name] = node
        if "A" in name:
            startingNodes.append(node)
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

    currentNodes = startingNodes
    answers = []

    for currentNode in currentNodes:
        instructionNum = 0
        steps = 0
        while "Z" not in currentNode.name:
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
        answers.append(steps)

    answer = calcAnswer(answers)
    print("steps: " + str(answer))
