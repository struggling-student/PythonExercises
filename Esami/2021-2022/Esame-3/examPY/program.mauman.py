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
Ex 1: 6 points
Scrivere una funzione che prende in ingresso una lista di stringhe ed
un intero K e restituisce una coppia di float calcolata come segue.

Chiamiamo media di una sequenza di K stringhe la media delle somme dei
valori unicode delle stringhe che la compongono.  Ad esempio: le
stringhe 'casa', 'coso', 'cosa', 'chiuso' hanno le somme dei valori
unicode 408, 436, 422, 651, rispettivamente. Se K=2, le medie delle
stringhe consecutive saranno 422.0, 429.0 e 536.5.

La varianza, invece, è la calcolata come la media del quadrato della
distanza di ogni stringa dalla media, ovvero:
- data la sequenza S lunga K, se m è la sua media, la sua varianza v è
calcolata come
   v = sum(( m - s)**2)/K
dove la somma è per ogni stringa s in S.

I due float da ritornare sono media e varianza del gruppo di K stringhe
consecutive della lista in ingresso che hanno media massima e vanno
arrotondati alla terza cifra decimale.

Esempio:
 ex1(['casa', 'coso', 'cosa', 'chiuso'], 2) ritornerà (536.5, 13110.25)
poiché le somme dei valori unicode sono
[408, 436, 422, 651] e le coppie media, varianza per K=2 sono,
 rispettivamente
422.0 196.0
429.0 49.0
536.5 13110.25.

"""
def ex1(strings, K):
    unicodes = []
    for s in strings:
        unicodes.append(sum(map(ord,list(s))))
    results = []
    for i in range(0, len(unicodes) - K + 1):
        seq = unicodes[i:i + K]
        mean = round(sum(seq) / K, 3)
        var = 0
        for v in seq:
            var = var + (mean - v) ** 2
        var = round(var / K, 3)
        results.append((mean, var))
    results.sort(key=lambda x : x[0], reverse=True)
    return results[0]

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
    con distanza = distanza euclidea, calcolata col teorema di Pitagora

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

def dist(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def ex2(list_ellisses, png_filename, width, height):
    img = [[(0, 0, 0) for i in range(width)] for j in range(height)]
    flags = [[False for i in range(width)] for j in range(height)]
    for ell in list_ellisses:
        f1x = ell[0]
        f1y = ell[1]
        f2x = ell[2]
        f2y = ell[3]
        D = ell[4]
        col = (ell[5], ell[6], ell[7])
        for y in range(height):
            for x in range(width):
                if dist(x, y, f1x, f1y) + dist(x, y, f2x, f2y) < D:
                    if img[y][x] != (0, 0, 0):
                        flags[y][x] = True
                    img[y][x] = col

    count = 0
    for row in flags:
        for cell in row:
            if cell:
                count += 1
    images.save(img, png_filename)
    return count


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

def buildTree(nodes):
    node = nodes.pop(0)
    root = tree.BinaryTree(node[0])
    if node[1] == 1:
        root.left = buildTree(nodes)
    if node[2] == 1:
        root.right = buildTree(nodes)
    return root

def ex3(file_txt):
    file = open(file_txt, encoding="utf-8")
    nodes = []
    for line in file:
        line = line.strip()
        nodes.append(list(map(int, line.split(" "))))
    file.close()
    return buildTree(nodes)


"""
Es 4: 8 punti

Si progetti la funzione ex4(node, k), ricorsiva o che fa uso di
funzioni o metodi ricorsivi, che riceve come argomenti un albero
binario e trova il nodo divisibile per k che si trova a profondità
massima (partendo da radice=0). La funzione restituisce la profondità
del nodo individuato. Se nessun nodo è divisibile per k la funzione
ritorna il valore -1.

Ciascun nodo è un oggetto della classe tree.BinaryTree

Esempio: se K=5 e l'albero è il seguente
                    1                           # profondità 0
                /       \                       #
            25           7  ------------------- # 1
        /      \                                #
       3        65 ---------------------------- # 2
     /   \                                      #
    4     55  --------------------------------- # 3

la funzione ex4 deve ritornare 3, perchè 55 è il nodo con valore
multiplo di 5 che si trova a profondità massima, ovvero 3. Gli
altri nodi potenziali sono 25 e 65, ma sono a una profondità
inferiore (rispettivamente 1 e 2).
"""

def FindRecurse(node, k, depth):
    l = -1
    r = -1
    if node.left is not None:
        l = FindRecurse(node.left, k, depth + 1)
    if node.right is not None:
        r = FindRecurse(node.right, k, depth + 1)
    if node.value % k == 0:
        return max(depth, l, r)
    return max(l, r)

def ex4(node, k):
    return FindRecurse(node, k, 0)




###################################################################################
if __name__ == '__main__':

    itree = tree.BinaryTree.fromList([269282, None, [-693856, None, [709402, [348847, [111989, None, [-502123, [-773768, None, [884775, None, None]], None]], [-19008, None, [310678, None, [-650898, [-68752, [981492, None, [944443, None, None]], [498992, [-290104, None, None], [443285, None, None]]], None]]]], None]]])

    print(ex4(itree, 7))
