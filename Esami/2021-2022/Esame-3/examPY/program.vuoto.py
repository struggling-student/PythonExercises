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
Es 1: 6 punti
Scrivere una funzione che prende una lista "points" di coordinate x,y
di N punti nel piano cartesiano, ed un intero K e ritorna una tupla di
due elementi. Ciascun punto è una coppia di interi. Per ogni gruppo di
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
la tupla con le coordinate X,Y del baricentro e il secondo è il raggio
individuato. Tutti i valori vanno riportati con una precisione di 3
cifre decimali.

  - NOTA: si può assumere che per ogni test esista un gruppo unico di
    K punti che soddisfa la richiesta
  - NOTA: La distanza fra 2 punti (x1, y1) e (x2, y2)
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


def ex1(points, K):
    # INSERISCI QUI IL TUO CODICE
    pass

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
    la distanza fra 2 punti (x1, y1) e (x2, y2)
    è Euclidea: sqrt[(x1-x2)² + (y1-y2)²].

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
    # INSERISCI QUI IL TUO CODICE
    pass


# %% ----------------------------------- EX.3 ----------------------------------- #

"""
Es 3: 8 punti
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


def ex3(file_txt):
    # INSERISCI QUI IL TUO CODICE
    pass


"""
Es 4: 6+3 punti
    Sono dati il path di una directory e una lista di parole da cercare.
    Vogliamo trovare il file di testo (.txt) che contiene le parole della
    lista in ingresso con varianza massima, ovvero con la maggiore
    variabilità della distribuzione delle occorrenze fra le parole.

    Per avere la varianza di un vettore si calcola la media dei quadrati
    delle differenze dei singoli valori rispetto alla media del vettore.
    Quindi, in questo caso, per ogni file si calcola il vettore delle
    occorrenze delle parole della lista, si calcola la media M e poi la
    varianza, con la seguente formula:

        varianza(vettore) = somma(  (v-M)^2 )/lunghezza(vettore)
                   per tutti i valori v del vettore

    Si definisca la funzione ex4(dirpath, parole) che cerca ricorsivamente,
    o usando funzioni ricorsive, il file in cui la frequenza delle occorrenze
    delle parole cercate ha varianza massima. Per la ricerca NON si fa
    distinzione fra maiuscole e minuscole. Inoltre, si devono considerare
    come separatori delle parole TUTTI i caratteri NON alfabetici.

    La funzione deve tornare una coppia contenente:
    - come primo elemento un dizionario che ha come chiavi le parole cercate
      e come valori il numero di occorrenze di ciascuna parola nel file
      trovato (6 punti)
    - come secondo elemento la varianza calcolata, arrotondata alla terza
      cifra decimale (3 punti)

Esempio:
    se dirpath = 'A' e parole = ['commodo', 'nisl', 'libero', 'in', 'gravida', 'lacus']
La funzione deve tornare il dizionario
    {'commodo': 13, 'nisl': 10, 'libero': 5, 'in': 37, 'gravida': 6, 'lacus': 14}
    che corrisponde al file 'A/C/Q/Z/Lorem.txt'
    e che ha la massima varianza (115.139) rispetto agli altri file '.txt'

    Si ricorda che è possibile utilizzare le funzioni del package os, in
    particolare os.listdir, os.path.isdir, os.path.isfile.
    È, invece, proibito utilizzare la funzione os.walkdir.
"""

import os

def ex4(dirpath, parole):
    pass
    # inserisci qui il tuo codice



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
