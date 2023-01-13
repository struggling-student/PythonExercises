#!/usr/bin/env python3
# -*- coding: utf-8 -*-
################################################################################
################################################################################
################################################################################

""" Operazioni da svolgere PRIMA DI TUTTO:
 1) Salvare questo file come program.py
 2) Indicare nelle variabili in basso il proprio
    NOME, COGNOME e NUMERO DI MATRICOLA
"""

nome        = "NOME"
cognome     = "COGNOME"
matricola   = "MATRICOLA"

################################################################################
################################################################################
################################################################################
# ---------------------------- SUGGERIMENTI PER IL DEBUG --------------------- #
# Per eseguire solo alcuni dei test, si possono commentare le voci con cui la
# lista 'test' è assegnata alla fine di grade.py
#
# Per controllare lo stack trace degli errori, si può decommentare la linea
# dedicata in testlib.py (vedere il commento nel corpo della funzione runOne)
################################################################################


# ----------------------------------- EX.1 ----------------------------------- #

""" Es 1: 6 punti

Parte 1)
E' dato in ingresso un dizionario D che ha come chiave un intero
e come valore una lista di interi con ripetizioni.

D = {1: [2, 3, 4, 4, 4], 2: [3, 4, 5, 6]}

Si implementi la funzione ex1(D, list_rm) che restituisca il dizionario
"inverso" W in cui:
 - esiste una chiave per ogni intero presente nelle liste dei valori di D
 - i nuovi valori di W sono le chiavi di D che hanno generato la
   chiave di W, ripetute per quante volte la chiave di W è presente nel
   valore delle chiavi di D.

Il dizionario inverso W deve avere ciascuna lista associata alla
chiave, ordinata in modo che prima vi siano i numeri pari e poi i
dispari; a sua volta i pari sono ordinati in maniera decrescente e i
dispari in maniera crescente.

L'esempio sopra deve restituire:

    W = {6: [2], 4: [2, 1, 1, 1], 2: [1], 3: [2, 1], 5: [2]}

Parte 2) Si estenda la funzione ex1(D, list_rm) in modo che siano
cancellati dal dizionario D in maniera distruttiva tutti gli interi nei
valori di D che compaiono in list_rm. Se dopo aver rimosso i valori una
lista in D è vuota, allora la chiave corrispondente deve essere cancellata
dal dizionario.

Esempio: se D = {1: [2, 3, 4, 4, 4], 2: [3, 4, 5, 6]}
         e list_rm = [4, 3, 2, 5]
         D deve essere trasformato in maniera distruttiva in
         {2: [6]} in quanto sono tolti tutti i valori tranne il 6
         e D non contiene più la lista vuota associata alla chiave 1.
"""

def mysort(L, previous=False):
    # prima i pari  (resto 0) poi i dispari (resto 1)
    # i pari vanno poi ordinati in maniera descrescente mentre i dispari in maniera crescente
    return L if previous else sorted(L, key=lambda k: (k % 2, -k if k % 2 == 0 else k))


def ex1(D, list_rm):
    rez = {}
    keys = mysort(D.keys())
    for k in keys:
        for v in D[k]:
            rez[v] = rez.get(v, []) + [k]

    for k in D.keys():
        lista = D[k]
        for rm in list_rm:
            while rm in lista:
                lista.remove(rm)
                
    [D.pop(k) for k in list(D.keys()) if not D[k]]
    return rez
# ----------------------------------- EX.2 ----------------------------------- #


''' Ex 2: 8 punti
    Si implementi una funzione che prende in ingresso una stringa di
    caratteri 'path' e una lista di liste 'griglia' e restituisca una
    lista. La stringa rappresenta una sequenza di spostamenti da
    effettuare sulla griglia, immaginando di partire dall'elemento in
    alto a sinistra (0,0). Gli spostamenti possibili sono 'R' (destra/right),
    'L' (sinistra/left), 'U' (su/up), 'D' (giù/down) o 'S' (pausa/stay).
    La funzione restituisce la lista dei valori incontrati sulla griglia
    seguendo la sequenza di spostamenti 'path'.
    Se la sequenza prevede uno spostamento al di fuori della griglia, il
    valore da inserire si immagina essere quello che si incontra
    rientrando nella griglia dal punto opposto.
    Se la sequenza prevede un carattere diverso dagli spostamenti elencati,
    allora la lista deve interrompersi all'ultimo valore della sequenza
    prima della mossa non valida.

    Es:
        Immaginando che la griglia è la seguente:
            [[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 0, 1, 2]]
        Se la sequenza è 'RRDS',   la lista restituita sarà [2,3,7,7],
        Se la sequenza è 'RRUSRR', la lista restituita sarà [2,3,1,1,2,9],
        Se la sequenza è 'DDXUU',  la lista restituita sarà [5, 9].
'''

def clip(x, X):
    if x >= X:
        return 0
    if x < 0:
        return X-1
    return x


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, p):
        return Position(clip(self.x + p.x, Position.X),
                        clip(self.y + p.y, Position.Y))
    
    def __repr__(self):
        return f"{self.x},{self.y}"


def make_move(griglia, path, moves, pos):
    if not path:
        return []
    if path[0] not in moves:
        return []
    new_pos = pos + moves[path[0]]
    rez = [griglia[new_pos.y][new_pos.x]] + make_move(griglia, path[1:],
                                                      moves,
                                                      new_pos)
    return rez

def ex2(griglia, path):
    moves = dict(R=Position(+1, 0), L=Position(-1, 0), U=Position(0,
                 -1), D=Position(0, +1), S=Position(0, 0))
    Position.X, Position.Y = len(griglia[0]), len(griglia)
    rez = make_move(griglia, path, moves, Position(0, 0))
    return rez


# ----------------------------------- EX.3 ----------------------------------- #

''' Ex 3: 9 punti
    Si implementi una funzione ricorsiva che prende in ingresso la
    radice di un albero e un intero. L'albero è realizzato attraverso
    istanze della classe BinaryTree definita nel file tree.py.
    La funzione ritorna il prodotto delle somme di tutte i nodi che sono
    un figlio sinistro per le somme di tutti i nodi che sono figlio destro
    a una profondità pari all'intero depth ricevuto in input.
    Si assume che la radice è a profondità 0.

    Es:

        ______5______                        ______2______
       |             |                      |             |
       8__        ___2___                __ 7__        ___5___
          |      |       |              |      |      |       |
          3      9       1             _4_     3_    _0_     _5_
                                      |   |      |  |   |   |   |
                                      2   -1     1  8   3   2   9

    Se l'albero è quello di sinistra e p=2, la funzione ritorna il valore
    9*(1+3)=36.
    Se l'albero è quello di destra e p=3, la funzione ritorna il valore
    (2+8+2)*(-1+1+3+9)=144.
    '''
from tree import BinaryTree

def prod_sum(root, depth, i=0):
    if i == depth - 1:
        return root.sx.valore if root.sx else 0, root.dx.valore if root.dx else 0
    LoL, LoR = prod_sum(root.sx, depth, i+1) if root.sx else (0, 0)
    RoL, RoR = prod_sum(root.dx, depth, i+1) if root.dx else (0, 0)
    somma = (LoL+RoL, LoR+RoR)
    return somma if i != 0 else somma[0]*somma[1]

def ex3(root, depth):
    return prod_sum(root, depth)


# ----------------------------------- EX.4 ----------------------------------- #

''' Ex 4: 9 punti
    Si implementi una funzione ricorsiva o che usa funzioni/metodi ricorsivi
    che prende in ingresso due percorsi (dirin e dirout) e un intero 'depth' 
    e crea all'interno della directory 'dirout' un file per ogni file di testo (.txt) 
    raggiungibile dal percorso 'dirin' percorrendo esattamente 'depth' sottodirectory.
    La struttura di sottodirectory che contengono il file deve essere ricreata
    sotto dirout.

    Ogni file da creare all'interno dei 'dirout' avrà lo stesso contenuto
    del file originario, ma con il minuscolo/maiuscolo invertito (ovvero
    ogni lettera minuscola sarà presente come maiuscola e viceversa).
    I caratteri non alfabetici vanno mantenuti tal quali.
    La funzione ritorna il numero totale di byte scritti all'interno
    dei file creati in 'dirout'. Si assuma che tutti i nomi di file
    raggiungibili nelle sottodirectory di 'dirin' siano univoci.

    NOTA: possono esservi utili le funzioni: os.listdir, os.path.join,
    os.path.isfile, os.mkdir, os.path.exists ...
    NOTA: è proibito usare la funzione os.walk

'''

import os

def create_dir(dirin, dirout, depth, i=0):
    somma = 0
    if depth == i:
        write_dir = '/'.join([dirout] + dirin.split('/')[-depth:])
        for item in os.listdir(dirin):
            full_path = dirin+'/'+item
            if os.path.isfile(full_path) and full_path.endswith('.txt'):
                os.makedirs(write_dir, exist_ok=True)
                write_file = write_dir+'/'+item
                with open(full_path) as fr, open(write_file, mode='wt') as fw:
                    print(fr.read().swapcase(), file=fw, end='')
                somma += os.stat(write_file).st_size
    else:
        for item in os.listdir(dirin):
            if os.path.isdir(dirin+'/'+item):
                somma += create_dir(dirin+'/'+item, dirout, depth, i=i+1)
    return somma


def ex4(dirin, dirout, depth):
    return create_dir(dirin, dirout, depth)
    ### INSERIRE QUI IL CODICE ###

# --------------------------------------------------------------------------- #

if __name__ == '__main__':
    pass
    ### INSERIRE QUI I VOSTRI TEST ###

