import os
import os.path


def es67(path):
    minimi = {}
    massimi = {}
    minmassimi(path, minimi, massimi, 0)
    return {k: massimi[k]-minimi[k] for k in minimi}


def minmassimi(path, m, M, prof):
    for fn in os.listdir(path):
        if '.' == fn[0]: continue
        filename = path + '/' + fn
        if os.path.isdir(filename):
            minmassimi(filename, m, M, prof+1)
        else:
            ext = fn[-3:]
            m[ext] = min(m.get(ext, prof), prof)
            M[ext] = max(M.get(ext, prof), prof)
