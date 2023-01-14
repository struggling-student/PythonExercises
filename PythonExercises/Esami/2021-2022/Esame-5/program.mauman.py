#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

# Operazioni da svolgere PRIMA DI TUTTO:
# 1) Salvare questo file come program.py
# 2) Indicare nelle variabili in basso il proprio
#    NOME, COGNOME e NUMERO DI MATRICOLA

nome        = "Maurizio"
cognome     = "Mancini"
matricola   = "12345678"

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

Si scriva una funzione ex1(Q, file_db, k) che prende in ingresso una
tupla Q, file_db che punta ad un file di testo, mentre k e' un
intero. Q e' una tupla (x, y) che indica le coordinate del punto di
query. Invece file_db contiene punti 2D su ogni riga. Ogni riga
contiene le coordinate intere x e y separate da uno spazio, come ad


esempio:

  -5 -5
  10 5

La funzione deve leggere il contenuto del file. Dato il punto Q, si
deve cercare gli indici dei k punti piu vicini a Q in file_db. Per la
distanza fra (x1, y1) e (x2, y2) si usi:
(x1-x2)² + (y1-y2)²

Ad esempio, se k=2 e Q=(-5, -5) e file_db contiene:

  1 1
  -3 -5
  -5 -3
  20 10

allora gli indici e le distanze di file_db rispetto a Q sono:

 | indice |  x |  y | dist |
 |      0 |  1 |  1 | 72   |
 |      1 | -3 | -5 | 4    |
 |      2 | -5 | -3 | 4    |
 |      3 | 20 | 10 | 850  |

I due vicini a Q sono la lista [2, 1] in quanto hanno le k=2 distanze
minori.  In caso di parita' sulla distanza, come in questo caso, si
ritornano gli indici dal piu grande al piu piccolo.

Si ritorni la lista che contiene i k indici vicini come sudetto.
Se in ingresso abbiamo Q=(-5, -5) e db_00.txt e k=2, si deve ritornare:

 [2, 1]

NOTA: vi suggeriamo con forza di spezzare il vostro codice in funzioni
semplici.
"""



def ex1(Q, file_db, k):
    file_db = open(file_db, "r", encoding="utf8")
    distances = []
    index = 0
    for row in file_db:
        point = tuple([int(x) for x in row.split()])
        distance = (Q[0] - point[0]) ** 2 + (Q[1] - point[1]) ** 2
        distances.append((distance, index))
        index += 1
    distances.sort(key = lambda x : (x[0], -x[1]))
    return [x[1] for x in distances[0:k]]
    file_db.close()



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
    - per ogni riga contenente esattamente tre pixel, è presente esattamente un
      segmento
    - per ogni riga con meno di tre pixel non c'è alcun segmento né pixel ma resta nera.
    - ogni segmento è in corrispondenza dei tre pixel della riga dell'immagine in 'img_in',
      presenti sulla stessa riga (esempio: se sulla riga y, ci sono i punti
                                  x1<x2<x3, il segmento andrà dal punto x1 al
                                  punto x3 e avrà lunghezza x3-x1+1)
    - ogni segmento è del colore dato dalla media dei tre colori di x1, x2, x3
      componente per componente (esempio: se le componenti R di x1, x2 e x3 sono
                                 rispettivamente 11, 22, 66, la componente R
                                 del colore del segmento sarà 33)
    
Le operazioni sui valori delle componenti vanno arrotondate con la funzione
int.

La funzione, inoltre, a partire dall'immagine salvata in 'img_out', ritorna il
MASSIMO numero di righe consecutive contenenti un segmento (3 punti)
(1 se tutte tutte le righe sono separate, 0 se nessuna riga contiene segmenti).

Esempio: ex2('img_1.png', 'img1_out.png') dovrà salvare in 'out21.png' un'immagine
         uguale a quella di 'img1_exp.png' e ritornare il valore 18

NOTA: vi suggeriamo con forza di spezzare il vostro codice in funzioni semplici.
"""

import images

def ex2(img_in, img_out):
    input = images.load(img_in)
    result = [[(0, 0, 0) for x in range(len(input[0]))] for y in range(len(input))]
    maxlines = 0
    countlines = 0
    for y in range(len(input)):
        pp = []
        pp_c = []
        for x in range(len(input[y])):
            point = input[y][x]
            if point != (0, 0, 0):
                pp.append(point)
                pp_c.append(x)

        if len(pp) == 3:
            color = (int((pp[0][0] + pp[1][0] + pp[2][0])/3), int((pp[0][1] + pp[1][1] + pp[2][1])/3), int((pp[0][2] + pp[1][2] + pp[2][2])/3))
            pp_c.sort()
            for x in range(pp_c[0], pp_c[2] + 1):
                result[y][x] = color
            countlines += 1
        else:
            if maxlines < countlines:
                maxlines = countlines
            countlines = 0
    images.save(result, img_out)
    return maxlines

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

def rec_scan(folder, k):
    items = os.listdir(folder)
    rez = {}
    for item in items:
        full_path = folder + '/' + item
        if os.path.isdir(full_path):
            rez = rez | rec_scan(full_path, k)
        else:
            if full_path[-4:] == ".txt":
                sum = 0
                file = open(full_path, "r", encoding="utf8")
                for row in file:
                    row = row.strip()
                    tok = row.split(" ")
                    for t in tok:
                        if t == "":
                            continue
                        flag = True
                        for c in t:
                            if not c.isnumeric():
                             flag = False
                             break
                        if flag:
                            sum = sum + int(t)
                if sum % k == 0:
                    rez[full_path] = sum
    return rez

def ex3(path, k):
    rez = rec_scan(path, k)
    return rez


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

class Tree:
    def __init__(self, value):
        self.value = value
        self.children = []

    def is_leaf(self):
        if self.children == []:
            return True
        return False

    def addChild(self, subtree):
        self.children.append(subtree)

    def __str__(self, prefix=""):
        res = prefix + self.value + "\n"
        prefix = prefix + "|="
        for c in self.children:
            res += c.__str__(prefix)
        return res

    def previsit(self):
        if self.is_leaf():
            res = [self.value]
        else:
            res = []
        for c in self.children:
            res = res + c.previsit()
        return res

def recurCreateTree(start, words):
    node = Tree(start)
    for w in words:
        if start[-1] == w[0]:
            newlist = words.copy()
            newlist.remove(w)
            node.addChild(recurCreateTree(start + w[1:], newlist))
    return node

def ex4(start, words, out=None): # non dovremmo togliere il terzo parametro?
    t = recurCreateTree(start, words)
    res = set()
    for i in t.previsit():
        res.add(i)
    return res


###################################################################################
if __name__ == '__main__':
    start = 'dog'
    words = {'good', 'gost', 'goat', 'mood', 'doom', 'gasp', 'pool', 'long', 'loud'}
    t = ex4(start, words)
    print(t)