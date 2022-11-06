import immagini


def es49(fimm1, fimm2, fimm3):
    img1 = immagini.load(fimm1)
    img2 = immagini.load(fimm2)
    w1, h1 = len(img1[0]), len(img1)
    w2, h2 = len(img2[0]), len(img2)
    w3 = min(w1, w2)
    h3 = min(h1, h2)
    img3 = [[(0, 0, 0) for _ in range(w3)] for _ in range(h3)]
    count = 0
    for i in range(h3):
        for j in range(w3):
            img3[i][j] = img2[i][j]
            if i % 2 == j % 2:
                img3[i][j] = img1[i][j]
            a, b, c = img3[i][j]
            if (a+b+c) % 2:
                count += 1
    immagini.save(img3, fimm3)
    return count
