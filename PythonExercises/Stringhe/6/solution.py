import albero

def es6(percorsi):
    lstPercorsi = list(percorsi)
    root = albero.AlberoBinario(lstPercorsi[0][-1:])
    for percorso in lstPercorsi:
        root = constructPath(root, percorso[:-1])
    return root



def constructPath(root, pathStr):
    if(pathStr == ''):
        return root
    lastChar = pathStr[-1:]
    if(lastChar > root.valore):
        if(root.dx == None):
            root.dx = albero.AlberoBinario(lastChar)
            constructPath(root.dx, pathStr[:-1])
        else:
            constructPath(root.dx, pathStr[:-1])
    elif(lastChar < root.valore):
        if(root.sx == None):
            root.sx = albero.AlberoBinario(lastChar)
            constructPath(root.sx, pathStr[:-1])
        else:
            constructPath(root.sx, pathStr[:-1])
    return root