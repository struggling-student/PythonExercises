


class Nodo:
    def __init__(self,V):
        self.id=V       # valore del nodo
        self.f=[]       # lista dei figli del nodo


################### DA QUI IN GIÙ SONO SOLO FUNZIONI NECESSARIE PER I TEST #####################
################### E' PROIBITO USARE QUESTE FUNZIONI NEL VOSTRO CODICE    #####################

def fromLista(lista):
    '''Crea l'albero da una lista [valore, listafigli]
           In cui lista figli contiene alberi o e' la lista vuota. '''
    r=Nodo(lista[0])
    r.f=[fromLista(x) for x in lista[1]]
    return r

def toLista(nodo):
    ''' Converte l'albero in una lista di liste [valore, listafigli]'''
    return [nodo.id, [toLista(x) for x in nodo.f]] 
