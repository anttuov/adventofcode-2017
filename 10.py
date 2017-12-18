def circlist(clist, pos, clen):
    if pos+clen > len(clist):
        plen = clen - (len(clist) - pos)
        sublist = clist[pos:] + clist[:plen]
        sublist = sublist[::-1]
        clist[pos:] = sublist[:len(clist[pos:])]
        clist[:plen] = sublist[len(clist[pos:]):]
    else:
        sublist = clist[pos:pos+clen]
        sublist = sublist[::-1]
        clist[pos:pos+clen] = sublist
    return clist

def knot_hash(myin):
    asciilens = [ord(c) for c in myin] + [17, 31, 73, 47, 23]

    l = list(range(256))
    pos = 0
    skip = 0
    for i in range(64):
        for length in asciilens:
            l = circlist(l, pos, length)
            pos = (pos + length + skip) % len(l)
            skip += 1

    dense = []
    value = 0
    count = 0
    for val in l:
        value = value ^ val
        count += 1
        if count == 16:
            count = 0
            dense.append(value)
            value = 0
    return "".join(["{:02x}".format(val) for val in dense])

if __name__ == "__main__":
    myin = "46,41,212,83,1,255,157,65,139,52,39,254,2,86,0,204"
    lengths = map(int, myin.split(","))
    l = list(range(256))

    pos = 0
    skip = 0
    for length in lengths:
        l = circlist(l, pos, length)
        pos = (pos + length + skip) % len(l)
        skip += 1

    print("done p1:", l[0]*l[1])

    print("done p2:", knot_hash(myin))