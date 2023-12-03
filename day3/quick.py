numbers = ["0","1","2","3","4","5","6","7","8","9"]

with open("input.txt", "r") as f:
    specials = []
    for line in f.readlines():
        for c in line.strip():
            if c not in numbers and c != "." and c not in specials:
                specials.append(c)
    print(specials)
