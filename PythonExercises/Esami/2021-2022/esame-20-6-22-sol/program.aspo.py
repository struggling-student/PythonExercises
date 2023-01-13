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
"""


def read_data(file_in):
    with open(file_in, mode='rt', encoding='utf8') as fr:
        data = []
        for idx, line in enumerate(fr):
            x, y = line.split()
            data.append((idx, (int(x), int(y))))
        return data


def ex1(file_query, file_db, k):
    query = read_data(file_query)
    db = read_data(file_db)  # (idx, (x,y))
    rez = []
    for qq in query:
        idxs_pts = sorted(db,
                          key=lambda p:
                          (sum(map(lambda x1, x2: (x1-x2)**2, p[1], qq[1])),
                           -p[0]))[:k]
        rez.append(list(map(lambda a: a[0], idxs_pts)))
    return rez


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
    - ogni segmento è in corrispondenza di tre pixel dell'immagine in 'img_in',
      presenti sulla stessa riga (esempio: se sulla riga y, ci sono i punti
                                  x1<x2<x3, il segmento andrà dal punto x1 al
                                  punto x3 e avrà lunghezza x3-x1+1)
    - ogni segmento è del colore dato dalla media dei tre colori di x1, x2, x3
      componente per componente (esempio: se le componenti R di x1, x2 e x3 sono
                                 rispettivamente 11, 22, 66, la componente R
                                 del colore del segmento sarà 33)
    - una riga con meno di tre pixel non ha alcun segmento né pixel.
    
Le operazioni sui valori delle componenti vanno arrotondate con la funzione
int.

La funzione, inoltre, a partire dall'immagine salvata in 'img_out', ritorna il
numero di righe consecutive contenenti un segmento (3 punti).

Esempio: ex2('e21.png', 'out21.png') dovrà salvare in 'out21.png' un'immagine
         uguale a quella di 'expected21.png' e ritornare il valore X
"""

import images

def fatti_riga(riga):
    x = []
    newrow = [(0,0,0)]*len(riga)
    for j in range(len(riga)):
        if riga[j] != (0,0,0):
            x.append(j)
    if len(x) < 3:
        return newrow
    maxl = x[2]-x[0]
    maxx = x[0:3]
    for i in range(1, len(x)-2):
        l = x[i+2] - x[i]
        if l > maxl:
            maxl = l
            maxx = x[i:i+3]
    # print(x, maxx)
    color = tuple(int(sum(map(lambda x: riga[x][i], maxx))/3) for i in (0,1,2))
    newrow[maxx[0]:maxx[2]+1] = [color]*(maxl+1)
    return newrow
            

def ex2(img_in, img_out):
    img = images.load(img_in)
    img_o = []
    righe = []
    for riga in img:
        img_o.append(fatti_riga(riga))
        righe.append(1 if len(set(img_o[-1])-set([(0,0,0)]))>0 else 0)
    images.save(img_o, img_out)
    print(righe)
    m = 0
    c = 0
    for i in righe:
        if i>0:
            c+=1
        else:
            if c > m:
                m=c
            c = 0
    return m


def ex2(img_in, img_out):
    img = images.load(img_in)
    img_o = []
    righe = []
    for riga in img:
        img_o.append(fatti_riga(riga))
        if len(set(img_o[-1])-set([(0,0,0)]))>0:
            righe.append(1+sum(righe[-1:]))
        else:
            righe.append(0)
    # img_o[-1][-1]=(1,2,3)
    images.save(img_o, img_out)
    # print(righe)
    return max(righe)

# %% ----------------------------------- EX.3 --------------------------------- #

"""
Esercizio 3: 8 punti 
Scrivere una funzione ricorsiva o che fa uso di funzioni ricorsive che
prende in input una stringa che rappresenta il nome di una directory e
un intero k e restituisce un dizionario.

All'interno del dizionario le chiavi sono delle stringhe che rappresentano
i percorsi di alcuni file con estenzione '.txt', relativi alla directory in
input.
Il valore associato ad una chiave è il numero intero dato dalla somma
di tutte le stringhe numeriche contenute nel file indicato dalla chiave.

ATTENZIONE: devono essere presenti nel dizionario soltanto quei file che
contengono delle stringhe numeriche la cui somma è un valore multiplo
dell'intero k preso in input.


Es: se un file contiene "34 casa c4a 22", la somma delle stringhe numeriche
    in esso contenute è 34+22=56 (infatti c4a *non* è una stringa numerica).
    
Non è consentito utilizzare la funzione os.walk.
Per valutare se una stringa è numerica si può utilizzare il metodo isnumeric
"""

import os


def check_file(file):
    with open(file) as f:
        text = f.read()
    return sum([int(w) for w in text.split() if w.isnumeric()])

def ex3(path, k):
    d = {}
    for file in os.listdir(path):
        ffile = path + '/' + file
        if os.path.isdir(ffile):
            d.update(ex3(ffile, k))
        if ffile.endswith('.txt') and os.path.isfile(ffile):
            i = check_file(ffile)
            if i % k == 0:
                d[ffile]=i
    return d

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
Per massimale si intende che una stringa non può essere più ulteriormente
concatenata con alcuna altra stringa rimasta in words, dopo tutti gli
accodamenti.

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

Le stringhe con (*) sono massimali rispetto al set words iniziale.

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
         
Le stringhe con (*) sono massimali rispetto al set words iniziale.

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

'''
def ex4(start, words):
    s = ex4set(start, words)
    # if start[0]!='p':
    #     return s
    return sorted(s, key=lambda x: (len(x), x))

def ex4set(start, words):
    if len(words) == 0:
        return {start}
    ret = set()
    append_list = [w for w in words if start.endswith(w[0])]
    if len(append_list) == 0:
        return {start}
    for word in append_list:
        ret.update(ex4(start[:-1]+word, words-{word}))
    return ret
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
