import json

def es40(jsonFile,k):
    # leggo la matrice dal file json
    with open(jsonFile, encoding='utf8') as f:
        matrice = json.load(f)
    h = len(matrice)                        # calcolo l'altezza
    w = len(matrice[0])                     # e la larghezza
    pos = (-1, -1)                          # inizializzo la posizione con (-1, -1)
    # scandisco prima le righe e poi le colonne
    # in modo che l'ultimo quadrato trovato sia anche quello piu' in basso a destra
    for y in range(h - k):                  # scandisco le righe fino alla h-k-1
        for x in range(w - k):              # scandisco le colonne fino alla w-k-1
            a = matrice[y  ][x  ]           # leggo i 4 valori
            b = matrice[y  ][x+k] - 1       # ai seguenti sottraggo 1, 2, 3
            c = matrice[y+k][x+k] - 2       # in modo da ottenere
            d = matrice[y+k][x  ] - 3       # 4 valori che dovrebbero essere uguali se ho trovato un quadrato
            if a == b == c == d:            # se sono uguali
                pos = x, y                  # ricordo la posizione
    return pos 