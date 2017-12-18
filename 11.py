with open("11.txt") as f:
    myin = f.read()
directions = myin.strip().split(",")

x = 0
y = 0
movement = {"n": [0, -1], "ne": [1, -1], "se": [1, 0], "s": [0, 1], "sw": [-1, 1], "nw": [-1, 0]}
maxsteps = 0
for d in directions:
    x += movement[d][0]
    y += movement[d][1]
    if maxsteps < max(abs(x), abs(y)):
        maxsteps = max(abs(x), abs(y))

print("done p1:", max(abs(x), abs(y)))
print("done p2:", maxsteps)
