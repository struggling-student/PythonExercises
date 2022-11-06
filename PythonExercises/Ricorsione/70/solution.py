import os
import os.path


def es70(dir, estensioni, parole):
    parole = [p.lower() for p in parole]
    count = {p: 0 for p in parole}
    for f in os.listdir(dir):
        fn = "{}/{}".format(dir, f)
        if os.path.isdir(fn):
            diz = es70(fn, estensioni, parole)
            for k, v in diz.items():
                count[k] += v
        elif not fn.endswith(tuple(estensioni)):
            with open(fn) as f:
                for line in f:
                    for word in line.split():
                        word = word.lower()
                        if word in parole:
                            count[word] += 1
    for k in list(count.keys()):
        if count[k] == 0:
            del count[k]
    return count
