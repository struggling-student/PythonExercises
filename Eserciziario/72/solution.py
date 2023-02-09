import os
import json
import os.path


def es72(dir, jsonFile):
    dizio, massimo = esploraDir(dir, dir)
    with open(jsonFile, mode='w', encoding='utf8') as f:
        json.dump({dir: dizio}, f, indent=4)
    return massimo


def esploraDir(dir, name):
    dizio = {}
    files = os.listdir(dir)
    massimo = 0
    contafile = 0
    for f in files:
        if f[0] == '.': continue
        contafile += 1
        fn = "{}/{}".format(dir, f)
        if os.path.isdir(fn):
            d, m = esploraDir(fn, f)
            dizio[f] = d
            massimo = max(massimo, m)
        else:
            stat = os.stat(fn)
            dizio[f] = stat.st_size
    massimo = max(massimo, contafile)
    return dizio, massimo
