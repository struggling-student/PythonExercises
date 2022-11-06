

def es60(ftesto, ftestoMod):
    matrice = []
    with open(ftesto) as fIn:
        for line in fIn:
            numeri = list(map(int, line.split()))
            matrice.append(numeri)
    w = len(matrice[0])
    h = len(matrice)
    numdispari = 0
    for c in range(w):
        countdispari = 0
        for r in range(h):
            countdispari += matrice[r][c] % 2
        if countdispari > h-countdispari:
            numdispari += 1
            for r in range(h):
                matrice[r][c] = 0
    with open(ftestoMod, mode='w') as fOut:
        fOut.write('\n'.join(' '.join(map(str, linea)) for linea in matrice))
    return numdispari
