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

def ex1(D, val_to_remove):
    # costruzione del dizionario inverso D
    W = {}
    for k,vals in D.items():
        for v in vals:
            W[v] = W.get(v, []) + [k]   # se v non esiste in W si inizia con []

    # ordino tutte le liste di valori
    for k in W:
        # prima pari in discesa (-x) poi dispari in salita (x)
        W[k].sort(key=lambda x: (-x if x%2==0 else x))
   
    # DOPO aver creato W elimino da D i valori proibiti
    for k,v in D.items():
        for x in val_to_remove:
            while x in v:
                v.remove(x)
    # e poi elimino le chiavi che non hanno più valori
    for k in list(D.keys()):
        if not D[k]:
            del D[k]
    # e torno W
    return W

# ----------------------------------- EX.2 ----------------------------------- #

def ex2(griglia, path):
    ''' Si implementi una funzione che prende in ingresso una stringa di
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
        Se la sequenza è 'RRDS', la lista restituita sarà [2,3,7,7],
        Se la sequenza è 'RRUSRR', la lista restituita sarà [2,3,1,1,2,9],
        Se la sequenza è 'DDXUU', la lista restituita sarà [5, 9].

    '''
    ### INSERIRE QUI IL CODICE ###
    pass
    # definisco gli incrementi da fare a x,y a seconda della lettera
    incrementi = { 'R':(1,0), 'L':(-1,0), 'U':(0,-1),'D':(0,1), 'S':(0,0) }
    x = y = 0                               # posizione iniziale
    visitate = []                           # lista di caselle visitate
    W,H = len(griglia[0]),len(griglia)      # dimensioni della griglia
    for step in path:                       # eseguo ciascuno step
        if step in incrementi:              # se è lettera conosciuta
            dx,dy = incrementi[step]        # prendo gli incrementi da applicare
            x += dx                         # incremento x
            x %= W                          # e se sbordo rientro dal lato opposto
            y += dy                         # lo stesso per y
            y %= H
            visitate.append(griglia[y][x])  # aggiungo la nuova casella alle visitate
        else:                               # altrimenti è sconosciuta
            break                           # e smetto
    return visitate                         # e torno la lista di caselle visitate

# ----------------------------------- EX.3 ----------------------------------- #

from tree import BinaryTree

def ex3(root, depth):
    ''' Si implementi una funzione ricorsiva che prende in ingresso la
    radice di un albero e un intero. L'albero è realizzato attraverso
    istanze della classe AlberoBinario definita nel file albero.py.
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
    36.
    Se l'albero è quello di destra e p=3, la funzione ritorna il valore
    144.
    '''
    ### INSERIRE QUI IL CODICE ###
    pass
    # esploro l'albero e ricavo la somma sinistra e destra dei nodi al livello depth 
    sx,dx = somma_sx_dx(root,depth)
    return sx*dx                                    # ne torno il prodotto

def somma_sx_dx(radice,d):
    if not radice:                                  # una foglia
        return 0,0                                  # ha somma sinistra e destra zero
    if d > 1:                                       # se ancora non solo a livello depth
        sx1,dx1 = somma_sx_dx(radice.sx, d-1)       # scendo nel sottoalbero sinistro
        sx2,dx2 = somma_sx_dx(radice.dx, d-1)       # e nel destro
        return sx1+sx2,dx1+dx2                      # e torno le due somme sinistri e destri
    # altrimenti sono al livello giusto
    sx = radice.sx.valore if radice.sx else 0       # sx è il valore del nodo sinistro se c'è
    dx = radice.dx.valore if radice.dx else 0       # dx del nodo destro se c'è (altrimenti 0)
    return sx,dx                                    # torno le due somme


# ----------------------------------- EX.4 ----------------------------------- #

import os

def ex4(dirin, dirout, depth):
    '''  Si implementi una funzione ricorsiva che prende in ingresso due
    percorsi (dirin e dirout) e un intero 'depth' e crea all'interno della
    directory 'dirout' un file per ogni file di testo raggiungibile dal
    percorso 'dirin' percorrendo esattamente 'depth' sottodirectory.

    Ogni file da creare all'interno dei 'dirout' avrà lo stesso contenuto
    del file originario, ma con il minuscolo/maiuscolo invertito (ovvero
    ogni lettera minuscola sarà presente come maiuscola e viceversa).
    I caratteri non alfabetici vanno mantenuti tal quali.
    La funzione ritorna il numero totale di byte scritti all'interno
    dei file creati in 'dirout'. Si assuma che tutti i nomi di file
    raggiungibili nelle sottodirectory di 'dirin' siano univoci.

'''
    ### INSERIRE QUI IL CODICE ###
    pass
    # se il path dirout non esiste creo la directory
    if not os.path.exists(dirout): os.mkdir(dirout)
    numbytes = 0                                # numero di bytes scritti
    for name in os.listdir(dirin):              # per ogni nome di file in dirin
        fullnamein  = dirin  + '/' + name       # fullname da leggere
        fullnameout = dirout + '/' + name       # fullname da scrivere
        if os.path.isdir(fullnamein):           # se si tratta di una directory
            if depth:               # e se NON sono ancora arrivato alla profondità voluta
                numbytes += ex4(fullnamein, fullnameout, depth-1)   # scendo di un livello
        else:                                   # altrimenti è un file
            if not depth:                       # se sono alla profondità giusta (0)
                if name.endswith('.txt'):       # se il filename finisce con '.txt'
                    with open(fullnamein) as FIN:                   # apro il file da leggere
                        with open(fullnameout, mode='w') as FOUT:   # apro il file da scrivere
                            text = FIN.read()                       # ne leggo il testo
                            FOUT.write(text.swapcase())             # lo scrivo scambiando case
                            numbytes += len(text)                   # e incremento il #bytes scritti
    return numbytes                             # finita la directory torno quanti bytes ho scritto



##########################################################################################
