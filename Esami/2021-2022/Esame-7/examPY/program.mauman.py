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
''' Ex 1: 6 punti
    Si implementi una funzione che prende in ingresso tre nomi di file
    e restituisce una coppia di numeri interi.
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
    scritte in file3. 
'''
def ex1(file1, file2, file3):
    f1 = open(file1, "r", encoding="utf8")
    f2 = open(file2, "r", encoding="utf8")
    f3 = open(file3, "w", encoding="utf8")
    l1 = f1.readlines()
    l2 = f2.readlines()
    f1.close()
    f2.close()
    stringcount = 0
    rowcount = 0
    for i in range(len(l1)):
        L1 = l1[i]
        L2 = l2[i]
        L1 = L1.replace("\n", "")
        L1 = L1.replace("\t", " ")
        L1 = L1.replace(",", " ")
        L1 = L1.replace(";", " ")
        L2 = L2.replace("\n", "")
        L2 = L2.replace("\t", " ")
        L2 = L2.replace(",", " ")
        L2 = L2.replace(";", " ")
        ws1 = L1.split(" ")
        ws1 = [x for x in ws1 if x != ""]
        ws2 = L2.split(" ")
        ws2 = [x for x in ws2 if x != ""]
        ws3 = []
        for w1 in ws1:
            if w1 in ws2:
                ws3.append(w1)
        if ws3 != []:
            ws3.sort(key=lambda x: (len(x), x))
            f3.write(" ".join(ws3) + "\n")
            stringcount += len(ws3)
            rowcount += 1
    f3.close()
    return (stringcount, rowcount)

# ----------------------------------- EX.2 ----------------------------------- #

''' Ex. 2: 6 points
    Write a function ex2(gridFilePath) that, given a NxN grid stored in a json file as
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

def oneMinute(grid):
    gridCopy = [x.copy() for x in grid]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 2:
                if gridCopy[max(i-1, 0)][j] == 1:
                    gridCopy[max(i-1, 0)][j] = 2
                if gridCopy[i][max(j-1, 0)] == 1:
                    gridCopy[i][max(j-1, 0)] = 2
                if gridCopy[min(i+1, len(gridCopy) - 1)][j] == 1:
                    gridCopy[min(i+1, len(gridCopy) - 1)][j] = 2
                if gridCopy[i][min(j+1, len(gridCopy[i]) - 1)] == 1:
                    gridCopy[i][min(j+1, len(gridCopy[i]) - 1)] = 2
    return gridCopy

def noFresh(grid):
    for row in grid:
        for cell in row:
            if cell == 1:
                return False
    return True

def ex2(gridFilePath):
    with open(gridFilePath, "r", encoding="utf8") as file:
        grid = json.load(file)
    gridCopy = None
    counter = 0
    while gridCopy != grid:
        if noFresh(grid):
            return counter
        gridCopy = [x.copy() for x in grid]
        grid = oneMinute(grid)
        counter += 1
    return -1
# ----------------------------------- EX.3 ----------------------------------- #

''' Ex 3: 9 punti
    Si implementi una funzione ricorsiva che prende in ingresso una
    coppia di stringhe a e b, e un intero k e ritorna una lista.
    Nella lista sono contenute tutte le possibili stringhe che si possono
    ottenere dalla concatenazione di una sottostringa di lunghezza k della
    prima stringa con una sottostringa di lunghezza k della seconda stringa.
    La lista ritornata è ordinata in ordine rispetto alla posizione della
    sottostringa di a in a e, a parimerito, in ordine della sottostringa di b in b.

    es: ex3('casa', 'riccio', 3) ritorna la lista
     ['casric', 'casicc', 'cascci', 'cascio', 'asaric', 'asaicc', 'asacci', 'asacio']
'''

def recurCombine(a, b, k, res):
    if len(a) < k:
        return res
    for s in range(0, len(b) - (k - 1)):
        res.append(a[0:k] + b[s:s + k])
    recurCombine(a[1:], b, k, res)


def ex3(a, b, k):
    res = []
    recurCombine(a, b, k, res)
    return res

# ----------------------------------- EX.4 ----------------------------------- #

'''Ex. 4: 9 points

Write a function ex4(folderPath), recursive or using recursive function/methods,
that, given the path of a folder being the root of a folder tree containing 
text files only, creates and returns a dictionary in which:

- there is one pair (key, value) for each text file that was found in the folderPath folder
or, recursively, in any of its subfolders;

- each key is the path of a text file, relative to the folderPath folder;

- the corresponding value is an integer, obtained as the sum of the unicode
equivalent of all the characters in the text file (the newline characters
are NOT included in the sum);

For example, given the following folder tree:

ex4
  |-f1
     |-f1-1

and the following files:

ex4/t1.txt          -   file content: hello world
ex4/f1/f1-1/t2.txt  -   file content: let's count to 3, 1-2-3

ex4("ex4") will return the dictionary {'ex4/t1.txt': 1116, 'ex4/f1/f1-1/t2.txt': 1722}
as the sum of the unicode equivalent of "hello world" is 1116, while the one
of "let's count to 3, 1-2-3" is 1722.

NOTICE: it's forbidden to use the os.walk function.
NOTICE: please do not place your recursive function inside another function, 
else the test system will not detect it and all test will fail.

'''


import os

def sumChars(filePath):
    result = 0
    with open(filePath, "r", encoding="utf8") as file:
        for line in file:
            for character in line:
                if character != "\n":
                    result += ord(character)
    return result

def createDict(folderPath):
    result = {}
    dir_list = os.listdir(folderPath)
    for item in dir_list:
        if os.path.isdir(folderPath + "/" + item):
            result.update(createDict(folderPath + "/" + item))
        else:
            result[folderPath + "/" + item] = sumChars(folderPath + "/" + item)
    return result

def ex4(folderPath):
    return createDict(folderPath)

# ----------------------------------- END ----------------------------------- #

if __name__ == '__main__':
    # print(ex1("ex1/f1.txt", "ex1/f2.txt", "ex1/f1f2.txt"))
    print(ex3('casa', 'riccio', 3))