import immagini
import json


def es22(filePng, fileJson):
    img = immagini.load(filePng)
    h = len(img)
    w = len(img[0])
    d = {}
    img1 = [['' for _ in range(w)] for _ in range(h)]
    for i in range(h):
        for j in range(w):
            a = codifica(img[i][j])
            img1[i][j] = a
            if a in d:
                d[a] += 1
            else:
                d[a] = 1
    with open(fileJson, 'w') as f:
        json.dump(img1, f)
    return sorted(d.items(), key=lambda x: (-x[1], x[0]))[0][0]


def codifica(tupla):
    r, g, b = tupla
    return adatta(r)+adatta(g)+adatta(b)


def adatta(x):
    if x < 10:
        return '00'+str(x)
    elif x < 100:
        return '0'+str(x)
    else:
        return str(x)
