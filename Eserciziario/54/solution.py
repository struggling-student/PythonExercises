import copy


def es54(lista):
    diz = {}
    for v in copy.copy(lista):
        if isinstance(v, str):
            lista.remove(v)
            if v in diz:
                diz[v] += 1
            else:
                diz[v] = 1
    return diz
