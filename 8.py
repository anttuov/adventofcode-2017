from collections import defaultdict
registers = defaultdict(int)

maxval = 0
with open("8.txt") as f:
    for line in f:
        l = line.strip().split("if")
        cline = l[1].strip().split(" ")
        cline[2] = int(cline[2])
        cond = cline[1]

        c1 = registers[cline[0]] > cline[2] and cline[1] == ">"
        c2 = registers[cline[0]] < cline[2] and cline[1] == "<"
        c3 = registers[cline[0]] >= cline[2] and cline[1] == ">="
        c4 = registers[cline[0]] == cline[2] and cline[1] == "=="
        c5 = registers[cline[0]] <= cline[2] and cline[1] == "<="
        c6 = registers[cline[0]] != cline[2] and cline[1] == "!="

        if c1 or c2 or c3 or c4 or c5 or c6:
            oline = l[0].strip().split(" ")
            oline[2] = int(oline[2])
            if oline[1] == "dec":
                oline[2] = -oline[2]
            registers[oline[0]] += oline[2]
            if registers[oline[0]] > maxval:
                maxval = registers[oline[0]]

print("done p1:", sorted(registers.values(), reverse=True)[0])
print("done p2:", maxval)