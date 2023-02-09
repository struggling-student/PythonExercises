def es29(tabella1,tabella2,col):
    inizio = len(tabella1)
    valori = [riga[col] for riga in tabella1]
    for riga in tabella2:
        if riga[col] not in valori:
            tabella1.append(riga)
    tabella1.sort(key=lambda x: x[col])
    return len(tabella1) - inizio