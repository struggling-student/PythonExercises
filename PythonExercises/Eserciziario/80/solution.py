import os


def es80(dir1, parole):
    return es80bis(dir1, parole, 0)


def es80bis(dir1, parole, level=0):
    diz = {p: [0, 0] for p in parole}
    for fn in os.listdir(dir1):
        filename = dir1 + "/" + fn
        if os.path.isdir(filename):
            for p, [n, l] in es80bis(filename, parole, level+1).items():
                diz[p][0] += n
                diz[p][1] = max(diz[p][1], l)
        elif fn[-4:] == '.txt':
            with open(filename, encoding='utf8') as f:
                words = f.read().split()
                for w in words:
                    if w in parole:
                        diz[w][0] += 1
                        diz[w][1] = level
    return {k: v for k, v in diz.items() if v[0]}
