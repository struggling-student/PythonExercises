import json

def es39(n, jsonFile):
    # costruisco una matrice vuota NxN contenente solo zeri
    matrice = [[0 for _ in range(n)] for _ in range(n)]
    x, y = 0, 0                                             # parto dall'angolo in alto a sinistra
    direzioni =[0,1], [1,0], [0, -1], [-1, 0]               # elenco delle 4 possibili direzioni (incrementi di y e di x)
    dir = 0                                                 # la direzzione iniziale e' la prima (verso destra)
    for i in range(1, n*n+1):                               # scandisco i valori da 1 a n^2 compreso
        matrice[y][x] = i                                   # inserisco il valore nella casella
        ny = y + direzioni[dir][0]                          # calcolo nuova y
        nx = x + direzioni[dir][1]                          # e nuova x
        if not (0 <= nx < n and 0 <= ny < n and matrice[ny][nx] == 0):  # se la casella NON esiste o NON contiene 0
            dir = (dir + 1) % 4                             # cambio direzione passando alla prossima
            ny = y + direzioni[dir][0]                      # e ricalcolo ny e nx
            nx = x + direzioni[dir][1]                      # per costruzione sono certo che la casella esiste ed e' vuota
        x,y = nx,ny                                         # aggiorno x e y con nx ed ny
    somma = 0                                               # finita la costruzione della matrice
    for x in range(0, n, 2):                                # sommo le colonne con x pari
        for y in range(n):
            somma += matrice[y][x]
    with open(jsonFile, mode='w', encoding='utf8') as f:    # e salvo la matrice nel file json
        json.dump(matrice, f)
    return somma