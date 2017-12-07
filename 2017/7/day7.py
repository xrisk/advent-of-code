import sys
import re

children = {}
weights = {}
parents = {}

matcher = re.compile("(?P<name>\w+) \((?P<weight>\d+)\)")

for line in sys.stdin.read().splitlines():

    arrow = line.find("->")

    before = line[:arrow] if arrow != -1 else line
    m = matcher.search(before)
    name, weight = m.group('name'), m.group('weight')

    weights[name] = int(weight)
    if name not in children:
        children[name] = []
    if name not in parents:
        parents[name] = []

    if arrow != -1:
        after = line[arrow + 2:].split(", ")
        for node in after:
            node = node.strip()
            if node not in parents:
                parents[node] = []
            if name not in children:
                children[name] = []
            children[name].append(node)
            parents[node].append(name)

for node in parents:
    if len(parents[node]) == 0:
        root = node

print(root)
