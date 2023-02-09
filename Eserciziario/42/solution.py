import immagini

def es42(fImageIn, fcolori, fImageOut):
    img = immagini.load(fImageIn)
    h = len(img)
    w = len(img[0])
    conteggio = 0
    palette = {}
    with open(fcolori) as f:
        for line in f:
            r, g, b, R, G, B = map(int, line.split())
            palette[(r, g, b)] = R, G, B
    for y in range(h):
        for x in range(w):
            c = img[y][x]
            if c in palette:
                img[y][x] = palette[c]
                conteggio += 1
    immagini.save(img, fImageOut)
    return conteggio