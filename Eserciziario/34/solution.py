import json


def es34(fname1, fname2):
    quadrato = []
    with open(fname1, encoding='utf8') as f:
        quadrato = json.load(f)
    simboli = set(quadrato[0]).union(set(quadrato[1]))
    N = len(simboli)
    for line in quadrato:
        line.append((simboli-set(line)).pop())
    last = []
    for c in range(N):
        col = set(l[c] for l in quadrato)
        last.append((simboli-col).pop())
    quadrato.append(last)
    with open(fname2, mode='w', encoding='utf8') as f:
        json.dump(quadrato, f)
    return simboli
