

def es3(ins1, ins2):
    if(len(ins1) < 3):
        return []
    l1 = list(ins1)
    l1.sort()
    result = []
    for i, a in enumerate(l1[:-2]):
        for b in l1[i+1:-1]:
            for c in l1[l1.index(b)+1:]:
                if(a+b+c in ins2):
                    result.append(tuple([a, b, c]))
    result = sorted(result)
    return sorted(result, key=lambda t: t[0]+t[1]+t[2])
