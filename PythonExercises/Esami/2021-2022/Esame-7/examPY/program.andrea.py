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
def ex1(file1, file2, file3):
    ''' Si implementi una funzione che prende in ingresso tre nomi di file
    e restituisce un numero intero.
    I parametri file1 e file2 sono stringhe contenenti i nomi di due file
    di testo. Questi file contengono, su ogni riga, una serie di stringhe
    separate da spazi, tabulazioni, virgole o punti e virgola.
    La funzione deve scrivere all'interno di un nuovo file indicato da
    file3 una riga per ogni riga di file1 la cui corrispondente riga in
    file2 ha almeno una stringa in comune. In particolare:
        - date le stringhe della riga i-esima di file1, se la riga i-esima
          di file2 contiene almeno una di tali stringhe, allora in file3
          sarà presente una riga con tutte le stringhe in comune.
        - Le stringhe in comune sono scritte nelle righe di file3 separate
          da uno spazio e ordinate per numero di caratteri crescente e, in
          caso di parità, in ordine alfabetico.
        - Le righe in file3 hanno lo stesso ordine delle righe di origine.
    La funzione ritorna una tupla in cui il primo e il secondo elemento
    sono, rispettivamente, il numero di stringhe e il numero di righe
    scritte in file3. '''
    ### INSERIRE QUI IL CODICE ###
    pass
    nstringhe = 0                                   # numero di parole scritte
    nrighe    = 0                                   # numero di righe scritte
    with open(file1, encoding='utf8') as F1:        # leggo da file1
        with open(file2, encoding='utf8') as F2:    # e da file2
            with open(file3, mode='w', encoding='utf8') as F3:  # e scrivo in file3
                for riga1, riga2 in zip(F1,F2):     # per ogni coppia di righe lette da F1 ed F2
                    parole1 = set(riga1.replace(',',' ').replace(';',' ').split())  # ottengo le parole di file1 come set
                    parole2 = set(riga2.replace(',',' ').replace(';',' ').split())  # e di file2
                    common  = parole1 & parole2     # quelle comuni sono l'intersezione dei due insiemi
                    if common:                      # se ce ne sono
                        nstringhe += len(common)    # incremento il numeri di parole scritte
                        nrighe    += 1              # ed il numero di righe
                        # e scrivo in file3 le parole comuni in ordine (spacchettando la lista nella print)
                        print(*sorted(common,key=lambda p: (len(p),p)), file=F3)
    return nstringhe, nrighe                        # quindi torno #parole e #righe

# ----------------------------------- EX.2 ----------------------------------- #

'''Ex. 4: 6 points
Write a function ex4(gridFilePath) that, given a NxN grid stored in a json file as
a list of lists, returns a positive integer. In the given grid, each cell
can have one of three values:
 - the value 0 representing an empty cell;
 - the value 1 representing a fresh orange;
 - the value 2 representing a rotten orange.
Every minute, any fresh orange that is horizontally or vertically adjacent to
a rotten orange becomes rotten.

The function must return the minimum number of minutes that must elapse
until no cell has a fresh orange. If that is impossible, it must return -1.

For example, given the grid:
[[2,1,1],
 [1,1,0],
 [0,1,1]]
the function will return 4.

While, given the grid:
[[2,1,1],
 [0,1,1],
 [1,0,1]]
the function will return -1.

'''
import json
def ex2(gridFilePath):
    # Enter your code here
    pass
    grid = json.load(open(gridFilePath))    # carico il file json
    return fastest_rot(grid)                # e ne calcolo il # di giorni

def fastest_rot(grid,level=0):              # ricorsivamente simulo l'evoluzione
    if rot(grid):                           # se tutta la cassetta è marcia
        return level                        # torno il numero di giorni
    else:                                   # altrimenti qualche arancia è sana
        rotted = rotting(grid)              # faccio marcire le prossime
        if rotted == grid:                  # se non è cambiato nulla
            return -1                       # torno -1 (undo dell'ultimo giorno)
        else:
            return fastest_rot(rotted, level+1) # altrimenti faccio un altro step

def rot(grid):
    # la cassetta è tutta marcia se non contiene arance sane su nessuna riga
    return not any( any( x == 1 for x in line ) for line in grid )

def rotting(grid):
    # uno step di simulazione crea una nuova griglia in cui 
    return [ [ 2 if v==1 and 2 in neighbors(grid,x,y)  # tutte le arance sane che hanno un vicino marcio diventano marce 
                 else v                                # altrimenti restano come sono
                 for x,v in enumerate(line) ] for y,line in enumerate(grid) ]

def neighbors(grid, x, y):
    # calcolo quali sono i 4 vicini di ciascuna arancia
    W,H = len(grid[0]), len(grid)                                   # date le dimensioni della cassetta
    coords = [ (x-1, y), (x+1, y), (x, y-1), (x, y+1) ]             # e le possibili posizioni dei vicini
    return [ grid[Y][X] for X,Y in coords if 0<=X<W and 0<=Y<H ]    # torno i valori di quelli interni alla cassetta

# ----------------------------------- EX.3 ----------------------------------- #

def ex3(a, b, k):
    ''' Si implementi una funzione ricorsiva che prende in ingresso una
    coppia di stringhe a e b, e un intero k e ritorna una lista.
    Nella lista sono contenute tutte le possibili stringhe che si possono
    ottenere dalla concatenazione di una sottostringa di lunghezza k della
    prima stringa con una sottostringa di lunghezza k della seconda stringa.
    La lista ritornata è ordinata in ordine rispetto alla posizione della
    sottostringa di a in a e della sottostringa di b in b.

    es: es4('casa', 'riccio', 3) ritorna la lista
     ['casric', 'casicc', 'cascci', 'cascio', 'asaric', 'asaicc', 'asacci', 'asacio']
    '''
    ### INSERIRE QUI IL CODICE ###
    pass
    A = sottostringhe(a,k)                      # genero le sottostringhe di a
    B = sottostringhe(b,k)                      # e quelle di b
    return [ sa+sb for sa in A for sb in B ]    # e le concateno nell'ordine desiderato

def sottostringhe(A,k):                         # risorsivamente genero le sottostringhe lunghe k
    if len(A)<k:                                # se la stringa non ha k lettere
        return []                               # non ha sottostringhe
    else:                                       # altrimenti prendo le prime k lettere
        return [ A[:k] ] + sottostringhe(A[1:],k)   # e continuo con la stringa che inizia un carattere dopo


# ----------------------------------- EX.4 ----------------------------------- #

'''Ex. 2: 9 points

Write a function ex2(folderPath) that, given the path of a folder being the root of
a folder tree containing text files only, creates and returns a dictionary in which:

- there is one pair (key, value) for each text file that was found in the folderPath folder
or, recursively, in any of its subfolders;

- each key is the path of a text file, relative to the folderPath folder;

- the corresponding value is an integer, obtained as the sum of the unicode
equivalent of all the characters in the text file (the newline characters
are NOT included in the sum);

For example, given the following folder tree:

ex2
  |-f1
     |-f1-1

and the following files:

ex2/t1.txt          -   file content: hello world
ex2/f1/f1-1/t2.txt  -   file content: let's count to 3, 1-2-3

ex2("ex2") will return the dictionary {'ex2/t1.txt': 1116, 'ex2/f1/f1-1/t2.txt': 1722}
as the sum of the unicode equivalent of "hello world" is 1116, while the one
of "let's count to 3, 1-2-3" is 1722.
'''
import os
def ex4(folderPath):
    # Enter your code here
    pass
    D = {}                                          # inizializzo il dizionario D vuoto
    for name in os.listdir(folderPath):             # scandiso la directory
        fullname = folderPath + '/' + name          # e costruisco il filename
        if os.path.isfile(fullname):                # se è un file
            text = open(fullname, encoding='utf8').read()   # ne leggo il testo
            # per ogni riga sommo il codice di ciascun carattere e sommo i risultati
            S = sum(sum(map(ord, line)) for line in text.split('\n'))
            D[fullname] = S                         # e metto nel dizionario filename:numero
        else:                                       # se invece è una directory
            D.update(ex4(fullname))                 # aggiorno D con il risultato della sua esplorazione
    return D                                        # infine torno D

# --------------------------------------------------------------------------- #


##########################################################################################
