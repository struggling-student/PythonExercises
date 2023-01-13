def es18(d1, d2):
    res = dict()
    if(len(d1) <= len(d2)):
        for k in d1.keys():
            if k in d2.keys():
                res[k] = (intersection(d1[k], d2[k]), union(d1[k], d2[k]))
    else:
        for k in d2.keys():
            if k in d1.keys():
                res[k] = (intersection(d1[k], d2[k]), union(d1[k], d2[k]))
    return res


def union(set1, set2):
    res = set1
    for el in set2:
        res.add(el)
    return res


def intersection(set1, set2):
    res = set()
    if(len(set1) <= len(set2)):
        for el in set1:
            if(el in set2):
                res.add(el)
    else:
        for el in set2:
            if(el in set1):
                res.add(el)
    return res
