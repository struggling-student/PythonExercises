def es52(d1,d2):
    d={ x:d1[x] for x in d1}
    for x in d2:
        if x not in d:
            d[x]=d2[x]
        else: 
            d[x]+=d2[x]
    return d