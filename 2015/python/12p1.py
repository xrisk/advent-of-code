import json
d = json.load(open('inp.in'))
c = 0


def walk(node):
    if isinstance(node, list):
        for i in node:
            walk(i)
    elif isinstance(node, dict):
        for key in node:
            walk(key)
            walk(node[key])
    elif isinstance(node, int):
        global c
        c += node

walk(d)
print c
