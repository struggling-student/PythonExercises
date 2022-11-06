

def es59(ftesto):
    stringa = ''
    with open(ftesto) as f:
        for line in f:
            interi = map(int, line.split())
            stringa += str(sum(interi)%2)
    return stringa