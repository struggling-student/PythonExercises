

def es64(l):
    m = max(l)
    rows = len(str(m))
    ls = ["{:{r}}".format(n, r=rows) for n in l]
    ris = "\n".join(" ".join([n[i] for n in ls]) for i in range(rows))
    return ris
