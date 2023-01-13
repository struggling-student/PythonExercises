import albero
def es1(k):
    t,_ = crea_albero(k,1)
    return t

def crea_albero(k, n):
    """
    crea l'albero con k livelli a partire dal valore n
    torna l'albero e l'ultimo n usato
    """
    if k:       # se siamo su un nodo interno
        t = albero.Nodo( None )
        sinistro, n1 = crea_albero(k-1, n)
        destro,   n2 = crea_albero(k-1, n1+1)
        t.f = [sinistro, destro]
        t.id = sinistro.id + destro.id
        return t, n2
    else:
        t = albero.Nodo(n)
        return t, n

