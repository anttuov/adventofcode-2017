def getmax(l):
    m = 0
    i = 0
    for index, val in enumerate(l):
        if val > m:
            m = val
            i = index
    return i


myin = "5	1	10	0	1	7	13	14	3	12	8	10	7	12	0	6"
blocks = list(map(int, myin.split("\t")))
blen = len(blocks)
count = 0
oldblocks = []
while True:
    count += 1
    index = getmax(blocks)
    value = blocks[index]
    oldblocks.append(blocks[:])
    blocks[index] = 0
    
    
    for i in range(value):
        index = (index + 1) % blen
        blocks[index] += 1

    if blocks in oldblocks:
        loopcount = oldblocks.index(blocks)
        break

print("done part 1: ", count)
print("done part 2: ", count-loopcount)