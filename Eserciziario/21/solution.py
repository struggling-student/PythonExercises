def es21(matrice):
    matrice1 = [[] for i in range(len(matrice))]
    for j in range(len(matrice[0])):
        colonna = []
        for i in range(len(matrice)):
            colonna += [matrice[i][j]]
        colonna.sort()
        for i in range(len(matrice)):
            matrice1[i] += [colonna[i]]
    return matrice1
