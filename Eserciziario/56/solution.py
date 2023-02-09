

def es56(tabella):
    counts = {}
    mc = 0
    for r in tabella:
        for v in r:
            if v in counts:
                counts[v] += 1
            else:
                counts[v] = 1
            mc = max(mc, counts[v])
    maxxes = []
    for k, v in counts.items():
        if v == mc:
            maxxes.append(k)
    for r in tabella:
        for i, v in enumerate(r):
            if v in maxxes:
                r[i] = '*'
    maxxes.sort()
    return maxxes
