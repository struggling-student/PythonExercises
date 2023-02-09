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

# %% ----------------------------------- EX.1 ----------------------------------- #
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
def MV(gruppo,K):
    valori = [ sum(ord(c) for c in parola) for parola in gruppo ]
    media  = sum(valori)/K
    varianza = sum( (V-media)**2 for V in valori)/K
    return media, varianza

def ex1(strings, K):
    ## INSERISCI QUI IL TUO CODICE
    pass
    N = len(strings)
    gruppi = [ strings[i:i+K] for i in range(N-K+1) ]
    M,V = max( [ MV(G,K) for G in gruppi ], key=lambda x: x[0] )
    return round(M,3), round(V,3)

# %% ----------------------------------- EX.2 ----------------------------------- #

"""
Es 2: 6+2 punti

Vogliamo disegnare una immagine che contiene ellissi colorate piene su sfondo nero.
Implementate la funzione ex2(lista_ellissi, file_png, larghezza, altezza)
che riceve gli argomenti:
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

La funzione ex2 deve inoltre tornare il numero di pixel che sono stati colorati
da più di una ellisse. (2 punti)

NOTA: Ricordo che i punti dell'immagine che appartengono alla ellisse sono tutti i punti P=x,y tali che
    D > distanza(P,F1) + distanza(P,F2)
    con distanza calcolata con il teorema di Pitagora

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
def ex2(list_ellisses, png_filename, width, height):
    pass
    # inserisci qui il tuo codice
    img = [ [ (0,0,0) ] * width for _ in range(height) ]
    count = [ [0]       * width for _ in range(height) ]
    for el in list_ellisses:
        draw_ellisse(*el, img, count, width, height)
    images.save(img, png_filename)
    N = 0
    for riga in count:
        for n in riga:
            if n>1: N += 1
    return N

def draw_ellisse(x1,y1, x2,y2, D, R,G,B, img, count, W, H):
    # per ogni x nell'intervallo orizzontale
    for x in range(W):
        # per ogni y nell'intervallo verticale
        for y in range(H):
            # se va dipinto
            if D > sqrt((x-x1)**2+(y-y1)**2)+sqrt((x-x2)**2+(y-y2)**2):
                img[y][x]    = R,G,B                    # coloro il pixel
                count[y][x] += 1                        # e conto quante volte lo faccio

# %% ----------------------------------- EX.3 ----------------------------------- #

"""
Es 3: 6+3 punti

Si progetti la funzione ex3, ricorsiva o che fa uso di funzioni o metodi ricorsivi,
che riceve come argomenti:
    - file_txt: un file di testo che descrive un albero binario in formato pre-ordine (vedi dopo)
e ritorna un albero binario.

La funzione deve leggere il file file_txt che contiene su ciascuna riga 3 valori interi separati da spazi
    - valore: il valore di un nodo dell'albero, da realizzare con la classe tree.BinaryTree
    - sx: 1 se il nodo ha un sottoalbero sinistro, 0 se non lo ha
    - dx: 1 se il nodo ha un sottoalbero destro,   0 se non lo ha

L'ordine delle righe corrisponde all'ordine di visita dei nodi dell'albero se stampato
ricorsivamente in pre-ordine, ovvero:
    - radice
    - sottoalbero sinistro se presente
    - sottoalbero destro   se presente

La funzione ritorna la radice dell' albero costruito.

SUGGERIMENTO: leggendo ciascuna riga potete sapere:
 - quale nodo creare
 - se possiede i sottoalberi sinistro e/o destro 
 e quindi potete guidare le chiamate ricorsive necessarie a leggere le righe immediatamente seguenti.

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
che va realizzato con istanze di BinaryNode

"""

import tree
def ex3(file_txt):
    # inserisci qui il tuo codice
    pass
    with open(file_txt, encoding='utf-8') as F:
        A = leggi_albero(F)
        print(A)
        return A

def leggi_albero(F):
    line = F.readline().strip()
    if line:
        V,l,r = list(map(int,line.split()))
        sx = leggi_albero(F) if l else None
        dx = leggi_albero(F) if r else None
        return tree.BinaryTree(V,sx,dx)
    else:
        return None


"""
Ex 4: parte 2) (3 punti)

Definite la funzione ex4(node, k) che, facendo uso della precedente ex4p1,
una volta ricostruito l'albero, trova il nodo divisibile per k che si trova
a profondità massima (partendo da radice=0).
Se nessun nodo è divisibile per k la profondità da ritornare è -1 .
La funzione torna la profondità trovata.

Esempio: se K=5 a l'albero è il seguente
                    1                           # profondità 0
                /       \                       #
            25           7                      # 1
        /      \                                #
       3        65                              # 2
     /   \                                      #
    4     55                                    # 3

la funzione ex4p2 deve tornare 3, perchè 55 è il più profondo multiplo di 5
e si trova a profondità 3

"""
def ex4(A, k):
    pass
    # inserisci qui il tuo codice
    return profondità_massima(A,k)

def profondità_massima(radice,k,depth=0):
    if not radice:
        return -1
    if radice.value % k == 0:
        return max(depth, profondità_massima(radice.left, k, depth+1), profondità_massima(radice.right,k,depth+1))
    else:
        return max(       profondità_massima(radice.left, k, depth+1), profondità_massima(radice.right,k,depth+1))

###################################################################################

if  __name__ == '__main__':
    pass
    # inserisci qui i tuoi test
