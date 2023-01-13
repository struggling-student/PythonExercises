import immagini


def es65(k, lista1, fout):
    img = [[(0, 0, 0) for _ in range(k)] for _ in range(k)]
    for q in lista1:
        x, y, l, r, g, b = q
        c = maxColore(img, q)
        disegna(img, x, y, l, c)
    immagini.save(img, fout)
    count = 0
    for x in range(len(img)):
        for y in range(len(img)):
            if img[x][y] == (0, 0, 0):
                count += 1
    return count


def massimo(c1, c2):
    r, g, b = c1
    r1, g1, b1 = c2
    if r > r1 or (r == r1 and g > g1) or (r == r1 and g == g1 and b >= b1):
        return c1
    return c2


def maxColore(img, q):
    lato = len(img)
    x, y, l, r, g, b = q
    c = (r, g, b)
    for ny in range(y, y+l):
        for nx in range(x, x+l):
            if nx < lato and ny < lato:
                c = massimo(c, img[ny][nx])
    return tuple(c)


def disegna(img, x, y, l, c):
    lato = len(img)
    for ny in range(y, y+l):
        for nx in range(x, x+l):
            if nx < lato and ny < lato:
                img[ny][nx] = c
