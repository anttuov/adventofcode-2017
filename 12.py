class Program:
    def __init__(self, name):
        self.name = str(name)
        self.links = []
        self.ingroup = False

    def __repr__(self):
        return "Prog_"+self.name

programs = []
for i in range(2000):
    programs.append(Program(i))

with open("12.txt") as f:
    for line in f:
        l = line.strip().split("<->")
        name = l[0].strip()
        links = map(int, l[1].strip().split(", "))
        programs[int(name)].links = [programs[int(name)] for name in links]

groups = []
groupcount = 0

for program in programs:
    if not program.ingroup:
        groups.append([program])
        program.ingroup = True
        a = 0
        while a < len(groups[groupcount]):
            for link in groups[groupcount][a].links:
                if link not in groups[groupcount]:
                    link.ingroup = True
                    groups[groupcount].append(link)
            a += 1
        groupcount += 1

print("done p1:", len(groups[0]))
print("done p2:", groupcount)