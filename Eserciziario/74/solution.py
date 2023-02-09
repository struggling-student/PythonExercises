import immagini


def es74(filePng, centro, spessore, colori, pngFileOut):
    img = immagini.load(filePng)
    conti = []
    for i, colore in enumerate(colori):
        raggioIn = i*spessore
        raggioOut = (i+1)*spessore
        conti.append(drawAnello(img, centro, raggioIn, raggioOut, colore))
    immagini.save(img, pngFileOut)
    return conti


def drawAnello(img, centro, rIn, rOut, colore):
    count = 0
    h = len(img)
    w = len(img[0])
    cx, cy = centro
    # si evita di sbordare dalla immagine
    minx = max(cx-rOut, 0)
    miny = max(cy-rOut, 0)
    maxx = min(cx+rOut, w)
    maxy = min(cy+rOut, h)
    # scandisco solo la zona dell'anello invece che tutta l'immagine
    for x in range(minx, maxx):
        for y in range(miny, maxy):
            d2 = (x-cx)**2 + (y-cy)**2  # distanza al quadrato
            # compresa tra raggio interno e raggio esterno (al quadrato)
            if rIn**2 <= d2 < rOut**2:
                img[y][x] = colore
                count += 1
    return count
