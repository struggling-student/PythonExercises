#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

# Operazioni da svolgere PRIMA DI TUTTO:
# 1) Salvare questo file come program.py
# 2) Indicare nelle variabili in basso il proprio
#    NOME, COGNOME e NUMERO DI MATRICOLA

nome        = "NOME"
cognome     = "COGNOME"
matricola   = "MATRICOLA"

################################################################################
################################################################################
################################################################################
# ---------------------------- SUGGERIMENTI PER IL DEBUG --------------------- #
# Per eseguire solo alcuni dei test, si possono commentare le voci con cui la
# lista 'test' è assegnata alla FINE di grade.py
#
# Per debuggare le funzioni ricorsive potete disattivare il test di ricorsione
# settando DEBUG=True nel file grade.py
#
# DEBUG=True vi attiva anche lo STACK TRACE degli errori per sapere il numero
# di linea di program.py che genera l'errore.
################################################################################

# ----------------------------------- EX.1 ----------------------------------- #
"""
Esercizio 1: 6 punti

Si scriva una funzione ex1(file_query, file_db, k) che prende in
ingresso due stringhe file_query e file_db che puntano a due file di
testo, mentre k e' un intero. I file contengono punti in 2D su ogni
riga. Ogni riga contiene le coordinate intere x e y separate da uno
spazio, come ad esempio:

  -5 -5
  10 5

La funzione deve leggere il contenuto dei file. Per ogni punto Q nel
file_query, si deve cercare gli indici dei k punti piu vicini a Q in
file_db.  Per la distanza fra (x1, y1) e (x2, y2) si usi:
(x1-x2)² + (y1-y2)²

Ad esempio, se k=2 e Q=(-5, -5) e DB e':

  1 1
  -3 -5
  -5 -3
  20 10

allora gli indici e le distanze in DB rispetto a Q sono:

| indice |  x |  y | dist |
|      0 |  1 |  1 | 72   |
|      1 | -3 | -5 | 4    |
|      2 | -5 | -3 | 4    |
|      3 | 20 | 10 | 850  |

I due vicini a Q sono la lista [2, 1] in quanto hanno le k=2
distanze minori.  In caso di parita' sulla distanza, come in questo
caso, si ritornano gli indici dal piu grande al piu piccolo.

Si ritorni la lista che contiene le liste dei k indici vicini, per
ogni punto Q nel solito ordine in cui sono letti i punti Q dal
file_query.

Se in ingresso abbiamo query_00.txt e db_00.txt e k=2, si deve ritornare:

[[2, 1], [0, 3]]

NOTA: vi suggeriamo con forza di spezzare il vostro codice in funzioni semplici.

"""

def leggi_file(filename):
    with open(filename) as f:
        return [ [int(x) for x in riga.split()] for riga in f ]

def ex1(file_query, file_db, k):
    punti = leggi_file(file_query)
    db    = leggi_file(file_db)
    return [ indici(P,db,k) for P in punti ]

def distanza(p1,p2):
    x1,y1 = p1
    x2,y2 = p2
    return (x1-x2)**2 + (y1-y2)**2

def indici(punto, db, k):
    distanze = [ (i,distanza(punto, P)) for i,P in enumerate(db) ]
    ordinate = sorted(distanze, key=lambda i_d: (i_d[1], -i_d[0]))
    return [ i_d[0] for i_d in ordinate[:k] ]


# %% ----------------------------------- EX.2 ----------------------------------- #
"""
Esercizio 2: 6+3 punti

Scrivere una funzione che prenda in ingresso due nomi di file 'img_in'
e 'img_out'. 
La funzione (6 punti) deve leggere un'immagine png contenuta nel file 'img_in'
costituita da uno sfondo nero e da diversi pixel colorati e costruire e salvare
in un nuovo file 'img_out' un'immagine delle stesse dimensioni di quella
contenuta in img_in. L'immagine ha al più tre pixel per ogni riga.

La nuova immagine dovrà contenere dei segmenti orizzontali calcolati a partire
dall'immagine contenuta nel file 'img_in' nel seguente modo:
    - per ogni riga contenente almeno tre pixel, è presente esattamente un
      segmento
    - ogni segmento è in corrispondenza dei tre pixel della riga dell'immagine in 'img_in',
      presenti sulla stessa riga (esempio: se sulla riga y, ci sono i punti
                                  x1<x2<x3, il segmento andrà dal punto x1 al
                                  punto x3 e avrà lunghezza x3-x1+1)
    - ogni segmento è del colore dato dalla media dei tre colori di x1, x2, x3
      componente per componente (esempio: se le componenti R di x1, x2 e x3 sono
                                 rispettivamente 11, 22, 66, la componente R
                                 del colore del segmento sarà 33)
    - una riga con meno di tre pixel non ha alcun segmento né pixel ma resta nera.
    
Le operazioni sui valori delle componenti vanno arrotondate con la funzione
int.

La funzione, inoltre, a partire dall'immagine salvata in 'img_out', ritorna il
MASSIMO numero di righe consecutive contenenti un segmento (3 punti)
(1 se tutte tutte le righe sono separate, 0 se nessuna riga contiene segmenti).

Esempio: ex2('e21.png', 'out21.png') dovrà salvare in 'out21.png' un'immagine
         uguale a quella di 'expected21.png' e ritornare il valore X

NOTA: vi suggeriamo con forza di spezzare il vostro codice in funzioni semplici.
"""

import images

def ex2(img_in, img_out):
    img = images.load(img_in)
    W = len(img[0])
    H = len(img)
    img2 = [ [ (0,0,0) ] * W for _ in range(H) ]
    colorate = [ y for y,riga in enumerate(img) if colora(img2, y, riga) ]
    images.save(img2, img_out)
    return max_consec(colorate)

def colora( img, y, riga ):
    pixels = [ [x,C] for x,C in enumerate(riga) if C != (0,0,0) ]
    if len(pixels)==3:
        assert len(pixels) <= 3
        (x0,C0),(x1,C1),(x2,C2) = pixels
        colore = tuple( int(sum(RGB)/3) for RGB in zip(C0,C1,C2) )
        for x in range(x0,x2+1):
            img[y][x] = colore
        return True
    return False

def max_consec(Ys):
    if not Ys: return 0
    maxgroup = 0
    gruppo = 1
    last   = Ys[0]
    for y in Ys[1:]:
        if y-1 == last:
            gruppo += 1
        else:
            if gruppo > maxgroup:
                maxgroup = gruppo
            gruppo = 1
        last = y
    if gruppo > maxgroup:
        maxgroup = gruppo
    return maxgroup

# %% ----------------------------------- EX.3 --------------------------------- #

"""
Esercizio 3: 8 punti 
Scrivere una funzione ricorsiva o che fa uso di funzioni ricorsive che
prende in input una stringa che rappresenta il nome di una directory e
un intero k e restituisce un dizionario.

All'interno del dizionario le chiavi sono delle stringhe che rappresentano
i percorsi di alcuni file con estenzione '.txt', relativi alla directory in
input. USANDO '/' COME SEPARATORE.
Il valore associato ad una chiave è il numero intero dato dalla somma
di tutte le stringhe numeriche contenute nel file indicato dalla chiave.

ATTENZIONE: devono essere presenti nel dizionario soltanto quei file che
contengono delle stringhe numeriche la cui somma è un valore multiplo
dell'intero k preso in input.

FIXME: e se la somma è 0? è sempre multiplo.

Es: se un file contiene "34 casa c4a 22", la somma delle stringhe numeriche
    in esso contenute è 34+22=56 (infatti c4a *non* è una stringa numerica).
    
Non è consentito utilizzare la funzione os.walk.
Per valutare se una stringa è numerica si può utilizzare il metodo isnumeric

NOTA: vi suggeriamo con forza di spezzare il vostro codice in funzioni semplici.
"""

import os


def ex3(path, k):
    pass
    dizio = {}
    esplora(path, k, dizio)
    return dizio

def esplora(path,k,dizio):
    if os.path.isfile(path):
        if path.endswith('.txt'):
            process_file(path, k, dizio)
    else:
        for name in os.listdir(path):
            fullname = path + '/' + name
            esplora(fullname, k, dizio)

def process_file(path, k, dizio):
    with open(path, encoding='utf8') as F:
        parole = F.read().split()
        numeri = [ int(x) for x in parole if x.isdigit() ]
        somma = sum(numeri)
        if somma % k == 0:
            dizio[path] = somma

# %% ----------------------------------- EX.4 ----------------------------------- #
'''
Esercizio 4: 9 punti (6+3)

L'operazione di accodamento "§" fra due stringhe A e B è possibile se la stringa
A termina con il primo carattere della stringa B. Il risultato dell'operazione
A § B è simile alla concatenazione, soltanto che il primo carattere di B è
rimosso:  dog § good = dogood.

Scrivere una funzione ricorsiva o che fa uso di funzioni ricorsive che
prende in input una stringa start e un set di stringhe words e calcola
ricorsivamente tutte le possibili stringhe massimali che possono essere generate
da accodamenti successivi a partire dalla stringa start, rimuovendo le parole
accodate. 
    NOTA: con 'rimovendo le parole accodate' si intende che ogni volta che una parola in words
    è stata concatenata a start con successo, l'esplorazione di quel ramo dell'albero di gioco continua senza riusare quella parola.
    Si veda negli esempi sotto come viene aggiornato l'insieme di parole valide per ogni mossa dell'albero di gioco.
Per massimale si intende che una stringa non può essere più ulteriormente
concatenata con alcuna altra stringa rimasta in words, dopo tutti gli
accodamenti.

NOTA: vi suggeriamo con forza di spezzare il vostro codice in funzioni semplici.

Esempio: 'aa' {'abb', 'acc', 'bdd', 'be'}

aa {abb, acc, bdd, be}
|
|- § abb -- aabb {acc, bdd, be}
|  |
|  |- § bdd -- aabbdd(*) {acc, be}
|  |
|  |- § be -- aabbe(*) {acc, bdd}
|
|- § acc -- aacc(*) {abb, bdd, be}

Le stringhe con (*) sono massimali rispetto al set words CORRENTE.

Esempio: 'dog' {'good', 'gost', 'goat', 'mood', 'doom', 'gasp', 'pool', 'long', 'loud'}

dog {good, gost, goat, mood, doom, gasp, pool, loop}
|
|- § gost -- dogost(*) {good, goat, mood, doom, gasp, pool, loop}
|
|- § goat -- dogoat(*) {good, gost, mood, doom, gasp, pool, loop}
|
|- § good -- dogood {gost, goat, mood, doom, gasp, pool, long, loud}
|  |
|  |- § doom -- dogoodoom {gost, goat, mood, gasp, pool, long, loud}
|     |
|     |- § mood -- dogoodoomood(*) {gost, goat, gasp, pool, long, loud}
|
|- § gasp -- dogasp {good, gost, goat, mood, doom, pool, long, loud}
   |
   |- § pool -- dogaspool {good, gost, goat, mood, doom, long, loud}
      |
      |- § loud  -- dogaspooloud {good, gost, goat, mood, doom, long}
      |  |
      |  |- § doom -- dogaspooloudoom {good, gost, goat, mood, long}
      |     |
      |     |- § mood -- dogaspooloudoomood(*) {good, gost, goat, long}
      |
      |- § long -- dogaspoolong {good, gost, goat, mood, doom, loud}
         |
         |- § good -- dogaspoolongood {mood, gost, goat, doom, loud}
         |  |
         |  |- § doom -- dogaspoolongoodoom {mood, gost, goat, loud}
         |     |
         |     |- § mood -- dogaspoolongoodoomood(*) {gost, goat, loud}
         |
         |- § gost -- dogaspoolongost(*) {good, goat, mood, doom, loud}
         |
         |- § goat -- dogaspoolongoat(*) {good, gost, mood, doom, loud}
         
Le stringhe con (*) sono massimali rispetto al set words CORRENTE 
(non possono essere allungate ulteriormente).

La funzione deve ritornare l'insieme di tutte le stringhe che è possibile
generare (ovvero le foglie dell'albero di gioco), come un insieme (6 punti),
    oppure (+3 punti) come una lista ordinata in in cui:
    - le stringhe sono ordinate in modo crescente rispetto alla loro lunghezza
    - in caso di pari lunghezza, in ordine alfabetico.

Nell'esempio ex4('aa' ,{'abb', 'acc', 'bdd', 'be'}) la funzione ritorna l'insieme
{'aacc', 'aabbdd', 'aabbe'} (6 punti)
oppure la lista
['aacc', 'aabbe', 'aabbdd'] (9 punti)

Nell'esempio ex4('dog',  {'good', 'gost', 'goat', 'mood', 'doom', 'gasp', 'pool', 'long', 'loud'})
la funzione ritorna l'insieme
{'dogaspoolongoodoomood', 'dogaspooloudoomood', 'dogoodoomood', 'dogaspoolongost',
 'dogaspoolongoat', 'dogost', 'dogoat'} (6 punti)
oppure la lista 
['dogoat', 'dogost', 'dogoodoomood', 'dogaspoolongoat', 'dogaspoolongost', 'dogaspooloudoomood', 'dogaspoolongoodoomood'] (9 punti)

NOTA: vi suggeriamo con forza di spezzare il vostro codice in funzioni semplici.
'''
def ex4(start, words):
    pass
    words  = set(words)
    parole = set()
    genera_parole(start, words, parole)
    return sorted(parole, key=lambda x: (len(x), x))

def genera_parole(start, words, S):
    fine = start[-1]
    trovata = False
    for w in words:
        if w[0] == fine:
            nuova = start[:-1] + w
            newwords = words - { w }
            genera_parole(nuova, newwords, S)
            trovata = True
    if not trovata:
        S.add(start)



###################################################################################
if __name__ == '__main__':
    # inserisci qui i tuoi test
    print('*'*50)
    print('ITA\nDevi eseguire il grade.py se vuoi debuggare con il grader incorporato.')
    print('Altrimenit puoi inserire qui del codice per testare le tue funzioni ma devi scriverti i casi che vuoi testare')
    print('*'*50)
    print('ENG\nYou have to run grade.py if you want to debug with the automatic grader.')
    print('Otherwise you can insert here you code to test the functions but you have to write your own tests')
    print('*'*50)
