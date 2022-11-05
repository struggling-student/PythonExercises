
def es77(parola):
    lista = []
    for i in range(len(parola)-1, -1, -1):
        lista += [parola[i:]]
    return lista
