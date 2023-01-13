
class AlberoBinario:
    def __init__(self, V, sx=None, dx=None):
        self.valore = V
        self.sx = sx
        self.dx = dx



################### DA QUI IN GIÙ SONO SOLO FUNZIONI NECESSARIE PER I TEST #####################



def fromLista(lista):
    '''Crea l'albero da una lista [valore, listafigli]
           In cui lista figli contiene alberi o e' la lista vuota. '''
    r=AlberoBinario(lista[0])
    if lista[1]!=None: r.sx= fromLista(lista[1])
    if lista[2]!=None: r.dx= fromLista(lista[2])
    return r
