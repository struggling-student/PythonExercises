
def es79(lista):
    a = b = 0
    ins = set()
    for s in lista:
        if type(s) == type([]):
            x, y, l = es79(s)
            a += x
            b += y
            ins = ins | set(l)
        else:
            a += 1
            b += s
            ins.add(s)
    lista.reverse()
    lista1 = sorted(list(ins))
    return (a, b, lista1)
