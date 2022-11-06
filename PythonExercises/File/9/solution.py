import os

def es9(pathDir):
    ls1=prova(pathDir)
    ls1+=[pathDir]
    ls_fin=[]
    for el in ls1:
        spazio=0
        for perc in os.listdir(el):
            p=el+'/'+perc
            if os.path.isfile(p):
                if p[-4:]=='.txt':
                    spazio+=os.path.getsize(p)
        ls_fin.append((os.path.basename(el),spazio))
    ls_fin=sorted(ls_fin,key=lambda x: (-x[1],x[0]))
    return ls_fin

def prova(path):
    if os.path.isfile(path):
        return []
    ls=[]
    for el in os.listdir(path):
        p=path+'/'+el
        ls=ls+prova(p)
        if os.path.isdir(p):
            ls+=[p]
    return ls