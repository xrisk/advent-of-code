adj = {}
sol = {}

symbols = {
            "AND": " & ",
            "OR": " | ",
            "NOT": " ~ ",
            "LSHIFT": " << ",
            "RSHIFT": " >> "
}

try:
    while True:
        l, r = raw_input().split(' -> ')
        deps = filter(lambda x: not(x in symbols or x.isdigit()), l.split(' '))
        adj[r] = deps
        sol[r] = l

except EOFError:

    inorder = []
    v = []

    def dfs(s):
        if s not in v:
            for i in adj[s]:
                    dfs(i)
        v.append(s)
        inorder.append(s)

    for i in adj.keys():
        dfs(i)

    for i in inorder:
        t = str(sol[i]).split(' ')
        for j in range(0, len(t)):
            if t[j].isalpha() and t[j] not in symbols:
                t[j] = str(sol[t[j]])
        t = ' '.join(t)
        for _ in symbols:
            t = t.replace(_, symbols[_])
        sol[i] = eval(t)

    print sol['a']
