import json


def es32(fname1):
    stringhe = []
    with open(fname1, encoding='utf8') as f:
        stringhe = json.load(f)
    lista = []
    for stringa in stringhe:
        pari = dispari = 0
        for c in stringa:
            if c in '13579':
                dispari += ord(c)-ord('0')
            else:
                pari += ord(c) - ord('0')
        lista.append((dispari, pari))
    return lista
