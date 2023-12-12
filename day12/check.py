with open("out.txt", "r") as o:
    with open("out-1.txt") as o1:
        totalWrong = 0
        o1Lines = list(o1.readlines())
        for i, line in enumerate(o.readlines()):
            if "total" in line:
                o1Total = int(o1Lines[i].strip().split(" ")[1])
                oTotal = int(line.strip().split(" ")[1])
                if o1Total != oTotal:
                    print(f"out.txt: {line.strip()}, out-1.txt: {o1Lines[i].strip()}, line: {i+1}")
                    totalWrong += 1
        print(f"total wrong: {totalWrong}")