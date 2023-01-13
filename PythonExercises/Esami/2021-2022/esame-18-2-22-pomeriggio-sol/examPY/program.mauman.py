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
# Per debuggare le funzioni ricorsive potete disattivare il test di ricorsione
# settando DEBUG=True nel file grade.py
#
# Per controllare lo stack trace degli errori, si può decommentare la linea
# dedicata in testlib.py (vedere il commento nel corpo della funzione runOne)
################################################################################

# %% ----------------------------------- EX.1 ----------------------------------- #

"""
Es 1: 7 punti
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

def barycenter(points):
    return round(sum([p[0] for p in points])/len(points), 3), round(sum([p[1] for p in points])/len(points), 3)

def dist(p1, p2):
    return round(sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2), 3)

def ray(points):
    b = [barycenter(points)] * len(points)
    return max(map(dist, b, points))

def ex1(points, K):
    barmin = -1
    raymin = -1
    for i in range(0, len(points) - K + 1):
        sub = points[i:i + K]
        if barmin == -1 or ray(sub) < raymin:
            barmin = barycenter(sub)
            raymin = ray(sub)
    return barmin, raymin



# %%----------------------------------- EX.2 ----------------------------------- #

"""
Es 2: 7 punti
Viene fornita un'immagine con sfondo nero al cui interno sono presenti
un numero variabile di croci, che possono avere colori sia diversi
sia uguali fra loro.  Ciascuna croce è composta da due linee, una
orizzontale e una verticale che si incontrano. Le linee hanno
spessore di 1 pixel e possono essere di lunghezza diversa.  Due croci
arbitrarie non possono sovrapporsi e c'è sempre almeno un pixel di sfondo
fra le due. Ciascun lato/braccio della croce è lungo almeno un pixel.

Consiglio: prima di iniziare vedere le immagini nella dir 'crosses/'

Si progetti e implementi la funzione ex2 che prende in ingresso
l'immagine suddetta e individua tutte le croci. Ogni croce deve essere
descritta come una tupla di 4 punti più la tupla del colore.
I 4 punti sono nell'ordine "alto", "basso", "sinistra", "destra", dove:
    - "alto" è il punto più in alto,
    - "basso" è il punto più in basso,
    - "sinistra" è il punto più a sinistra,
    - "destra" è il punto più a destra.
Ogni punto è una tupla di coordinate y, x, dove y è la riga e x la colonna.

Ad esempio, la croce seguente:

     0 1 2 3 4
   0 . . . . .
   1 . . x . .
   2 . x x x x
   3 . . x . .
   4 . . x . .
   5 . . . . .

                    alto   basso   sx     dx       colore
è descritta da:  ((1, 2), (4,2), (2,1), (2, 4), (r, g, b))

La funzione deve ritornare tutte le croci individuate come un dizionario
che ha:
- come chiavi i colori delle croci
- come valore un insieme con tutte le croci del colore indicato
  dalla chiave.
"""

import images

def ex2(path_to_im):
    black = (0, 0, 0)
    img = images.load(path_to_im)
    result = {}
    for y in range(1, len(img) - 1):
        for x in range(1, len(img[y]) - 1):
            col = img[y][x]
            coltop = img[y - 1][x]
            colleft = img[y][x - 1]
            colright = img[y][x + 1]
            if col != black and coltop == black and colleft == black and colright == black:
                tx = x
                ty = y
                top = (ty, tx)
                intersection = (-1, -1)
                while col != black and ty < len(img):
                    ty = ty + 1
                    col = img[ty][tx]
                    if img[ty][tx - 1] != black:
                        intersection = tx, ty
                bottom = (ty - 1, tx)
                tx, ty = intersection
                col = img[ty][tx]
                while col != black and tx < len(img[y]):
                    tx = tx + 1
                    col = img[ty][tx]
                right = (ty, tx - 1)
                tx, ty = intersection
                col = img[ty][tx]
                while col != black and tx > 0:
                    tx = tx - 1
                    col = img[ty][tx]
                left = (ty, tx + 1)
                tx, ty = intersection
                col = img[ty][tx]
                if col not in result:
                    result[col] = set()
                    result[col].add((top, bottom, left, right))
                else:
                    result[col].add((top, bottom, left, right))
    return result


# ----------------------------------- EX.3 ----------------------------------- #

"""
Es 3: 9 punti (6+3)
Si progetti e implementi la funzione ricorsiva ex3(S), o che faccia
uso di funzioni ricorsive, che prende in ingresso una sequenza di
numeri sotto forma di stringa S e restituisca le foglie dell'albero di
gioco applicando la seguente mossa:

   - si sostituisca una tripla di cifre consecutive dalla stringa solo se
  la tripla contiene elementi binari, ossia solo zeri e uno.  Ad
  esempio, data tripla "501" non è' possible applicare nessuna mossa
  perché il 5 invalida il fatto che tutte le cifre devono essere
  binarie.  Al contrario si può applicare la mossa a "101".
   - In caso di mossa applicata, la mossa sostituisce alla tripla, il
  singolo carattere che deriva dalla conversione della tripla binaria
  in numero decimale, ossia "101" --> "5" = 2**2 + 2**0 = 4 + 1
   - NOTA: per convertire guardare help(int)

Le foglie sono le stringhe alle quali non è più possibile applicare la mossa.
La stringa nella foglia deve essere convertita in intero.

Esempio: se la stringa è '5111001', l'albero di gioco (indentato) sarà
il seguente.  Nota: le parentesi indicano la trasformazione della mossa.
5111001     # inizio - 5111001
-57001      #   5(111)001   diventa 5(7)001
--571*      #       57(001) diventa 571,   *foglia, nessuna mossa applicabile
-51601*     #   51(110)01   diventa 51601, *foglia, nessuna mossa applicabile
-51141*     #   511(100)1   diventa 51141, *foglia, nessuna mossa applicabile
-51111      #   5111(001)   diventa 51111
--571*      #       5(111)1 diventa 571,   *foglia, nessuna mossa applicabile
--517*      #       51(111) diventa 517,   *foglia, nessuna mossa applicabile

6 punti:
La funzione deve tornare la lista di foglie, senza ripetizioni.
Altri 3 punti:
La lista deve essere ordinata in modo che prima appaiano gli interi
con meno cifre e poi dopo quelli con piu cifre; a parità di cifre,
gli interi sono ordinati in modo decrescente rispetto al valore numerico.
L'esempio sopra rende [571, 517, 51601, 51141], se ordinato.
"""
def ex3(S):
    pass
    # inserisci qui il tuo codice

# ----------------------------------- EX.4 ----------------------------------- #


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

if  __name__ == '__main__':
    print(ex2("crosses/cross_01.png"))