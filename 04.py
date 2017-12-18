# http://adventofcode.com/2017/day/4

def check_pass(words):
    while len(words) > 1:
        word = words.pop()
        if word in words:
            return False
    return True


valids = [0, 0]
with open("inputs/4.txt") as f:
    for line in f:
        if check_pass(line.strip().split(" ")):
            valids[0] += 1
        if check_pass([''.join(sorted(w)) for w in line.strip().split(" ")]):
            valids[1] += 1
print("done:", valids)

