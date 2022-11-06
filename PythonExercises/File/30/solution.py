def es30(fname1,fname2,fname3):
    mappa = {}
    with open(fname2, encoding='utf8') as f:
        for riga in f:
            c, n = riga.split()
            mappa[n] = c
    testo =''
    with open(fname1,encoding='utf8') as f:
        testo = f.read()
    testo1 = ''
    quanti = 0
    i = 0
    while i < len(testo):
        c = testo[i]
        if c in '0123456789':
            k = testo[i:i+3]
            i += 3
            if k in mappa:
                testo1 += mappa[k]
            else:
                testo1 += '?'
                quanti += 1
        else:
            i += 1
            testo1 += c
    with open(fname3, mode='w',encoding='utf8') as f:
        f.write(testo1)
    return quanti
