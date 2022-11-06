import os
import os.path


def es71(dir, minimo, massimo, prof=0):
    profs = {}
    for f in os.listdir(dir):
        fn = "{}/{}".format(dir, f)
        if os.path.isdir(fn):
            diz = es71(fn, minimo, massimo, prof+1)
            for k, v in diz.items():
                if k not in profs or v > profs[k]:
                    profs[k] = v
        else:
            stat = os.stat(fn)
            if minimo <= stat.st_size <= massimo:
                if f not in profs or prof > profs[f]:
                    profs[f] = prof
    return profs
