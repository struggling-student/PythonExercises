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
Es 1: punti 6
Un file di testo contiene una sequenza di interi separati tra loro  da spazi e andate a capo. 
Il file codifica una matrice di interi. Il primo intero 
del file riporta  il numero di righe di M, il secondo intero riporta il numero di colonne di M 
i numeri seguenti riportano gli elementi della matrice ordinati per colonne e a parita' per righe.
Si guardi  ad esempio il file 'mat1.txt' che codifica la matrice 

1 2 
3 4 
5 6  

Progettare una funzione es1(ftesto)  che prende in input l'indirizzo  
di un file di testo siffatto e restituisca la  matrice codificata rappresentanta tramite lista
di liste di interi.
 

Ad esempio, nel caso del file 'mat1.txt'  la funzione deve restituire 
[[1,2],[3,4],[5,6]]
'''

def es1(fname):
    # inserisci qui il tuo codice
    with open(fname) as F:
        H,W,*numeri = list(map(int, F.read().split()))
        matrice = [ [0]*W for _ in range(H)]
        for i, N in enumerate(numeri):
            Y = i%H
            X = i//H
            matrice[Y][X] = N
    return matrice

#####################################################################################


'''    
    Es 2: punti 7
    
    Abbiamo immagini che contengono su sfondo nero rettangoli di diversi colori che non 
    si intersecano   e i cui lati sono segmenti orizzontali o verticali. 
    Si consideri ad esempio la figura Rettangoli.png.
    Dato un intero k vogliamo individuare i pixel dell'immagine che hanno 
    come vicini pixel di esattamente k diversi colori
    Ricorda che ogni pixel ha potenzialmente 8 vicini: 2 in orizzontale, due in verticale e 4 in diagonale

    
    Progettare la  funzione es2(fname) che prende come parametro l' intero k e 
    l'indirizzo di un file .PNG contenente un'immagine siffatta e  restituisce un dizionario.
    Il dizionario contiene come chiavi le  tuple di k colori
    ed ogni chiave ha come attributo l'insieme di pixel dell'immagine  che hanno come vicini k pixel 
    con quei colori.
    I colori delle chiavi sono rappresentati tramite triple RGB e compaiono nella tupla in ordine lessicografico crescente, 
    i pixel negli insiemi-attributo sono rappresentati tramite le tuple con le loro coordinate (colonna, riga)
    
    Ad esempio per il file Rettangoli.png e k=4 la funzione e2 deve restituire il dizionario
    {
    ((0, 0, 255), (0, 255, 0), (100, 100, 100), (255, 0, 0)): {(39, 60), (39, 59), (40, 59), (40, 60)}
    }

    Per caricare e salvare i file PNG si possono usare load e 
    save della libreria immagini.
    '''

import immagini

def es2(k,fname1):
    # inserisci qui il tuo codice
    img = immagini.load(fname1)
    W,H = len(img[0]), len(img)
    dizio = {}
    for x in range(W):
        for y in range(H):
            vicini = set()
            for X in range(max(0,x-1), min(x+2,W)):
                for Y in range(max(0, y-1), min(y+2,H)):
                    if X==x and Y==x: continue
                    vicini.add(img[Y][X])
            if k != len(vicini): continue
            chiave = tuple(sorted(vicini))
            if chiave in dizio:
                dizio[chiave].add((x, y))
            else:
                dizio[chiave] = {(x, y)}
    return dizio


############################################################################


'''
    Es. 3: punti 10

    Si definisca la funzione es3(r) ricorsiva (o che fa uso 
    di funzioni o metodi ricorsive/i) che riceve come parametro la radice r di un albero binario
    formato da nodi del tipo AlberoBinario definito nella libreria albero.py e 
    restituisce una lista di tuple.
    La lista contiene una tripla per ogni nodo x dell'albero, piu' precisamente per ogni nodo x dell'albero:
    - la prima coordinata della tripla riporta il valore del nodo x, 
    - la seconda coordinata riporta il numero di nodi discendenti di x con valore inferiore al valore di x
    - la terza coordinata riporta il numero di nodi discendenti di x con  valore superiore al valore di x
    Le triple della lista devono risultare ordinate lessicograficamente.



Ad esempio per l'albero:
     0
    / \
   5   5 
      / 
     3
    / \ 
   9   7

   
la funzione es3 restituisce la lista 
[(0, 0, 5), (1, 0, 0), (3, 0, 2), (5, 1, 2), (7, 0, 0), (9, 0, 0)]


    NOTA: definite le vostre sottofunzioni a livello esterno altrimenti non passate 
          il test di ricorsione
'''


import albero

def es3(r):
    # inserisci qui il tuo codice
    lista = []
    scandisci(r,lista)
    return sorted(lista)

def scandisci(r,lista):
    if r != None:
        l,m = conta(r,r.valore)
        lista.append((r.valore,l,m))
        scandisci(r.sx,lista)
        scandisci(r.dx,lista)

def conta(r,v):
    if r == None: return 0, 0
    less, more = conta(r.sx, v)
    l, m = conta(r.dx, v)
    less += l
    more += m
    if r.valore < v:
        less += 1
    elif r.valore > v:
        more += 1
    return less, more

###########################################################################

'''
    Es. 4: punti 9
    
    Si realizzi la funzione ricorsiva (o che usa funzioni ricorsive) es(dirname, insieme) che
    riceve come argomento il nome di una directory (dirname) ed un insieme di stringhe (insieme).
    La funzione esplora la directory dirname e le sue sottodirectory e restituisce il numero di file  
    che incontra aventi come   estensione una delle stringhe dell'insieme:  
    Ignorate tutti i file e directory che iniziano con '.' oppure '_'
    
    Ad esempio con dirname='dir1' e insieme={'txt','pdf'} la funzione es4 deve restituire il numero 5
    NOTA: è proibito usare la funzione os.walk
    NOTA: definite le vostre sottofunzioni a livello esterno altrimenti non passate 
          il test di ricorsione
'''    

import os
def es4(dirname,insieme): 
    # inserisci qui il tuo codice
    conta = 0
    for name in os.listdir(dirname):
        if name[0] in '._': continue
        fullname = dirname + '/' + name
        if os.path.isdir(fullname):
            conta += es4(fullname, insieme)
        else:
            if fullname.split('.')[-1] in insieme:
                conta += 1
    return conta

