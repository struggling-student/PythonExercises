def es31(fname1, fname2):
    testo = ''
    with open(fname1, encoding='utf8') as f:
        testo = f.read()
    parole = testo.split()
    conto = {chr(ord('a')+c): 0 for c in range(26)}
    for parola in parole:
        chars = set(parola)
        for c in chars:
            if 'a' <= c <= 'z':
                conto[c] += 1
    quanti = 0
    for c, v in conto.items():
        if v % 2:
            quanti += 1
            testo = testo.replace(c, c.upper())
    with open(fname2, mode='w', encoding='utf8') as f:
        f.write(testo)
    return quanti
