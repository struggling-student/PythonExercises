def es46(parola):
    sotto = set()
    l = len(parola)
    for i in range(l):
        for j in range(i,l):
            sotto.add(parola[i:j+1])
    sotto = sorted(sotto, key=lambda p: (-len(p), p))
    for p in sotto:
        if palindroma(p):
            return p

def palindroma(p):
    if len(p) < 2:
        return True
    else:
        return p[0]==p[-1] and palindroma(p[1:-1])