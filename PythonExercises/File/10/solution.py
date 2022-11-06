def es10(ftesto,k):
    with open(ftesto) as f:
        testo=f.read()
    ls_parole=testo.split('\n')
    for i in range(len(ls_parole)-1,-1,-1):
        if len(ls_parole[i])!=k:
            del ls_parole[i]
    s=''
    if ls_parole==[]:
        return s
    for i in range(k):
        d=dict()
        for par in ls_parole:
            d[par[i]]=d.get(par[i],0)
            d[par[i]]+=1
        ls1=list(d.values())
        m=max(ls1)
        if ls1.count(m)==1:
            for c in d:
                if d[c]==m:
                    s+=c
        else:
            ls2=[]
            for c in d:
                if d[c]==m:
                    ls2.append(c)
            ls2.sort()
            s+=ls2[0]
    return s