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


def weight_at_subtree(node):
    child_weights = [(weight_at_subtree(n), n) for n in children[node]]

    if len(child_weights) == 0: # leaf
        return weights[node]

    child_weights.sort()

    expected = child_weights[1][0]

    if sum((w[0] for w in child_weights)) != expected * len(child_weights):
        to_adjust = 0
        if child_weights[0][0] != expected:
            to_adjust = 0
        else:
            to_adjust = len(child_weights) - 1
        diff = expected - child_weights[to_adjust][0]
        print(diff + weights[child_weights[to_adjust][1]])

    return weights[node] + expected * len(child_weights)


weight_at_subtree(root)




