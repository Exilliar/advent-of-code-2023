numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

with open("input.txt", "r") as f:
    sum = 0
    for line in f.readlines():
        first = ""
        last = ""
        for char in line:
            if char in numbers:
                if first == "":
                    first = char
                last = char
        sum += int(first+last)
    print("sum: " + str(sum))
