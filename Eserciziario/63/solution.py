def es63(fileParole, fileTerne):
    conteggio = 0
    with open(fileParole, encoding='utf8') as fin:
        with open(fileTerne, mode='w', encoding='utf8') as fout:
            for line in fin:
                parola = line.strip()
                l = len(parola)
                conteggio += l
                v = 0
                m = 0
                for c in parola:
                    if c in 'aiuoeAIUOE':
                        v += 1
                    if c.isupper():
                        m += 1
                fout.write(str((l, v, m)) + '\n')
    return conteggio
