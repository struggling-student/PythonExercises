import immagini


def es75(w, h, listaColori, listaAltezze, larghezzaPalazzo, filePngOut):
    return es75_interpretazione2(w, h, listaColori, listaAltezze, larghezzaPalazzo, filePngOut)


def es75_interpretazione1(w, h, listaColori, listaAltezze, larghezzaPalazzo, filePngOut):
    # inserite qui il vostro codice
    blu = (0, 0, 255)
    img = [[blu for _ in range(w)] for _ in range(h)]
    counts = [[0 for _ in range(w)] for _ in range(h)]
    rettangoli = []
    N = len(listaAltezze)

    # prima possibile interpretazione delle parole "rettangoli equispaziati" (= con i centri equispaziati nella immagine)
    # i centri dei palazzi sono spaziati regolarmente nella immagine
    step = w//(N+1)
    # MA! se larghezzaPalazzo > step allora possono sbordare dalla immagine
    start = step - larghezzaPalazzo//2
    end = start + larghezzaPalazzo

    for colore, altezza in zip(listaColori, listaAltezze):
        rettangoli.append((start, end, h-altezza, h, colore))
        start += step
        end += step
    rettangoli.sort(key=lambda r: r[2])
    for r in rettangoli:
        drawRettangolo(img, *r, counts)
    immagini.save(img, filePngOut)
    cambiati = 0
    for line in counts:
        for n in line:
            if n > 1:
                cambiati += 1
    return cambiati


def es75_interpretazione2(w, h, listaColori, listaAltezze, larghezzaPalazzo, filePngOut):
    # inserite qui il vostro codice
    blu = (0, 0, 255)
    img = [[blu for _ in range(w)] for _ in range(h)]
    counts = [[0 for _ in range(w)] for _ in range(h)]
    rettangoli = []
    N = len(listaAltezze)

    # seconda possibile interpretazione delle parole "rettangoli equispaziati"
    # (= primo ed ultimo appoggiati al bordo, gli altri spaziati uniformemente)
    # il primo e l'ultimo palazzo sono appoggiati a sinistra e a destra
    start = 0
    end = larghezzaPalazzo
    # gli altri sono spaziati regolarmente (sono N-1 spazi)
    step = (w-larghezzaPalazzo)//(N-1)

    for colore, altezza in zip(listaColori, listaAltezze):
        rettangoli.append((start, end, h-altezza, h, colore))
        start += step
        end += step
    rettangoli.sort(key=lambda r: r[2])
    for r in rettangoli:
        drawRettangolo(img, *r, counts)
    immagini.save(img, filePngOut)
    cambiati = 0
    for line in counts:
        for n in line:
            if n > 1:
                cambiati += 1
    return cambiati


def drawRettangolo(img, l, r, t, b, c, counts):
    # si evita di sbordare dalla immagine
    w = len(img[0])
    h = len(img)
    l = max(l, 0)
    r = min(r, w)
    t = max(t, 0)
    b = min(b, h)
    for x in range(l, r):
        for y in range(t, b):
            img[y][x] = c
            counts[y][x] += 1
