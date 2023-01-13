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
# Per debuggare le funzioni ricorsive potete disattivare il test di ricorsione
# settando DEBUG=True nel file grade.py
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
def ex1(strings, K):
    values = []
    for i, s in enumerate(strings[:-K+1]):
        l = [sum(map(ord, s)) for s in strings[i:i+K]]
        ave = sum(l)/K
        var = sum([(ave-c)**2 for c in l])/K
        values.append((round(ave,3),round(var,3)))
    return max(values)


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


def follow_cross_hor(im, i, col):
    color = im[i][col+1]
    j = col-1
    while j>=0 and im[i][j] == color:
        im[i][j] = (0,0,0)
        j-=1
    col1 = j+1
    j = col+1
    while j<len(im[0]) and im[i][j] == color:
        im[i][j] = (0,0,0)
        j+=1
    return col1, j-1

def follow_cross_vert(im, row1, col):
    color = im[row1][col]
    i = row1
    horizontal_row = 0
    while i<len(im) and im[i][col] == color:
        im[i][col] = (0,0,0)
        if im[i][col+1] == color:
            horizontal_row = i
        i+=1
    col1, col2 = follow_cross_hor(im, horizontal_row, col)
    return (row1, col), (i-1,col), (horizontal_row, col1), (horizontal_row, col2), color



def ex2(path_to_im):
    im = images.load(path_to_im)
    res = {}
    for row in range(len(im)):
        for col in range(len(im[0])):
            if im[row][col] != (0,0,0):
                cross = follow_cross_vert(im, row, col)
                res[cross[-1]] = res.get(cross[-1], set()).union({cross[:-1]})
    return res

# ----------------------------------- EX.3 ----------------------------------- #

"""
Es 3: 9 punti (6+3)
Si progetti e implementi la funzione ricorsiva ex3(S) che prende in
ingresso una sequenza di numeri sotto forma di stringa S e
restituisca tutte le foglie dell'albero di gioco che si ottengono
applicando la seguente mossa:
- si sostituisca una tripla di cifre consecutive dalla stringa solo se
  la tripla contiene elementi binari, ossia solo zeri e uno.  Ad
  esempio, data tripla "501" non è' possible applicare nessuna mossa
  perché il 5 invalida il fatto che tutte le cifre devono essere
  binarie.  Al contrario si può applicare la mossa a "101".
- In caso di mossa applicata, la mossa sostituisce alla tripla, il
  singolo carattere che deriva dalla conversione della tripla binaria
  in numero decimale, ossia "101" --> "5" = 2**2 + 2**0 = 4 + 1
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

def reduce(S):
    ret = set()
    for i in range(len(S)-2):
        try:
            x = str(int(S[i:i+3], 2))
            ret.add(S[:i]+x+S[i+3:])
        except ValueError:
            continue
    return ret

def ex3(S):
    return list(map(int,ex3_aux(S)))

def ex3_aux(S):
    ret = reduce(S)
    if len(ret) == 0:
        return {S}
    more = set()
    for s in ret:
        more.update(ex3_aux(s))
    return sorted(list(more), key = lambda x: (-len(x), x), reverse=True)

# ----------------------------------- EX.4 ----------------------------------- #

"""
Ex 4: 8 punti

Si progetti la funzione ex4(node, k), ricorsiva o che fa uso di
funzioni o metodi ricorsivi, che riceve come argomenti un albero
binario e trova il nodo divisibile per k che si trova a profondità
massima (partendo da radice=0). Se nessun nodo è divisibile per k la
profondità da ritornare è -1.  La funzione restituisce la profondità
del nodo individuato.

Ciascun nodo è un oggetto della classe tree.BinaryTree

Esempio: se K=5 e l'albero è il seguente
                    1                           # profondità 0
                /       \                       #
            25           7  ------------------- # 1
        /      \                                #
       3        65 ---------------------------- # 2
     /   \                                      #
    4     55  --------------------------------- # 3

la funzione ex4 deve tornare 3, perchè 55 è il nodo con valore
multiplo di 5 che si trova a profondità massima, ovvero 3. Gli
altri nodi potenziali sono 25 e 65, ma sono a una profondità
inferiore (rispettivamente 1 e 2).
"""
import tree

def profondita(root, k, prof):
    res = set()
    if root.value % k == 0:
        res.add(prof)
    if root.left:
        res.update(profondita(root.left, k, prof+1))
    if root.right:
        res.update(profondita(root.right, k, prof+1))
    return res

def ex4(node, k):
    prof = profondita(node, k, 0)
    if len(prof) == 0:
        prof = {-1}
    return  max(prof)



###################################################################################

if  __name__ == '__main__':
    pass
    # inserisci qui i tuoi test
