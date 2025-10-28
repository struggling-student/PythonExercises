#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# type: ignore

################################################################################
################################################################################
################################################################################

""" Operazioni da fare PRIMA DI TUTTO:
 1) Salvare il file come program.py
 2) Assegnare le variabili sottostanti con il tuo
    NOME, COGNOME, NUMERO DI MATRICOLA

Per superare l'esame è necessario:
    - ottenere un punteggio maggiore o uguale a 18

Il voto finale è la somma dei punteggi dei problemi risolti.

IMPORTANTE: impostare DEBUG = True in `grade.py` per aumentare il livello
di debug e conoscere dove un esercizio genera errore.
Ricordare che per testare e valutare la ricorsione è necessario
impostare DEBUG = False

Per commentare/decommentare il codice velocemente usate Control + 1 !
"""
nome       = "NOME"
cognome    = "COGNOME"
matricola  = "MATRICOLA"

#########################################

# %% ----------------------------------- FUNC1 ------------------------- #
''' func1: 2 punti

Implementa la funzione func1(testo:str) -> dict[str,list[int] che riceve come argomento:
- testo: una stringa di testo
e che ritorna un dizionario che ha come chiavi solo le lettere alfabetiche presenti nel testo
e, per ogni lettera, il numero medio di occorrenze nella stringa. Il numero medio è calcolato
come numero di occorrenze della lettera diviso lunghezza della stringa.
Il numero medio di occorrenze è arrotondato alla seconda cifra decimale usando la funzione round().

Esempio:
    testo = 'sopra la panca la capra campa, sotto la panca la capra crepa'
    expected = {'s': 0.03, 'o': 0.05, 'p': 0.12, 'r': 0.07, 'a': 0.27, 'l': 0.07,
                'n': 0.03, 'c': 0.1, 'm': 0.02, 't': 0.03, 'e': 0.02}
'''


def func1(text):
    # Your code here
    pass


# testo = 'sopra la panca la capra campa, sotto la panca la capra crepa'
# expected = {'s': 0.03, 'o': 0.05, 'p': 0.12, 'r': 0.07, 'a': 0.27, 'l': 0.07,
#             'n': 0.03, 'c': 0.1, 'm': 0.02, 't': 0.03, 'e': 0.02}
# print(func1(testo))

# %% ----------------------------------- FUNC2 ------------------------- #
''' func2: 2 punti

Si definisca la funzione func2(lists) che prende in ingresso una lista
di liste. Ciascuna lista interna contiene degli interi, anche ripetuti.
La funzione restituisce una lista che contiene tutte gli interi che sono
presenti in una sola delle liste interne, tante volte quante vi appaiono. 
Gli interi nella lista in uscita sono ordinati dal più grande al più piccolo.

Se lists = [[4, 4, 10, 4, 1, 10], [4, 2, 1], [1, 4]]

allora la funzione restituisce [10, 10, 2] in quanto 10 e 2 sono in una sola
lista; invece 1 e 4 non sono inclusi perché compaiono in più di una lista.

Si assuma che lists non sia mai vuota.
'''


def func2(lists: list[list[str]]) -> list[str]:
    # Your code here
    pass

# print(func2([[4, 4, 10, 4, 1, 10], [4, 2, 1], [1, 4]]))

# %% ----------------------------------- FUNC3 ------------------------- #
'''  func3: 4 punti
Si definisca la funzione func3(textfile_in, textfile_out) che riceve come argomento:
- textfile_in:  il percorso di un file di testo da leggere
- textfile_out: il percorso di un file di testo da creare

La funzione deve leggere il file textfile_in e scrivere nel file textfile_out.

Il file textfile_in contiene una serie di righe di testo, ciascuna delle quali
contiene una sequenza di numeri interi separati sicuramente da virgole e addizionalmente
da un numero variabile di spazi e \t.

La funzione deve scrivere nel file textfile_out una riga per ogni riga di textfile_in
contenente la somma dei numeri pari meno la somma dei numeri dispari trovati nella corrispondente
riga di textfile_in.
Nota: l'ultima riga del file textfile_out non è mai vuota!

La funzione deve ritornare la coppia (somma_pari, somma_dispari) dove somma_pari e somma_dispari
sono, rispettivamente, la somma di tutti i numeri pari e dispari del file.

Esempio: se il file contiene le righe:
    1,    2,    17, 22
    6, -38, 71, 50,  3
    12, -8, 190,  0,  1

Il file in output deve contenere le 3 righe:
6
-56
193

e la funzione deve tornare la coppia (somma_pari, somma_dispari) = (236, 93)
'''


def func3(textfile_in, textfile_out):
    # Your code here
    pass


# print(func3('func3/in_1.txt', 'func3/your_output_1.txt'))


# %% ----------------------------------- FUNC4 ------------------------- #
""" func4: 2 punti
Si definisca la funzione func4(S1 : set[str], S2 : set[str]) -> dict[str,list[str]]
che riceve come argomenti due insiemi di stringhe S1 e S2 e che torna come risultato
un dizionario che come chiavi ha le stringhe di S1 che sono sottostringhe di almeno una stringa di S2
e come valori la lista di stringhe di S2 che contengono quella particolare stringa di S1.
Le liste associate a ciascuna chiave devono essere ordinate in ordine decrescente
di lunghezza e, in caso di parità, in ordine alfabetico crescente.

Esempio:
S1 = {'a', 'b', 'c', 'e'}
S2 = {'aa', 'bb', 'cc', 'ab', 'bc', 'cd', 'abc'}
Risultato = {'a': ['abc', 'aa', 'ab'], 'b': ['abc', 'ab', 'bb', 'bc'], 'c': ['abc', 'bc', 'cc', 'cd']}
Nota: 'e' non è presente nel risultato perché non appare in nessuna stringa di S2.
"""

def func4(S1: set[str], S2: set[str]) -> dict[str, list[str]]:
    # Your code here
    pass


# S1 = {'a', 'b', 'c', 'e'}
# S2 = {'aa', 'bb', 'cc', 'ab', 'bc', 'cd', 'abc'}
# print(func4(S1, S2))

# %% ----------------------------------- FUNC5 ------------------------- #
""" func5: 8 punti

Definire la funzione func5(png_input: str) -> tuple[int,int] che prende in
ingresso una stringa png_input che indica il percorso ad una immagine
png.  L'immagine ha uno sfondo bianco e, sopra lo sfondo, sono disegnati
dei rettangoli pieni di colore uniforme (il colore è sempre diverso dal bianco)
che non si toccano né si sovrappongono.  Si veda ad esempio
l'immagine in func5/in_01.png. La funzione deve trovare i rettangoli presenti
nell'immagine e restituire un dizionario di item (key, value), in cui:
- key è una tupla (R, G, B) che rappresenta un colore;
- value è un intero che indica il numero di rettangoli di colore key
  trovati nell'immagine.

Ad esempio per l'immagine func5/in_01.png la funzione deve restituire:
{(28, 33, 221): 1, (187, 0, 0): 1, (187, 177, 0): 1, (191, 190, 186): 1, (0, 255, 7): 1}

Per caricare i file PNG si può usare load(png_path) della libreria images.
"""

import images


def func5(png_input):
    # Your code here
    pass


# print(func5("func5/in_01.png"))


# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex1: 6 punti

Si definisca la funzione ex1(root: BinaryTree) -> str che riceve in
ingresso la radice di un albero binario, come definito nella classe
`BinaryTree` del modulo tree.py e ritorna l'intero che corrisponde
al valore massimo che si può ottenere moltiplicando il valore di
un nodo per il suo livello, considerando che il livello della radice
è 1.

Esempio:

        ______20_____       level 1          ______13______
       |             |                      |              |
      15__        ___1___   level 2      ___7___        ___10___
          |      |       |              |       |      |        |
          -2    11       4  level 3    _-5_    -1_    _9_      _3_
                                      |    |      |  |   |    |   |
                            level 4 -10    4      6  5  -2    -6  2

 Se l'albero è quello di sinistra, la funzione deve restituire il valore 33=11*3

 Se l'albero è quello di destra, la funzione deve ritornare il valore 27=9*3
********************************************************************
NB: se scrivete una funziona addizionale, NON definite la funzione
ricorsiva addizionale come funzione interna ma mettetela al solito
livello di ex, come funzione esterna, altrimenti non passate il test
ricorsivo!
"""

from tree import BinaryTree

def ex1(root: BinaryTree) -> int:
    # Your code here
    pass

# root = BinaryTree.fromList([20, [15,None,[-2,None,None]],
# [1, [11,None,None], [4,None,None]]])
# print(ex1(root))
# 
# root = BinaryTree.fromList([13,
# [7,[-5,[-10,None,None],[4,None,None]],[-1,None,[6,None,None]]],
# [10, [9,[5,None,None],[-2,None,None]],
#  [3,[-6,None,None],[2,None,None]]]])
# print(ex1(root))

# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex2: 8 punti

Si definisca la funzione ex2(I : set[int], m : int, M : int) -> list[int]
ricorsiva o che utilizza funzioni o metodi ricorsivi, che prende in ingresso
un insieme di interi e una coppia di interi m e M, con m < M.
La funzione ritorna la lista di interi compresi fra m ed M inclusi
ottenuta considerando tutti i possibili valori ottenuti moltiplicando
uno o più elementi dell'insieme I, senza ripetizioni.
La lista ritornata è ordinata in modo crescente.

Esempio: ex2({2, 3, 7}, 5, 15) ritorna [6, 7, 14],
perchè i sottoinsiemi di {2, 3, 7} sono:
{2} -> prodotto 2 (minore di 5)
{3} -> prodotto 3 (minore di 5)
{7} -> prodotto 7 (OK)
{2, 3} -> prodotto 6 (OK)
{2, 7} -> prodotto 14 (OK)
{3, 7} -> prodotto 21 (maggiore di 15)
{2, 3, 7} -> prodotto 42 (maggiore di 15)

NOTA: è vietato importare librerie esterne a parte quelle già importate.

********************************************************************
NB: se scrivete una funziona addizionale, NON definite la funzione
ricorsiva addizionale come funzione interna ma mettetela al solito
livello di ex, come funzione esterna, altrimenti non passate il test
ricorsivo!
********************************************************************
"""

def ex2(I : set[int], m : int, M : int) -> list[int]:
    # Your code here
    pass

# print(ex2({1, 2, 3, 7}, 1, 15))
    
# %% 
###################################################################################
if __name__ == '__main__':
    # Scrivi qui i tuoi test
    print('*'*50)
    print('Devi eseguire il grade.py se vuoi debuggare con il grader incorporato.')
    print('Altrimenit puoi inserire qui del codice per testare le tue funzioni ma devi scriverti i casi che vuoi testare')
    print('*'*50)
    
    # from tree import BinaryTree
    # root = BinaryTree.fromList(['A', ['B',[],['D',[],[]]], ['C', ['E',[],[]], ['F',[],[]]]])
    # print(ex1(root))
    # root = BinaryTree.fromList(['A', ['B',['D',['H',[],[]],['I',[],[]]],['E',[],['J',[],[]]]], ['C', ['F',['K',[],[]],['L',[],[]]], ['G',['M',[],[]],['N',[],[]]]]])
    # print(ex1(root))
    # 
    # ex2({1, 2, 3, 7}, 1, 15)


