

def es61(ftesto, op, sel):
    matrice = []
    with open(ftesto) as fIn:
        for line in fIn:
            matrice.append(list(map(int, line.split())))
    l = len(matrice)
    resM = []
    resm = []
    ress = []
    if sel == 'row':
        for row in matrice:
            M = m = row[0]
            s = 0
            for v in row:
                M = max(M, v)
                m = min(m, v)
                s += v
            resM.append(M)
            resm.append(m)
            ress.append(s)
    elif sel == 'col':
        for c in range(l):
            M = m = matrice[0][c]
            s = 0
            for r in range(l):
                v = matrice[r][c]
                M = max(M, v)
                m = min(m, v)
                s += v
            resM.append(M)
            resm.append(m)
            ress.append(s)
    elif sel == 'dp':
        M = m = matrice[0][0]
        s = 0
        for c in range(l):
            v = matrice[c][c]
            M = max(M, v)
            m = min(m, v)
            s += v
        resM.append(M)
        resm.append(m)
        ress.append(s)
    else:
        M = m = matrice[0][l-1]
        s = 0
        for c in range(l):
            v = matrice[c][l-1-c]
            M = max(M, v)
            m = min(m, v)
            s += v
        resM.append(M)
        resm.append(m)
        ress.append(s)
    if op == 'max':
        return resM
    elif op == 'min':
        return resm
    else:
        return ress
