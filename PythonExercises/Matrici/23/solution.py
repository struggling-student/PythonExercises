import immagini
import json


def es23(fileJson, filePng):
    with open(fileJson) as f:
        img = json.load(f)
    h = len(img)
    w = len(img[0])
    img1 = [[0 for _ in range(w)] for _ in range(h)]
    d = {}
    for i in range(h):
        for j in range(w):
            stringa = img[i][j]
            t = int(stringa[:3]), int(stringa[3:6]), int(stringa[6:])
            img1[i][j] = t
            if t in d:
                d[t] += 1
            else:
                d[t] = 1
    immagini.save(img1, filePng)
    return sorted(d.items(), key=lambda x: (-x[1], x[0][0], x[0][1], x[0][2]))[0][0]
