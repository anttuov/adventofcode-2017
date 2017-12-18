def check_caught(layers, depth, delay=0):
    severity = 0
    caught = False
    try:
        a = (depth+delay) / (layers[depth] - 1)
        if int(a) % 2 == 0:
            if (depth+delay) % (layers[depth]-1) == 0:
                severity = layers[depth]*depth
                caught = True
    except:
        pass
    return [caught, severity]

layers = {}
with open("inputs/13.txt") as f:
    for line in f:
        l = line.strip().split(": ")
        maxdepth = int(l[0])
        layers[int(l[0])] = int(l[1])

depth = 0
severity = 0
while depth <= maxdepth:
    if check_caught(layers, depth)[0]:
        severity += check_caught(layers, depth)[1]
    depth += 1

print("done p1:", severity)

depth = 0
step = 0
caught = True
print("calculating p2...")

while caught:
    depth = 0
    caught = False

    while depth <= maxdepth:
        if check_caught(layers, depth, step)[0]:
            caught = True
            break

        depth += 1
    step += 1

print("done p2:", step-1)