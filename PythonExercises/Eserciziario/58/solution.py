

def es58(lista):
    spostamenti = {
        'N': (-1,  0),
        'S': (1,  0),
        'E': (0,  1),
        'O': (0, -1),
    }
    nummosse = 0
    for i, mossa in enumerate(lista):
        x = 0
        y = 0
        for c in mossa:
            if c in 'NSEO':
                nummosse += 1
                dx, dy = spostamenti[c]
                x += dx
                y += dy
        lista[i] = abs(x)+abs(y)
    return nummosse
