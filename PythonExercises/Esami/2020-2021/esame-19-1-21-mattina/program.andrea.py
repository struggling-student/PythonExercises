
################################################################################
################################################################################
################################################################################

''' ATTENZIONE!!! INSERITE SUBITO QUI SOTTO IL VOSTRO NOME, COGNOME E MATRICOLA '''

nome        = "NOME"
cognome     = "COGNOME"
matricola   = "MATRICOLA"

################################################################################
################################################################################
################################################################################
# SUGGERIMENTI PER IL DEBUG 
#   per eseguire solo parte dei test commentare le righe 288-292 alla fine di grade.py
#
#   per vedere lo stack trace degli errore scommentate la riga 36 di testlib.py 
################################################################################
################################################################################
################################################################################

'''
Esercizio 1: 6 punti

Sia data una tabella rappresentata come lista di dizionari.
Ciascuna colonna della tabella è individuata dal suo nome.
Ciascun dizionario contenuto nella lista ha le stesse chiavi, che sono i nomi delle colonne della tabella.
I valori possono essere stringhe, interi o float.

Esempio: la tabella
    Nome    Cognome     Telefono    Indirizzo
    Andrea  Sterbini    137487468   via del Pero 3
    Gianni  Pierini     764817689   via degli Angeli 17
Corrisponde alla lista di dizionari
[   { 'Nome': 'Andrea', 'Cognome': 'Sterbini', 'Telefono': 137487468, 'Indirizzo': 'via del Pero 3' },
    { 'Nome': 'Gianni', 'Cognome': 'Rodari',   'Telefono': 137487468, 'Indirizzo': 'via degli Angeli 14' },
    { 'Nome': 'Gianni', 'Cognome': 'Pierini',  'Telefono': 137487468, 'Indirizzo': 'via degli Angeli 17' },
]

Si progetti la funzione es1(tabella, colonne, elimina) che riceve come argomenti:
    - tabella: una tabella rappresentata come lista di dizionari
    - colonne: una lista di nomi di colonne rispetto alle quali ordinare la tabella
    - elimina: una lista di nomi di colonne che vanno completamente eliminate
e che torna come risultato  il numero di colonne eliminate 
in modo che le sue righe siano ordinate in ordine crescente 
relativamente al sottoinsieme di valori presenti nelle colonne indicate.
Ed inoltre tutte le colonne indicate nella lista 'elimina' vallo eliminate dai dizionari.

Esempio: se colonne=['Nome', 'Cognome'] e elimina=['Telefono'] la tabella deve diventare
[   { 'Nome': 'Andrea', 'Cognome': 'Sterbini', 'Indirizzo': 'via del Pero 3' },
    { 'Nome': 'Gianni', 'Cognome': 'Pierini',  'Indirizzo': 'via degli Angeli 17' },
    { 'Nome': 'Gianni', 'Cognome': 'Rodari',   'Indirizzo': 'via degli Angeli 14' }
]

Esempio: se colonne=['Telefono', 'Nome', 'Indirizzo'] la tabella deve diventare
[   { 'Nome': 'Andrea', 'Cognome': 'Sterbini', 'Telefono': 137487468, 'Indirizzo': 'via del Pero 3' },
    { 'Nome': 'Gianni', 'Cognome': 'Rodari',   'Telefono': 137487468, 'Indirizzo': 'via degli Angeli 14' },
    { 'Nome': 'Gianni', 'Cognome': 'Pierini',  'Telefono': 137487468, 'Indirizzo': 'via degli Angeli 17' },
]

NOTA: se colonne=[] la tabella deve rimanere invariata.
NOTA: se elimina=[] non deve essere eliminata nessuna colonna.

'''
def es1(tabella, colonne, elimina):
    tabella.sort(key=lambda x: [x[colonna] for colonna in colonne] )
    for riga in tabella:
        for colonna in elimina:
            del riga[colonna]
    return len(elimina)

#################################################################################################

'''
Es 2: punti 8

Sia dato un file PNG contenente una immagine.
Si realizzi la funzione es2(file_png, colori) che riceve come argomenti:
    - file_png: il filename del file PNG
    - colori:   una lista di colori RGB (tuple di 3 valori tra 0 e 255)
che trova i bounding-box dei pixel che sono colorati con ciascuno dei colori 
(il bounding-box è la tupla  (x1,y1,x2,y2) del punto più in alto a sinistra x1,y1 
e del più in basso a destra x2,y2 che contiene tutti i pixel di quel colore)
La funzione deve infine tornare la lista dei bounding-box ordinata per superficie decrescente,
e in caso di parità in ordine crescente di colore.
NOTA: se il colore non appare nell'immagine il valore da tornare per quel colore è None.
Esempio: se la immagine è '3cime.png' ed i colori sono [ (255, 255, 255), (0, 0, 0), (255, 0, 0), (0, 200, 200) ]
Il risultato sarà:
    [(137, 10, 191, 31), (95, 121, 95, 121), (149, 47, 149, 47), None]
'''
import images

def area_colore(colore_bb):
    colore, bb = colore_bb
    area = 0 
    if bb:
        x1,y1,x2,y2 = bb
        area = (x2-x1+1)*(y2-y1+1)
    return -area, colore

def es2(file_png, colori):
    img = images.load(file_png)
    bb = { colore: None for colore in colori }
    for y, riga in enumerate(img):
        for x, pixel, in enumerate(riga):
            if pixel in bb:
                if bb[pixel] is None:
                    bb[pixel] = x,y,x,y
                else:
                    x1,y1,x2,y2 = bb[pixel]
                    bb[pixel] = min(x1,x), min(y1,y), max(x2,x), max(y2,y)
    return [ bb for colore,bb in sorted(bb.items(), key=area_colore) ]

#################################################################################

'''
Es 3: punti 9

Si definisca la funzione es3(albero, k), ricorsiva o che fa uso di funzioni/metodi ricorsivi,
che riceve come argomenti:
    - albero: la radice di un albero di tipo tree.BinaryTree (vedi tree.py)
    - k:      un intero
che per ogni nodo che ha valore ID che è multiplo di k, elimina tutti i nodi in esso contenuti.
Lo ID del nodo multiplo di k viene sostituito con la somma degli ID dei nodi eliminati.

Esempio:            6
                /       \
            7               5
        /       \       /       \
    2           4       6       8
               /                 \
              15                  10
se k = 5 l'albero diventa
                    6
                /       \
            7               24
        /       \       
    2           4      
               /
              0
'''
import tree
def es3(albero, k):
    if albero is None:
        return None
    if albero.ID % k == 0:
        return tree.BinaryTree(somma(albero.left) + somma(albero.right))
    else:
        albero.left  = es3(albero.left, k)
        albero.right = es3(albero.right, k)
    return albero

def somma(albero):
    if albero is None:
        return 0
    else:
        return somma(albero.left) + somma(albero.right) + albero.ID

###############################################################################
'''
Esercizio 4: 9 punti

Si dato un albero N-ario formato da nodi tree.NaryTree.

Realizzate la funzione es4(radice, k) che riceve come argomenti:
    - radice: un nodo di tipo tree.NaryTree
    - k: il numero minimo di figli da cercare
e che trova i due nodi che hanno almeno k figli ed hanno profondità massima e minima
e torna come risultato la tupla
    (differenza_di_profondita, differenza_di_valore)
NOTA: potete assumere che i nodi con almeno k figli che sono a profondità massima e minima sono unici

Esempio:
                          17
                          |
        -------------------------------------------
        |      |          |         |             |
        13     21        95        32            26
        |      |          |                       |
    --------   |     ---------------------        |
    |   |  |   |     |   |   |   |   |   |        |
    4   7  9   5    -3  -4  -5  -6   -8  -10      42

    Se k=4
    - il nodo meno profondo con almeno 4 figli è il 17 che sta a profondità 0
    - il nodo più  profondo con almeno 4 figli è il 95 che sta a profondità 1
    e la funzione deve tornare la tupla (1, 78)
'''

def es4(radice, k):
    profondità_e_valori = []
    esplora(radice, k, 0, profondità_e_valori)
    upper_d, upper_v = min(profondità_e_valori)
    lower_d, lower_v = max(profondità_e_valori)
    return lower_d-upper_d, lower_v-upper_v

def esplora(radice, k, prof, lista):
    if len(radice.sons) >= k:
        lista.append((prof, radice.value))
    for son in radice.sons:
        esplora(son, k, prof+1, lista)


if __name__ == '__main__':
    pass
