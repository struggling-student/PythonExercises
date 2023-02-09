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
Es 1: punti 6. 
Un file contiene dei numeri interi scritto nel seguente modo: 
- i numeri sono separati tra loro da una o piu' righe vuote.
- ciascun  numero  occupa righe consecutive, una cifra per riga, ciascuna 
  riga comincia con il carattere % seguito dalla cifra, la cifra e' rappresentata 
  in unario, cioe' con un numero di caratteri 1 pari al suo valore. Le cifre sono scritte dalla piu' 
  significativa alla meno significativa.  
Ad esempio, il file "U1.txt" contiene i numeri  5049, 10, 94, 0, 49, 66.
Si puo` assumere che nel file non siano presenti 
spazi bianchi o altri caratteri e che il file termini con una riga vuota.


Progettare una funzione es1(ftesto) che prende in input  l'indirizzo di un 
file siffatto e restituisce una lista contenente i numeri del file. nalle lista i numeri 
devono risultare  ordinati per numero di cifre decrescenti, a parita' di cifre per 
per valore crescente.


Ad esempio, nel caso del file 'U1.txt'  la funzione deve restituire la lista
[5049,10,49,66,94,0] 
'''

def es1(ftesto):
    # inserisci qui il tuo codice
    with open(ftesto) as F:
        numeri = []
        corrente = None
        for riga in F:
            riga = riga.strip()
            if riga == '':
                if corrente != None:
                    numeri.append(corrente)
                corrente = None
            elif riga[0] == '%':
                if corrente == None: corrente = 0
                corrente *= 10
                corrente += len(riga) - 1
        if corrente != None:
            numeri.append(corrente)
    numeri = sorted(numeri, key=lambda n: (-len(str(n)),n))
    return numeri

    
#####################################################################################


'''    
    Es 2: punti 8
    
    Abbiamo un insieme P contenete punti, ogni punto e' una tupla (x,y) con le coordinate del punto. 
    Vogliamo produrre un'immagine dove compaiano i punti  ed eventualmente alcuni segmenti verticali 
    ed alcuni segmenti orizzontali. 
    Piu' precisamente:
    1) L'altezza h e la larghezza w dell'immagine sono i valori minimi in grado di contenere 
    le coordinate di tutti i punti.
    1) i punti appaiono nell'immagine in rosso (255,0,0) su sfondo nero (0,0,0).
    2) per ogni punto p=(x,y) per cui esistono due punti 
        p1=(x1,y) con x1>x e stessa y
        e p2=(x,y1) con y1>y e stessa x
    nell'immagine deve comparire un segmento  di colore bianco (255,255,255) che unisce  
    p al punto piu' vicino tra p1 e p2 (a p1 se le due distanze sono uguali).
    In altre parole se a destra di p c'e' un punto p1 con la sua stessa coordinata 
    y e sotto di p c'e' un punto p2 con la sua stessa coordinata x,  nell'immagine 
    comparira' un segmento  orizzontale tra p e p1 se p 
    dista meno o lo stesso da p1, un segmento verticale tra  p e p2 se p2 dista meno da p. 
    Ad esempio l'immagine corrispondente all'insieme 
    P={(20,10),(20,20),(20,40),(40,40),(50,20),(50,70),(60,20)}
    avra' altezza 70 e larghezza 60 ed e' riportata in figura I1.png
    
    Progettare la  funzione es2(P, fname1) che prende in input l'insieme di punti P e 
    l'indirizzo fname1 di un file .png e salva  all'indirizzo fname1 l'immagine ottenuta 
    dall'insieme  dei punti P e restituisce il numero di segmenti orizzontali presenti nell'immagine.
     
    Per caricare e salvare i file PNG si devono usare load e 
    save della libreria immagini.
    '''
import immagini

def es2(P,fname):
    # inserisci qui il tuo codice
    punti = sorted(P)
    maxx = max([x for x,y in P]) + 1
    maxy = max([y for x,y in P]) + 1
    img = [ [(0,0,0)] * maxx for _ in range(maxy) ]
    for x,y in punti:
        img[y][x] = (255, 0, 0)
    segmenti = 0
    for x,y in punti:
        DX = min([(X,Y) for X,Y in P if Y==y and X>x], key=lambda p: p[0], default=None)
        DN = min([(X,Y) for X,Y in P if X==x and Y>y], key=lambda p: p[1], default=None)
        if DX and DN :
            x1,_ = DX
            _,y2 = DN
            if x1-x <= y2-y:
                segmenti += 1
                for X in range(x+1, x1):
                    img[y][X] = (255, 255, 255)
            else:
                for Y in range(y+1, y2):
                    img[Y][x] = (255,255,255)
    immagini.save(img, fname)
    return segmenti

############################################################################


'''
    Es. 3: punti 9
    Dato un nodo di un albero, il grado del nodo e' il numero di figli che il nodo ha.
    
    Si definisca la funzione es3(r) ricorsiva (o che fa uso 
    di funzioni o metodi ricorsive/i) che riceve come parametro la radice r di un albero 
    formato da nodi del tipo Nodo definito nella libreria tree.py e 
    restituisce un dizionario.
    Il dizionario contiene come chiave i gradi dei nodi presenti nell'albero e 
    associato ad ogni grado c'e' la lista dei valori dei nodi dell'albero che hanno quel grado. 
    La lista deve risultare ordinata in modo non decrescente.

    Ad esempio per l'albero:
              16               
      ________|_____________   
     |          |           |  
     2          4           5  
     |     _____|______        
     10   |   |  |  |  |       
          1   2  9  8  2       
            __|__              
           |     |             
           3     6             

   la funzione es3 restituisce il dizionario {3: [16], 1: [2], 0: [1, 2, 3, 5, 6, 8, 9, 10], 5: [4], 2: [2]} 

    NOTA: definite le vostre sottofunzioni a livello esterno altrimenti non passate 
          il test di ricorsione
'''

import tree

def es3(r):
    # inserisci qui il tuo codice
    dizio = {}

    es3_ric(r, dizio)

    for k in dizio:
        dizio[k].sort()
    return dizio

def es3_ric(r, diz):
    grado = len(r.sons)
    if grado in diz:
        diz[grado].append(r.value)
    else:
        diz[grado] = [r.value]
    for son in r.sons:
        es3_ric(son, diz)

###########################################################################

'''
    Es. 4: punti 9
    
    Si realizzi la funzione ricorsiva (o che usa funzioni ricorsive) es4(dirname) che
    riceve come argomento il nome di una directory (dirname) ed una stringa (s).
    La funzione esplora la directory dirname e le sue sottodirectory e ritorna una lista di tuple.
    E' presente una tupla per ogni file con estensione .txt 
    contenente occorrenze della stringa s (indipendentemente dalle maiuscole/minuscole) 
    incontrato durante la visita. Le tuple sono coppie (a,b) dove:
        - a e' il nome completo del file
        - b e' il numero di posizioni all'interno del file in cui si e' rilevata la stringa.
    La lista deve risultare ordinata lessicograficamente rispetto alla prima coordinata 
    delle tuple.
    Ignorate tutti i file e directory che iniziano con '.' oppure '_'
    
    Ad esempio per la cartella dir1 la funzione es4 deve restituire la lista:
    [('dir1/st1/st2/1W.txt', 4), ('dir1/st1/st2/Ncn.txt', 5), ('dir1/zzzEFG.txt', 1)]
    
    NOTA: è proibito usare la funzione os.walk o similari ricorsive di sistema
    NOTA: definite le vostre sottofunzioni a livello esterno altrimenti non passate 
          il test di ricorsione
'''    

import os

def es4(dirname,parola): 
    #inserisci qui il tuo codice
    lista = []
    parola = parola.lower()
    esplora(dirname, parola, lista)
    return sorted(lista)

def esplora(dirname, parola, lista):
    for name in os.listdir(dirname):
        if name[0] in '._': continue
        fullname = f"{dirname}/{name}"
        if os.path.isdir(fullname):
            esplora(fullname, parola, lista)
        elif fullname.endswith('txt'):
            with open(fullname) as F:
                testo = F.read().lower()
            quanti = testo.count(parola)
            if quanti:
                lista.append((fullname, quanti))
