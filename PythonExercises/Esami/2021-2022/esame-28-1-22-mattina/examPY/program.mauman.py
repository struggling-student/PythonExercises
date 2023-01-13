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

nome        = "Maurizio"
cognome     = "Mancini"
matricola   = "12345678"

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
I valori vanno aggiunti nelle liste di W nell'ordine in cui appaiono le
chiavi di D e per ciascuna chiave nell'ordine in cui appaiono i suoi valori.

L'esempio sopra deve restituire:

    W = {2: [1], 3: [1, 2], 4: [1, 1, 1, 2], 5: [2], 6: [2]}

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
def ex1(D, list_rm):
    result = {}
    for key in D.keys():
        L = D[key]
        for item in L:
            if item not in result:
                result[item] = [key]
            else:
                result[item].append(key)
    keyslist = list(D.keys())
    for key_i in range(len(keyslist)):
        for item in list_rm:
            while item in D[keyslist[key_i]]:
                D[keyslist[key_i]].remove(item)
        if len(D[keyslist[key_i]]) == 0:
            toremove = keyslist[key_i]
            D.pop(toremove)
    print(D)
    return result

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
def ex2(griglia, path):
    x = 0
    y = 0
    stop = False
    move_i = 0
    result = []
    while move_i < len(path) and stop is False:
        move = path[move_i]
        if move == "R":
            x += 1
        elif move == "L":
            x -= 1
        elif move == "U":
            y -= 1
        elif move == "D":
            y += 1
        elif move != "S":
            stop = True
        if stop is False:
            x = x % len(griglia[0])
            y = y % len(griglia)
            result.append(griglia[y][x])
        move_i += 1
    return result

# ----------------------------------- EX.3 ----------------------------------- #

''' Ex 3: 9 punti
    Si implementi una funzione ricorsiva che prende in ingresso la
    radice di un albero e un intero. L'albero è realizzato attraverso
    istanze della classe BinaryTree definita nel file tree.py.
    La funzione ritorna la somma di tutte i nodi che sono
    un figlio sinistro moltiplicata per la somma di tutti i nodi che sono figlio destro
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
import tree

def recurSum(root, wantedlevel, currentlevel, sxlist, dxlist):
    if currentlevel == wantedlevel - 1:
        if root.sx is not None:
            sxlist.append(root.sx.valore)
        if root.dx is not None:
            dxlist.append(root.dx.valore)
        return
    recurSum(root.dx, wantedlevel, currentlevel + 1, sxlist, dxlist)
    recurSum(root.sx, wantedlevel, currentlevel + 1, sxlist, dxlist)
    if currentlevel == 0:
        return sum(sxlist) * sum(dxlist)



def ex3(root, depth):
    sxlist = []
    dxlist = sxlist.copy()
    return recurSum(root, depth, 0, sxlist, dxlist)


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

def walkAndCreate(dirin, dirout, depth):
    if depth == -1:
        return
    items = os.listdir(dirin)
    # if not os.path.exists(dirout):
        # os.mkdir(dirout)
    for item in items:
        if os.path.isfile(os.path.join(dirin, item)):
            if depth == 0 and item[-4:] == ".txt":
                if not os.path.exists(dirout):
                    os.makedirs(dirout)
                filein = open(os.path.join(dirin, item), "r", encoding="utf8")
                fileout = open(os.path.join(dirout, item), "w", encoding="utf8")
                lines = filein.readlines()
                result = ""
                for l in lines:
                    for c in l:
                        if c.isalpha():
                            if c.islower():
                                result += c.upper()
                            else:
                                result += c.lower()
                        else:
                            result += c
                fileout.writelines(result)
                filein.close()
                fileout.close()
        else:
            walkAndCreate(os.path.join(dirin, item), os.path.join(dirout, item), depth - 1)

def ex4(dirin, dirout, depth):
    walkAndCreate(dirin, dirout, depth)

# --------------------------------------------------------------------------- #

if __name__ == '__main__':
    # ex1({1: [2, 3, 4, 4, 4], 2: [3, 4, 5, 6]}, [4, 3, 2, 5])
    grid = [[2, 1, 7, 1, 0],
            [3, -1, 2, 6, 6],
            [5, 1, 3, 2, 9],
            [9, 0, 4, 1, -2],
            [-2, 9, 1, -2, 5]]
    path = 'SDDDDDRDDDDDRDDDDDRDDDDDRDDDDDR'
    # print(ex2(grid, path))

    root = tree.BinaryTree.fromList([2, [7, [4, [2, None, None], [-1, None, None]], [3, None, [1, None, None]]],
                                     [5, [0, [8, None, None], [3, None, None]], [5, [2, None, None], [9, None, None]]]])
    depth = 3
    expected = 144
    # print(ex3(root, depth))

    dirin = 'A'
    dirout = 'test'
    depth = 2
    expected = (1730, ['B/E/x10.txt', 'B/D/x11.txt', 'B/E/x12.txt', 'B/D/xx10.txt'])
    print(ex4(dirin, dirout, depth))

