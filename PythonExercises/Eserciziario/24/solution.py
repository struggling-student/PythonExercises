def es24(ifile, l):
    with open(ifile, encoding='utf8') as f:
        text = f.read()
    text = text.lower()
    d = {}
    lt = 0
    for c in text:
        if c.isalpha():
            lt += 1
    for c in l:
        d[c] = text.count(c.lower())
    for c in l:
        d[c] = 100*d[c]/lt
    for c in l:
        d[c] = round(d[c], 2)
    return [(k, "{:.2f}%".format(v))for k, v in sorted(d.items(), key=lambda x: (-x[1], x[0]))]
