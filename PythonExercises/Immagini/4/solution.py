import immagini


def es4(fimm, fimm1, h1, w1):
    imgNuova = []                             # inizializzo una lista per la nuova immagine
    imgOriginale = immagini.load(fimm)        # carico l'immagine oeiginale
    hOrignale = len(imgOriginale)             # altezza immagine originale
    wOriginale = len(imgOriginale[0])         # larghezza immagine originale
    countColor = {}
    for _ in range(hOrignale*h1):             # preparo l'mmagine inserendo al posto di ogni pixel, uno 0
        row = []
        for _ in range(wOriginale*w1):
            row.append(0)
        imgNuova.append(row)
    for x in range(hOrignale):
        for y in range(wOriginale):
            colorePix = imgOriginale[x][y]
            imgNuova = disegnaRettangolo(imgNuova, x*h1, y*w1, h1, w1, colorePix)   # disegna il rettangolo in imgNuova
            if colorePix in countColor:                                             # aggiorna il dizionario dei colori
                countColor[colorePix] += 1
            else:
                countColor[colorePix] = 1
    immagini.save(imgNuova, fimm1)                                                        # salva l'immagine nuova in fimm1
    maxColor = max(countColor.values())                                                   # prendo il numero di volte maggiore che un colore compare
    listColor = sorted(list(filter(lambda x: countColor[x] == maxColor, countColor)))     # elimino tutti i colori che non compaiono il numero di volte massimo e ordino la lista ottenuta
    return listColor[0]                                                                   # ritorno il colore con valore massimo

def disegnaRettangolo(img, x, y, h, w, c):
    '''la funzione disegna un rettangolo nell'immagine img
    con vertice in alto a sinistra in (x, y), di altezza h e larghezza w,
    di colore c'''
    for i in range(x, x+h):
        for j in range(y, y+w):
            img[i][j] = c
    return img
