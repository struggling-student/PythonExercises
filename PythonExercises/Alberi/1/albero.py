
import copy
import random

class AlberoBinario:
    def __init__(self, V, sx=None, dx=None):
        self.valore = V
        self.sx = sx
        self.dx = dx


################### DA QUI IN GIÙ SONO SOLO FUNZIONI NECESSARIE PER I TEST #####################

################### ATTENZIONE È VIETATO USARE LE FUNZIONI QUI SOTTO ###########################

    @classmethod
    def fromList(cls, lista):
        """
        Costruisce l'albero da una lista [valore, sinistro, destro]
        In cui sinistro e destro sono altrettanti alberi oppure il valore None
        :param lista:
        :return:
        """
        valore, sx, dx = lista
        if sx: sx = cls.fromList(sx)
        if dx: dx = cls.fromList(dx)
        return cls(valore, sx, dx)

    def toList(self):
        """
        Converte l'albero in lista di liste [valore, sinistra, destra]
        :return:
        """
        sx = None if not self.sx else self.sx.toList()
        dx = None if not self.dx else self.dx.toList()
        return [self.valore, sx, dx]

    def __eq__(self, other):
        """
        Confronta due alberi
        :param other:
        :return:
        """
        return other != None and \
               type(self) == type(other) and \
               self.valore == other.valore and \
               self.sx == other.sx and \
               self.dx == other.dx

    def __repr__(self, livello=0):
        """
        Stampa un albero con livello di indentazione dato
        :param livello: indentazione
        :return:
        """
        indent = "|  "*livello
        res = "{0}Nodo_{1}: {2.valore}".format(indent, id(self), self)
        indent = "|  "*(livello+1)
        if self.sx:
            res += "\n{}".format(self.sx.__repr__(livello+1))
        else:
            res += "\n{}{}".format(indent, self.sx)
        if self.dx:
            res += "\n{}".format(self.dx.__repr__(livello+1))
        else:
            res += "\n{}{}".format(indent, self.dx)
        return res

    @classmethod
    def randomTree(cls, level):
        """
        Genera un albero casuale di al più level livelli
        :param level:
        :return:
        """
        if random.randint(0, 100) < 10 or level < 0:    # nel 10% dei casi è None
            return None
        V = random.randint(1, 1000000)
        sx = cls.randomTree(level - random.randint(1,3)) # accorcio la profondita da 1 a 3 livelli a caso
        dx = cls.randomTree(level - random.randint(1,3)) # accorcio la profondita da 1 a 3 livelli a caso
        return cls(V, sx, dx)

if __name__ == '__main__':
    lista = [1, [2, None, None],
                [3, [4, None, None],
                    [5, None, None],
                ],
            ]
    albero  = AlberoBinario.fromList(lista)
    albero2 = copy.deepcopy(albero)
    albero3 = AlberoBinario.randomTree(10)

    print('A =', albero, sep='\n')
    print('B =', albero2, sep='\n')
    print('A =', albero.toList())
    print('C =', albero3 )
    print('C =', albero3.toList() )
