def es20(stringa1):
    alf='abcdefghilmnopqrstuvz'
    d={alf[i]:i+1 for i in range(len(alf))}
    stringa=''
    n=0
    stringa1=stringa1.lower()
    for x in stringa1:
        if x in d: 
            n+=d[x]
        else:
            if n !=0:
                stringa=stringa+str(n)
                stringa=stringa+' '
                n=0
    if n !=0:
        stringa=stringa+str(n)
    return stringa