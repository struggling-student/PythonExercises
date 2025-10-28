#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List, Dict
import os
import tree

################################################################################
################################################################################
################################################################################

"""
Prima di tutto, assegna le variabili sottostanti con il tuo NOME, COGNOME,
NUMERO DI MATRICOLA

Aggiungi le tue implementazioni delle funzioni descritte sotto.

Il voto finale e' la somma dei punteggi dei problemi risolti.
Per superare la simulazione e' sufficiente ottenere un punteggio maggiore o
uguale a 18 (le persone con DSA devono ottenere almeno 15, previa
comunicazione dal Servizio DSA di Sapienza).

Per ottenere il punteggio esegui il file grade.py contenuto nella cartella.
Setta DEBUG=True nel grade.py per visualizzare la stack trace degli errori.

Per commentare/decommentare il codice velocemente puoi usare la
combinazione di tasti Control + 1
"""

nome = "NOME"
cognome = "COGNOME"
matricola = "MATRICOLA"

# %% ----------------------------------- FUNC1 ------------------------- #

"""
 func1: 6 punti
Scrivere una funzione ricorsiva func1(lista) che, data una lista di
elementi, restituisca un dizionario in cui le chiavi sono gli elementi della 
lista e i valori rappresentano il numero di occorrenze di ciascun elemento.

NOTA: È possibile chiamare funzioni ricorsive, che però non possono essere 
interne (ossia, le funzioni ricorsive possono solo essere definite al livello 
più alto del modulo e non possono essere definite all'interno di 
altre funzioni o classi). 
"""


def func1(l: List, counts: Dict = None) -> Dict:
    pass


# %% ----------------------------------- FUNC2 ------------------------- #
"""
func2: 9 punti

Si scriva una funzione ricorsiva func2(directory), o che al suo interno
usi una funzione ricorsiva, che prende in ingresso una stringa
'directory' che rappresenta il percorso ad una directory.

La funzione deve esplorare ricorsivamente l'albero delle directory con
radice in 'directory' e restituire un dizionario.
Le chiavi del dizionario sono i percorsi delle sotto-directory di
'directory', sottoforma di stringa.

Il valore associato alla chiave di una directory è un set di stringhe con i 
nomi di file '.txt' nella directory il cui contenuto inizia e finisce con lo 
stesso carattere. 

Se una directory non contiene nessun file .txt con tale 
caratteristica, allora quella directory non appare nel dizionario.

Se la funzione e' chiamata su 'func2/A', ritorna:

{'func2/A/B': {'b.txt'}, 'func2/A/C': {'c.txt'}}

NOTA: e' proibito usare la funzione os.walk. Si possono usare:
  os.listdir, os.path.isfile, os.path.exists, etc.  Per concatenare i
  path, si usi l'operazione di concatenazione con il carattere '/'

NOTA: consigliamo fortemente di dividere l'esercizio in sottoproblemi
  dividendo in funzioni per ogni sottoproblema.  
  
NOTA: È possibile chiamare funzioni ricorsive, che però non possono essere 
interne (ossia, le funzioni ricorsive possono solo essere definite al livello 
più alto del modulo e non possono essere definite all'interno di 
altre funzioni o classi). 
"""


def func2(root):
    pass


#%% ----------------------------------- FUNC3 ------------------------- #
""" func3: 5 punti 

Il massimo comun divisore (GCD) di due numeri interi positivi è il numero 
intero più grande che divide entrambi i numeri senza lasciare resto.

La procedura per calcolare il GCD segue questi passi:

- Prendi due numeri, a e b.
- Controlla se il secondo numero (b) è uguale a 0:
    - Se sì, il GCD è il primo numero (a).
    - Se no, calcola il resto della divisione di a per b (a%b).
- Ripeti la procedura con i nuovi valori:
    - Sostituisci a con il valore di b.
    - Sostituisci b con il valore del resto calcolato (a%b).
    - Continua fino a quando b diventa 0. A quel punto, il GCD è il valore 
corrente di a.

Scrivi una funzione ricorsiva o che fa uso di funzioni ricorsive che 
calcoli il GCD di due numeri. Assumi che a e b siano interi non-negativi.

Esempio: Troviamo il GCD di 48 e 18:

1. 48 % 18 = 12 (il resto di 48 diviso per 18 è 12).
2. Ora calcoliamo il GCD di 18 e 12: 18 % 12 = 6.
3. Ora calcoliamo il GCD di 12 e 6: 12 % 6 = 0.
4. Il resto è 0, quindi il GCD è 6.

NOTA: È possibile chiamare funzioni ricorsive, che però non possono essere 
interne (ossia, le funzioni ricorsive possono solo essere definite al livello 
più alto del modulo e non possono essere definite all'interno di 
altre funzioni o classi). 
"""


def func3(a: int, b: int) -> int:
    pass


# ---------------------------- FUNC 4 ---------------------------- #
""" func4: 10 punti

Scrivere una funzione ricorsiva o che fa uso di funzioni ricorsive che
prende in input un albero root (costituito da nodi istanza della classe
BinaryTree del modulo tree) e un valore intero k e restituisce due interi.

Il primo valore da restituire è dato dalla somma di tutti i nodi
dell'albero che sono ad un livello pari meno la somma di tutti i nodi
dell'albero che sono ad un livello dispari.
La radice è al livello 0 e si considera pari.

Il secondo valore da restituire è il numero di nodi che hanno un valore
maggiore del valore k preso in input.

    Es:

        ______5______                        ______2______
       |             |                      |             |
       8__        ___2___                __ 7__        ___5___
          |      |       |              |      |      |       |
          3      9       1             _4_     3_    _0_     _5_
                                      |   |      |  |   |   |   |
                                      2   -1     1  8   3   2   9

    Se l'albero è quello di sinistra e k=2, la funzione ritorna la coppia
    8, 4.
    Se l'albero è quello di destra e k=3, la funzione ritorna la coppia
    -22, 6.
"""


def func4(root, k):
    pass


if __name__ == '__main__':
    pass
# ---------------------------- EOF ---------------------------- #
