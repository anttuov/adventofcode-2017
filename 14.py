import importlib
knot = importlib.import_module("10")

myin = "ljoxqyyw"


class Grid():
    def __init__(self, value):
        self.value = int(value)
        self.value2 = 0
        self.in_group = False
    def __repr__(self):
        return str("{:04}".format(self.value2))


def find_group(grid, x, y, groups):
    grid[x][y].in_group = True
    grid[x][y].value2 = groups
    if x+1 <= 127:
        if grid[x+1][y].value == 1 and not grid[x+1][y].in_group:
            find_group(grid, x+1, y, groups)

    if x-1 >= 0:
        if grid[x-1][y].value == 1 and not grid[x-1][y].in_group:
            find_group(grid, x-1, y, groups)

    if y+1 <= 127:
        if grid[x][y+1].value == 1 and not grid[x][y+1].in_group:
            find_group(grid, x, y+1, groups)

    if y-1 >= 0:
        if grid[x][y-1].value == 1 and not grid[x][y-1].in_group:
            find_group(grid, x, y-1, groups)


grid = [[0] * 128 for i in range(128)]

binary = []
for i in range(128):
    hashed = knot.knot_hash(f"{myin}-{i}")
    binary.append("".join(["{:04b}".format(int(c, 16)) for c in hashed]))
    x = 0
    for c in binary[i]:
        grid[x][i] = Grid(c)
        x += 1

groups = 0
for y in range(128):
    for x in range(128):
        if grid[x][y].value == 1 and not grid[x][y].in_group:
            groups += 1
            find_group(grid, x, y, groups)

print("done p1:", "".join(binary).count("1"))
print("done p2:", groups)
