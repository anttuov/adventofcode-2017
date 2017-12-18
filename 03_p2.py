# http://adventofcode.com/2017/day/3

import math
myin = 325489

w, h = 99, 99
values = [[0 for x in range(w)] for y in range(h)] 
values[0][0] = 1
x = 0
y = 0
inc = 1
incb = False
direction = 0


i = 0
found = False
while not found:
    for ii in range(inc):
        if direction == 0:
            x += 1
        if direction == 1:
            y += 1
        if direction == 2:
            x -= 1
        if direction == 3:
            y -= 1
        # print(x, y)
        value = 0
        for xx in range(-1,2):
            for yy in range(-1,2):
                try:
                    value = value + values[x+xx][y+yy]
                except:
                    pass
        print(value)
        if value > myin:
            found = True
            break
        values[x][y] = value

    if incb:
        inc += 1
        incb = False
    else:
        incb = True
    direction = (direction+1)%4
    i = 0

print("done:", value)
