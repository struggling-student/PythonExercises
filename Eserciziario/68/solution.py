
import os
import os.path


def es68(dir, estensioni):
    count = {ext: 0 for ext in estensioni}
    for f in os.listdir(dir):
        fn = "{}/{}".format(dir, f)
        if os.path.isdir(fn):
            diz = es68(fn, estensioni)
            for k, v in diz.items():
                count[k] += v
        else:
            for ext in estensioni:
                if fn.endswith(ext):
                    count[ext] += 1
    for k in list(count.keys()):
        if count[k] == 0:
            del count[k]
    return count
