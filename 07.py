import statistics

class ProgramTree:
    def __init__(self, name, weight):
        self.name = name
        self.weight = int(weight)
        self.children = []
        self.is_child = False

    def add_child(self, child):
        self.children.append(child)

    def total_weight(self):
        tw = self.weight
        if len(self.children) > 0:
            for c in self.children:
                tw += c.total_weight()
        return tw

    def __str__(self):
        return "{}, {}, {}, {}".format(self.name, self.weight, self.children, self.is_child)

    def __repr__(self):
        return self.name

programs = {}
children = {}

with open("inputs/7.txt") as f:
    for line in f:
        l = line.split("->")
        name = l[0].split("(")[0][:-1]
        weight = l[0].split("(")[1].strip()[:-1]
        programs[name] = ProgramTree(name, weight)
        if len(l) == 2:
            children[name] = l[1].strip().split(", ")

for name in children:
    for c in children[name]:
        programs[c].is_child = True
        programs[name].add_child(programs[c])

for prog in programs.values():
    if not prog.is_child and len(prog.children) > 0:
        base = prog.name
        break

print("done p1:", base)

stop = False
while not stop:
    weights = []
    stop = True
    for c in programs[base].children:
        weights.append(c.total_weight())

    for w in weights:
        if w != statistics.median(weights):
            prevw = statistics.median(weights)
            base = programs[base].children[weights.index(w)].name
            stop = False
            break

print("done p2:", int(programs[base].weight - (programs[base].total_weight() - prevw)))
