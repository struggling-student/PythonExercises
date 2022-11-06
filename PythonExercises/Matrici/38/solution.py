import copy


def es38(labirinto):
    # non posso modificare il labirinto, per cui ne creo una copia
    # copio il labirinto per poterlo modificare
    lab = [[v for v in row] for row in labirinto]

    # per capire se una cella e' raggiungibile basta guardare le due sopra e a sinistra)
    # uso il valore 2 per indicare che la cella e' raggiungibile
    # marco la prima casella come raggiungibile
    lab[0][0] = 2
    # e ricordo posizione iniziale
    pos = (0, 0)
    # scandisco la matrice prima per righe e poi per colonne
    # in modo che l'ultima cella raggiungibile trovata sia anche quella piu' in basso a destra
    # scandisco la matrice dall'alto in basso
    for y, row in enumerate(lab):
        for x, cell in enumerate(row):              # e da sinistra a destra
            # se la casella corrente e' vuota
            # e a destra di una raggiungibile oppure sotto una raggiungibile
            if cell == 0 and ((y > 0 and lab[y-1][x] == 2) or (x > 0 and lab[y][x-1] == 2)):
                # la marco come raggiungibile
                lab[y][x] = 2
                pos = x, y                          # me la segno
    return pos                                      # e alla fine la ritorno
