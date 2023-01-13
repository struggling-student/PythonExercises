def es11(ftesto):
    with open(ftesto) as f:
        testo=f.read()
    testo=testo.strip()
    ls_parole=testo.split('\n')
    for i in range(len(ls_parole)):
        ls_parole[i]=ls_parole[i].strip()
    d=dict()
    for par in ls_parole:
        ls1=[]
        for i in range(len(par)):
            if par[i] not in 'aeiou':
                ls1.append(par[i])
        ls1.sort()
        chiave=''.join(ls1)
        d[chiave]=d.get(chiave,[])
        d[chiave].append(par)
    for c in d:
        ls=d[c]
        ls=sorted(ls,key=lambda x: (-len(x),x))
        d[c]=ls
    return d