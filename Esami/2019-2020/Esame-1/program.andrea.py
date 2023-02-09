################################################################################
################################################################################
################################################################################

''' ATTENZIONE!!! INSERITE QUI SOTTO IL VOSTRO NOME, COGNOME E MATRICOLA '''

nome        = "NOME"
cognome     = "COGNOME"
matricola   = "MATRICOLA"

################################################################################
################################################################################
################################################################################

'''
Es 2: punti 6.

Si progetti la funzione che es2(fname) che, prende in input 
l'indirizzo di un file di testo  e restituisce una  lista di interi. 
Ciascuna riga del file contiene una espressione aritmetica del tipo somma di prodotti di interi positivi.
Ad esempio
    3 + 5 * 2 * 4 + 2 * 7
 
Ciascuna riga del file tranne l'ultima termina con un'andata a capo.
Si veda ad esempio il file espressioni1.txt.
La lista da restituire ha tanti elementi quante sono 
le righe del file di testo e, in posizione i, contiene l'intero risultante dall'esecuzione della
espressione aritmetica presente nella riga i -ma del file.

NOTA: è proibito usare la funzione eval o similari per valutare la stringa.

Ad esempio per il file di cinque righe espressioni1.txt la lista da produrre e' 
[482156580588, 6064232672398893380837, 941824502495832474, 316431, 4842258225]
'''

def es2(fname):
    # inserisci qui il tuo codice
    with open(fname, encoding='utf8') as F:
        L = []
        for line in F:
            somma = 0
            for prodotto in line.split('+'):
                pro = 1
                for numero in prodotto.split('*'):
                    pro *= int(numero)
                somma += pro
            L.append(somma)
        return L

#####################################################################################


'''    
    Es 4: punti 9
    
    Abbiamo immagini che contengono su sfondo nero cammini di color bianco 
    che non si intrecciano ne' si toccano e sono formati da segmenti orizzontali 
    o verticali consecutivi.
    Si veda ad Esempio l'immagine f4c.png.
    Progettare la  funzione es4(fname1) che prende in input l'indirizzo 
    di un file .png. e restituisce un insieme di quadruple di interi. 
    L'insieme  deve contenere 
    una quadrupla per ogni cammino presente nell'immagine. 
    Se il cammino ha come estremi i due pixel (w1,h1) e (w2,h2), la quadrupla  contiene 
    nell'ordine i quattro interi w1,h1, w2,h2  
    I due pixel devono comparire nella quadrupla ordinati per colonna crescente (vale a dire 
    w1 <= w2) ed a parita' di colonna per riga crescente (vale a dire (h1<=h2).
    
    Ad esempio per l'immagine f4c.png l'insieme restituito  sara' 
    {(20, 20, 99, 20), (20, 40, 20, 50), (30, 60, 70, 70)} 
    
    Per caricare e salvare i file PNG si devono usare load e 
    save della libreria immagini.
    '''
import immagini

def es4(fname1):
    img = immagini.load(fname1)
    return cerca_percorsi(img)

def cerca_percorsi(img):
    bianco = (255, 255, 255)
    # tutti i pixel bianchi
    pixels = { (x,y): {(x,y,)} 
                    for y, riga   in enumerate(img) 
                    for x, colore in enumerate(riga)
                    if colore == bianco}
    vicinato = [ (-1,0), (+1,0), (0,-1), (0,+1) ]
    changed = True
    while changed:
        changed = False
        for (x,y), vicini in pixels.items():
            for dx,dy in vicinato:
                X, Y = x+dx, y+dy
                # se un vicino è bianco
                if (X,Y) in pixels:
                    #unisco i miei vicini ai suoi
                    assieme = vicini.union(pixels[X,Y])
                    # e li setto come vicini di tutto il gruppo
                    for xx,yy in assieme:
                        if pixels[xx,yy] != assieme:
                            pixels[xx,yy] = assieme
                            changed = True
    # tengo solo gli insiemi diversi
    connessi = set( tuple(sorted(S)) for S in pixels.values())
    #print("XXX", len(pixels.values()), len(connessi))
    #return set()
    all_estremi  = []
    for connesso in connessi:
        estremi = []
        for x,y in connesso:
            count = 0
            for dx,dy in vicinato:
                X, Y = x+dx, y+dy
                if (X,Y) in connesso:
                    count += 1
            if count == 1:
                # gli estremi hanno un solo vicino
                estremi.append((x,y,))
        assert len(estremi) == 2
        estremi.sort()
        (x1,y1),(x2,y2) = estremi
        all_estremi.append((x1,y1,x2,y2))
    return set(all_estremi)

############################################################################

import albero

'''
    Es. 5: punti 6

    Si definisca la funzione es5(r) ricorsiva (o che fa uso 
    di funzioni o metodi ricorsive/i) che riceve come parametro la radice r di un albero 
    formato da nodi del tipo Nodo definito nella libreria albero.py e 
    restituisce un dizionario.
    Il dizionario contiene come chiave le altezze in cui sono presenti nodi dell'albero
    e associata ad ogni altezza c'e' la lista  coi valori dei nodi che nell'albero
    si trovano a quell'altezza. La lista non contiene duplicati e i suoi valori devono 
    essere ordinati in modo crescente. 

    Ad esempio per l'albero:
                    10                                       
             _______|______                              
            |              |                           
            3              3                           
         ___|___        ___|__                    
        |       |      |      |                
        2       1      8      1                  

   la funzione e5 restituisce il dizionario {0:[10], 1:[3],2:[1,2,8]}


    NOTA: definite le vostre sottofunzioni a livello esterno altrimenti non passate 
          il test di ricorsione
'''

def es5(r):
    # inserisci qui il tuo codice
    dizio = {}
    traversa(r, 0, dizio)
    for h in dizio: dizio[h] = sorted(dizio[h])
    return dizio

def traversa(r, h, dizio):
    if h not in dizio: dizio[h] = set()
    dizio[h].add(r.id)
    for s in r.f:
        traversa(s,h+1,dizio)

  
###########################################################################

'''
    Es. 7: punti 9
    
    Si vogliono estrarre dei frammenti di testo da file che sono contenuti in una directory.
    Si realizzi la funzione ricorsiva (o che usa funzioni ricorsive) es7(dirname, ext) che
    riceve come argomenti il nome di una directory (dirname) e l'estensione (ext) dei file cercati.
    La funzione esplora la directory dirname e ritorna un dizionario in cui:
        - le chiavi sono i path completi dei file che hanno estensione 'ext' indipendentemente dalle maiuscole/minuscole
        - i valori sono delle stringhe che contengono i primi 10 caratteri dei file individuati
    Ignorate tutti i file e directory che iniziano con '.' oppure '_'
    
    
    NOTA: è proibito usare la funzione os.walk
    NOTA: definite le vostre sottofunzioni a livello esterno altrimenti non passate 
          il test di ricorsione
'''    

import os
def es7(dirname, ext): 
    dizio = {}
    for fn in os.listdir(dirname):
        if fn[0] in '._': continue
        filename = f'{dirname}/{fn}'
        if os.path.isfile(filename):
            if filename[-3:].lower() == ext.lower():
                with open(filename, encoding='utf8') as F:
                    dizio[filename] = F.read(10)
        else:
            dizio.update(es7(filename, ext))
    return dizio
