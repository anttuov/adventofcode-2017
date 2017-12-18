with open("inputs/9.txt") as f:
    stream = f.read()

a = 0
while a < len(stream):
    if stream[a] == "!":
        stream = stream[:a] + stream[(a+2):] 
        a -= 1
    a += 1

a = 0
state = "START"
garbage = 0
while a < len(stream):
    if stream[a] == "<" and state == "START":
        start = a
        state = "END"
    elif stream[a] == ">" and state == "END":
        garbage += (a - start - 1)
        if stream[a+1] == ",":
            a += 1
        if stream[start-1] == ",":
            start -= 1

        stream = stream[:start] + stream[(a+1):]
        state = "START"
        a = start-1
    a += 1


totalscore = 0

while len(stream) > 0:
    if stream == "{}":
        totalscore += 1
        break
    a = 0
    score = 0
    while a < len(stream):

        if stream[a] == "{":
            score += 1
        if stream[a] == "}":
            score -= 1

        if stream[a:a+2] == "{}":
            totalscore += score
            score -= 1

            stream = stream[:a] + stream[(a+2):]

            if stream[a] == ",":
                stream = stream[:a] + stream[(a+1):]

            elif stream[a-1] == ",":
                stream = stream[:(a-1)] + stream[a:]
                a -= 1

            if stream[a] == ",":
                stream = stream[:a] + stream[(a+1):]
            a -= 1
        a += 1

    # print(stream, stream.count("{"), stream.count("}"), totalscore)
print("done p1:", totalscore)
print("done p2:", garbage)