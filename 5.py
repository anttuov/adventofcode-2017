def jumps(lines, part2):
    a = 0
    steps = 0
    while a < len(lines):
        val = lines[a]
        if part2 and val > 2:
            lines[a] = lines[a] - 1
        else:
            lines[a] += 1
        a += val
        steps += 1

    return steps

lines = []
with open("5.txt") as f:
    for line in f:
        lines.append(int(line.strip()))


print("done p1:", jumps(lines[:], False))
print("done p2:", jumps(lines[:], True))

