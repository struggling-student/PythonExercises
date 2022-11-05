def es33(fname1,fname2):
    testo = ''
    with open(fname1, encoding='utf8') as f:
        testo = f.read()
    histo = []
    for i in range(26):
        c = chr(ord('a')+i)
        n = testo.count(c)
        if n:
            histo.append((c*n,26-i))
    histo.sort(key=lambda x: (len(x[0]),x[1]),reverse=True)
    with open(fname2, mode='w',encoding='utf8') as f:
        f.write('\n'.join([x[0] for x in histo]))
    return len(histo)
