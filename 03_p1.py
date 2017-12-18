# http://adventofcode.com/2017/day/3

import math
myin = 325489

layer = int(math.sqrt(myin-1)+1)
if layer % 2 == 0:
    layer += 1
squares = layer**2 - (layer-2)**2
startsq = ((layer-2)**2)+1
myin_pos = layer**2 - myin

y = int((-(layer-1)/2)+1)
x = int(((layer-1)/2))
print(layer, squares, myin_pos, startsq, x, y)

yinc = 1
xinc = 0

for i in range(squares):
    #print(startsq+i, x, y)
    if startsq+i == myin:
        xsel = x
        ysel = y
    x += xinc
    y += yinc
    if i+2 >= squares/4:
        yinc = 0
        xinc = -1
    if i+2 >= 2*squares/4:
        yinc = -1
        xinc = 0
    if i+2 >= 3*squares/4:
        yinc = 0
        xinc = 1
    
#print(xsel, ysel)
steps = abs(xsel)+abs(ysel)
print("done:",steps)