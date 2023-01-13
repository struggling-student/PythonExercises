
class Node:
    def __init__(self,value):
        self.value = value
        self.sons  = []

################### DA QUI IN GIÙ SONO SOLO FUNZIONI NECESSARIE PER I TEST #####################
################### E' VIETATO USARE QUESTE FUNZIONI                       #####################

def fromLista(lista):
    '''Crea l'albero da una lista [valore, listafigli]
           In cui lista figli contiene alberi o e' la lista vuota. '''
    r=Node(lista[0])
    r.sons=[fromLista(x) for x in lista[1]]
    return r

def toLista(nodo):
    ''' Converte l'albero in una lista di liste [valore, listafigli]'''
    return [nodo.value, [toLista(x) for x in nodo.sons]]
