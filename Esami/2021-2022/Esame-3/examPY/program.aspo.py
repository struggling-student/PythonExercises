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
# lista 'test' è assegnata alla fine di grade.py
#
# Per debuggare facilmente le funzioni ricorsive potete disattivare il controllo
# di ricorsione settando DEBUG=True nel file grade.py
#
# Per controllare lo stack trace degli errori, si può decommentare la linea
# dedicata in testlib.py (vedere il commento nel corpo della funzione runOne)
################################################################################

# ----------------------------------- EX.1 ----------------------------------- #

"""
Es 1: 7 punti
Scrivere una funzione che prende una lista "points" di coordinate x,y
di N punti nel piano cartesiano, ed un intero K e ritorna una tupla di
due elementi. Ciascun punto è una tupla di interi. Per ogni gruppo di
K punti consecutivi si deve calcolare il suo baricentro e il raggio al
fine di individuare il gruppo con raggio minimo.
Definiamo:
- "baricentro" di un gruppo di punti, il punto X,Y ottenuto calcolando
  la media X delle loro coordinate x, e la media Y delle loro
  coordinate y;
- "raggio" di un gruppo di punti è dato dalla distanza del punto più
  lontano dal baricentro.

La funzione deve tornare il baricentro ed il raggio del gruppo di
punti con raggio minore, ovvero una tupla in cui il primo elemento è
sono le coordinate X,Y del baricentro e il secondo è il raggio
individuato. Tutti i valori vanno riportati con una precisione di 3
cifre decimali.

  - NOTA: potete assumere che per ogni test esista un gruppo unico di
    K punti che soddisfa la richiesta
  - NOTA: La distanza fra 2 punti dist((x1, y1), (x2, y2))
    è Euclidea: sqrt[(x1-x2)² + (y1-y2)²]

Esempio:
se i punti sono:
[(-1, 3), (1, 3), (3, 11), (5, 27), (7, 51), (9, 83), (11, 123), (13, 171), (15, 227), (17, 291), (19, 363)]
La sequenza di K=4 punti che è contenuta nel cerchio più piccolo è:
[(-1, 3), (1, 3), (3, 11), (5, 27)]
che ha baricentro in X=(-1+1+3+5)/4 = 8/4 = 2.0 Y=(3+3+11+27)/4 = 44/4 = 11.0
ed ha raggio 16.279 (distanza dal baricentro 2,11 al punto più lontano 5,27).
Quindi ex1 torna la coppia ((2.0, 11.0), 16.279)
"""

from math import sqrt

def baricentro(l):
    return round(sum(map(lambda x:x[0],l))/len(l),3), round(sum(map(lambda x:x[1],l))/len(l),3)

def dist(p1, p2):
    return sqrt(sum([(p1[i]-p2[i])**2 for i in (0,1)]))

def ex1(points, K):
    gruppi = {}

    for i in range(len(points)-K+1):
        g = points[i:i+K]
        gruppi[baricentro(g)] =[dist(baricentro(g),x) for x in g]
    gruppo = min(gruppi, key=lambda x: max(gruppi[x]))
    return gruppo, round(max(gruppi[gruppo]), 3)
        # insert here your code

# %% ----------------------------------- EX.2 ----------------------------------- #
"""
Es 2: 6+3 punti

Vogliamo disegnare una immagine che contiene ellissi colorate piene su
sfondo nero.  Implementate la funzione ex2(lista_ellissi, file_png,
larghezza, altezza) che riceve gli argomenti:
    lista_ellissi: una lista di 8-tuple contenenti ciascuna:
        x1, y1: le coordinate del primo   fuoco F1 della ellisse
        x2, y2: le coordinate del secondo fuoco F2 della ellisse
        D:      parametro della ellisse (vedi sotto)
        R,G,B:  il colore da usare per disegnare l'ellisse
    file_png:   il nome del file png in cui salvare l'immagine che avete creato
    larghezza:  larghezza della immagine
    altezza:    altezza della immagine

e disegna sulla immagine, nello stesso ordine della lista, le ellissi,
e quindi la salva nel file indicato da file_png. (6 punti)

La funzione ex2 deve inoltre tornare il numero di pixel che sono stati
colorati da più di una ellisse. (2 punti)

NOTA: Ricordo che i punti dell'immagine che appartengono alla ellisse
    sono tutti i punti P=x,y tali che:
    D > distanza(P,F1) + distanza(P,F2)
    con distanza calcolata come specificato in ex1.

Esempio: se W=279 e H=233  e lista_ellissi è

       x1  y1     x2   y2    D     R    G    B
  [  (160, 185,  182, 199,   28,  110, 146, 109),
     (233, 187,  161, 173,   83,  148, 175, 239),
     (133, 152,  253, 176,  125,  220, 161, 227)]

l'immagine da produrre è come ex2/3.png
ed il valore da tornare è 1077
"""

import images
from math import sqrt

def distanza(x1, y1, x2, y2):
    return sqrt((x1-x2)**2 + (y1- y2)**2)


def disegna(e, im, colora):
    x1, y1, x2, y2, D, R, G, B = e

    for row in range(len(im)):
        for col in range(len(im[0])):
            if distanza(col, row, x1, y1) + distanza(col, row, x2, y2) < D:
                if colora[row][col] == 0:
                    colora[row][col] = 1
                else:
                    colora[row][col] = 2
                im[row][col] = (R,G,B)


def ex2(list_ellisses, png_filename, width, height):
    im = [[(0,)*3 for _ in range(width)] for x in range(height)]
    colora = [[0 for _ in range(width)] for x in range(height)]
    for e in list_ellisses:
        disegna(e, im, colora)
    images.save(im, png_filename)

    # inserisci qui il tuo codice
    return sum([len(list(filter(lambda x: x==2, y))) for y in colora])
    pass


# %% ----------------------------------- EX.3 ----------------------------------- #

"""
Es 3: 9 punti
Si progetti la funzione ex3, ricorsiva o che fa uso di funzioni o
metodi ricorsivi, che riceve come argomenti:
    - file_txt: un file di testo che descrive un albero binario in
      formato pre-ordine (vedi dopo) e ritorna l'abero binario letto.

La funzione deve leggere il file file_txt che contiene su ciascuna
riga 3 valori interi separati da spazi:
    - valore: il valore di un nodo dell'albero, da realizzare con la
      classe tree.BinaryTree
    - sx: 1 se il nodo ha un sottoalbero sinistro, 0 se non lo ha
    - dx: 1 se il nodo ha un sottoalbero destro,   0 se non lo ha

L'ordine delle righe corrisponde all'ordine di visita dei nodi
dell'albero se stampato ricorsivamente in pre-ordine, ovvero:
    - radice
    - sottoalbero sinistro se presente
    - sottoalbero destro   se presente

La funzione ritorna la radice dell' albero costruito.

SUGGERIMENTO: leggendo ciascuna riga potete sapere:
 - quale nodo creare
 - se possiede i sottoalberi sinistro e/o destro
 e quindi potete guidare le chiamate ricorsive necessarie a leggere le
 righe immediatamente seguenti.

Esempio: se il file contiene le linee (che ho commentato):
    1  1 1     # la radice contiene il valore 1 ed ha sia il sottoalbero SX che il DX
    25 1 1     # qui inizia il sottoalbero SX, che contiene 25 ed ha entrambi i figli
    3  1 1     # qui inizia il figlio SX di 25, che ha entrambi i figli
    4  0 0     # questa è una foglia, figlio SX di 3
    55 0 0     # questa è una foglia, figlio DX di 3
    65 0 0     # qui inizia il figlio DX di 25, che è una foglia
    7  0 0     # e questo è il figlio DX di 1, ed è una foglia

si ottiene l'albero seguente
                    1             #
                /       \         #
            25           7        #
        /      \                  #
       3        65                #
     /   \                        #
    4     55                      #
che va realizzato con istanze di tree.BinaryTree
"""

import tree
def build_tree(lines):
    node = next(lines)
    v, l, r = node.split()
    root = tree.BinaryTree(int(v))
    if l!='0':
        root.left = build_tree(lines)
    if r!='0':
        root.right = build_tree(lines)
    return root


def ex3(file_txt):
    with open(file_txt) as f:
        lines = map(str.strip, f.readlines())
    root = build_tree(lines)
    return  root

# ----------------------------------- EX.4 ----------------------------------- #

"""
Es 4: 6+3 punti
    Sia data una lista di parole da cercare ed il path di una directory in cui cercare.
    Vogliamo trovare il file di testo (.txt) che contiene le parole indicate con
    una distribuzione delle frequenze "più variabile" (ovvero con varianza massima).

    Associamo ad un vettore di interi (in questo caso le frequenze delle parole nel file)
    la sua "varianza" ovvero la somma dei quadrati delle differenze dalla media.
        varianza(vettore) = somma(  (f-f_medio)^2 ) per tutti gli f del vettore

    Definite la funzione exB(dirpath, parole) che cerca ricorsivamente,
    o usando funzioni ricorsive, il file in cui la frequenza delle occorrenze
    delle parole cercate (ignorando la differenza tra maiuscole e minuscole)
    ha varianza massima.
    NOTA: nell'analizzare un file di testo considerate come separatori tutti i caratteri non
    alfabetici.

    La funzione deve tornare una coppia contenente:
    - come primo elemento un dizionario che ha come chiavi le parole cercate e come
      valori il numero di occorrenze di ciascuna parola nel file trovato (6 punti)
    - come secondo elemento la varianza calcolata, arrotondata alla 3° cifra decimale (3 punti)

Esempio:
    se dirpath = 'A' e parole = ['commodo', 'nisl', 'libero', 'in', 'gravida', 'lacus']
La funzione deve tornare il dizionario
    {'commodo': 13, 'nisl': 10, 'libero': 5, 'in': 37, 'gravida': 6, 'lacus': 14}
    che corrisponde al file 'A/C/Q/Z/Lorem.txt'
    e che ha la massima varianza (690.833) rispetto agli altri file '.txt'

    Si ricorda che è possibile utilizzare le funzioni del package os, in
    particolare os.listdir, os.path.isdir, os.path.isfile.
    È, invece, proibito utilizzare la funzione os.walkdir.
"""
import os

def process(file, parole):
    alfabeto = set(range(ord('a'),ord('z')+1))
    nonalfa = set(range(0, 255))-alfabeto
    table = {c:ord(' ') for c in nonalfa}
    with open(file) as f:
        text = f.read()
        text = text.lower().translate(table)
    words = text.split()
    d = {parola:words.count(parola) for parola in parole}
    return d, var(d)


def var(d):
    if not d:
        return 0
    m = sum(d.values())/len(d)
    return round(sum([(m-v)**2 for v in d.values()])/len(d),3)

def ex4(dirpath, parole):
    massimo = {}, 0
    for file in os.listdir(dirpath):
        fullname = dirpath+'/'+file
        res = 0
        if os.path.isfile(fullname) and fullname.endswith('.txt'):
            res = process(fullname, parole)
        elif os.path.isdir(fullname):
            res = ex4(fullname, parole)
        if res and res[1] > massimo[1]:
            massimo = res
    return massimo




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


