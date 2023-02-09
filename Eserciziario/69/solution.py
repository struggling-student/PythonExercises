import os
import os.path


def es69(dir, profondita, estensioni):
    count = 0
    for f in os.listdir(dir):
        if '.' == f[0]: continue
        fn = "{}/{}".format(dir, f)
        if profondita > 0:
            if os.path.isdir(fn):
                count += es69(fn, profondita-1, estensioni)
            else:
                count += 1
        else:
            if not os.path.isdir(fn):
                if fn.endswith(tuple(estensioni)):
                    os.remove(fn)
                else:
                    count += 1
    return count
